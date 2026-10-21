# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Normalize stems, distractors, and explanations for all seed facts at load time."""

from __future__ import annotations

import re
from typing import Sequence

_JOKE_DISTRACTOR = re.compile(
    r"always without|only always|without exception|whole pizza|growth set|historically but now",
    re.IGNORECASE,
)

_STEM_FIXES: tuple[tuple[str, str], ...] = (
    (r"\s*\(growth set \d+\)\s*\?", ""),
    (r"\s*\(growth set \d+\)\s*", ""),
    ("CLIA-waived test means:", "Under CLIA, a waived laboratory test is one that:"),
    ("CLIA-waived POC testing is:", "Point-of-care testing under a CLIA waiver must be:"),
)

_GENERIC_DISTRACTORS: tuple[str, ...] = (
    "A step that conflicts with standard safety practice",
    "An action that would skew or contaminate the specimen",
    "A ratio or depth outside current BLS guidelines",
    "A technique that increases risk of injury or error",
)

_TOPIC_DISTRACTORS: dict[str, tuple[str, ...]] = {
    "cpr": (
        "15:2 for all adult BLS teams",
        "Compression depth of about 1 inch only",
        "A compression rate near 60 per minute",
    ),
    "phleb": (
        "EDTA tube drawn before blood cultures",
        "Shaking additive tubes vigorously after fill",
        "Reusing needles between patients",
    ),
    "ekg": (
        "Lead placement with all electrodes on one limb",
        "Ignoring patient motion as never causing artifact",
        "ST elevation in every lead as a normal finding",
    ),
    "ccma": (
        "Working outside scope without provider oversight",
        "Skipping hand hygiene between patients",
        "Sharing needles between patients",
    ),
}


def _topic_prefix(topic: str) -> str:
    if topic.startswith("cpr"):
        return "cpr"
    if topic.startswith("phleb") or topic.startswith("skill-specimen"):
        return "phleb"
    if topic.startswith("ekg"):
        return "ekg"
    if topic.startswith("ccma") or topic.startswith("skill"):
        return "ccma"
    return "ccma"


def _sentence_count(text: str) -> int:
    parts = [p.strip() for p in re.split(r"[.!?]+", text) if p.strip()]
    return len(parts)


def clean_stem(stem: str) -> str:
    text = stem.replace("—", "-").replace("–", "-").strip()
    for pattern, repl in _STEM_FIXES:
        if pattern.startswith("(") or pattern.startswith("\\"):
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        else:
            text = text.replace(pattern, repl)
    text = re.sub(r":\s*\?", "?", text)
    if text.endswith(":") and len(text.split()) <= 6:
        text = text[:-1] + "?"
    if not text.endswith("?") and not text.endswith("."):
        if text.endswith(":"):
            text = text[:-1] + "?"
    return text.strip()


def _needs_distractor_replace(d: str) -> bool:
    return len(d) > 58 or bool(_JOKE_DISTRACTOR.search(d))


def _replacement_distractor(topic: str, index: int) -> str:
    pool = _TOPIC_DISTRACTORS.get(_topic_prefix(topic), _GENERIC_DISTRACTORS)
    return pool[index % len(pool)]


def sanitize_distractors(topic: str, correct: str, distractors: Sequence[str]) -> list[str]:
    out: list[str] = []
    seen = {correct.strip().lower()}
    rep_i = 0
    for d in distractors:
        text = d.replace("—", "-").replace("–", "-").strip()
        if _needs_distractor_replace(text):
            text = _replacement_distractor(topic, rep_i)
            rep_i += 1
        key = text.lower()
        if key in seen:
            text = _replacement_distractor(topic, rep_i)
            rep_i += 1
            key = text.lower()
        seen.add(key)
        out.append(text)
    while len(out) < 3:
        text = _replacement_distractor(topic, rep_i)
        rep_i += 1
        if text.lower() not in seen:
            out.append(text)
            seen.add(text.lower())
    return out[:3]


def _pick_tempting_wrong(distractors: Sequence[str], correct: str) -> str:
    for d in distractors:
        if d.strip().lower() == correct.strip().lower():
            continue
        if not _needs_distractor_replace(d):
            return d.strip()
    return distractors[0].strip() if distractors else "another option"


def enrich_explanation(fact: dict) -> str:
    correct = str(fact["correct"]).strip()
    distractors = fact.get("distractors") or []
    wrong = _pick_tempting_wrong(distractors, correct)
    base = str(fact.get("explanation") or "").strip().replace("—", "-").replace("–", "-")

    if _sentence_count(base) >= 2 and len(base) >= 80:
        return base

    sentences: list[str] = []
    if base:
        if base[-1] not in ".!?":
            base += "."
        sentences.append(base)
    else:
        sentences.append(f"{correct} is the answer keyed to current exam references for this topic.")

    joined = " ".join(sentences).lower()
    if wrong.lower() not in joined:
        short_wrong = wrong if len(wrong) <= 52 else wrong[:49].rstrip() + "..."
        sentences.append(
            f'"{short_wrong}" is incorrect here because it conflicts with the safety rule or number in the stem.'
        )

    text = " ".join(sentences)
    if len(text) < 80:
        sentences.append(f"The correct option is {correct}.")
        text = " ".join(sentences)
    if len(text) < 80:
        sentences.append("Check the linked reference for the full calculation or protocol.")
        text = " ".join(sentences)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def finalize_fact(fact: dict) -> dict:
    topic = str(fact["topic"])
    stem = clean_stem(str(fact["stem"]))
    correct = str(fact["correct"]).strip()
    distractors = sanitize_distractors(topic, correct, list(fact.get("distractors") or []))
    updated = {**fact, "stem": stem, "correct": correct, "distractors": distractors}
    updated["explanation"] = enrich_explanation(updated)
    return updated
