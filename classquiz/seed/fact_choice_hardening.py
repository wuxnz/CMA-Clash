# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Assign difficulty and harden ABCD choices to reduce giveaway patterns."""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from typing import Sequence

from classquiz.seed.catalog import CERTIFICATIONS, TOPIC_QUESTIONS_PER_QUIZ
from classquiz.seed.stem_normalize import normalize_stem

VALID_DIFFICULTIES = frozenset({"beginner", "intermediate", "advanced"})
_DIFFICULTY_ALIASES = {
    "easy": "beginner",
    "medium": "intermediate",
    "hard": "advanced",
    "beginner": "beginner",
    "intermediate": "intermediate",
    "advanced": "advanced",
}

_FORBIDDEN_CHOICE = re.compile(
    r"all of the above|none of the above|both a and b|not enough information",
    re.IGNORECASE,
)
_OBVIOUS_WRONG = re.compile(
    r"without exception|only always|whole pizza|never ever|always wrong|ignore all",
    re.IGNORECASE,
)
_ABSOLUTE_GIVEAWAY = re.compile(r"\b(never|always|only)\b", re.IGNORECASE)

_SCENARIO_START = re.compile(
    r"^(your patient|a patient|during |while |in clinic|on the (ward|unit|floor)|"
    r"the (ekg|ecg|tracing|monitor)|an adult|a child|a coworker)",
    re.IGNORECASE,
)

_SCENARIO_PREFIX: dict[str, str] = {
    "cpr": "During BLS on an unresponsive patient, ",
    "phleb": "During venipuncture in outpatient lab, ",
    "ekg": "While acquiring a 12-lead ECG, ",
    "ccma": "In an ambulatory clinic, ",
}

_QUIZ_BANK_SIZE = 28
_LENGTH_PADS = (
    " per protocol",
    " when ordered",
    " if stable",
    " in adults",
    " per policy",
)

# Plausible same-category wrong answers by topic family (beginner tier).
_BEGINNER_POOL: dict[str, tuple[str, ...]] = {
    "cpr": (
        "15 compressions to 2 breaths for a lone adult",
        "Compress to about 1 inch depth",
        "Ventilate every 30 seconds without compressions",
    ),
    "phleb": (
        "Lavender EDTA tube before blood cultures",
        "Invert serum tubes vigorously for 30 seconds",
        "Label tubes after leaving the patient room",
    ),
    "ekg": (
        "Place all limb leads on the same arm",
        "Document artifact as normal sinus rhythm",
        "Use only one chest lead for diagnosis",
    ),
    "ccma": (
        "Skip hand hygiene when gloves are worn",
        "Use one identifier to confirm the patient",
        "Document only abnormal vital signs",
    ),
}

# Near-miss swaps for intermediate (pattern on correct -> distractor ideas).
_INTERMEDIATE_SWAPS: tuple[tuple[re.Pattern[str], tuple[str, ...]], ...] = (
    (
        re.compile(r"30 compressions to 2 breaths", re.I),
        (
            "15 compressions to 2 breaths",
            "30 compressions to 1 breath",
            "5 compressions to 1 breath",
        ),
    ),
    (
        re.compile(r"100 to 120", re.I),
        ("90 to 100 compressions per minute", "110 to 130 compressions per minute", "60 to 80 per minute"),
    ),
    (
        re.compile(r"2 inches \(5 cm\)", re.I),
        ("At least 1 inch (2.5 cm)", "At least 3 inches (7.5 cm)", "Depth is not measured"),
    ),
    (
        re.compile(r"blood culture", re.I),
        (
            "Sodium citrate tube before cultures",
            "EDTA tube before cultures",
            "Serum tube before cultures",
        ),
    ),
    (
        re.compile(r"alveoli", re.I),
        ("Bronchi", "Trachea", "Pleural space only"),
    ),
)


def _topic_family(topic: str) -> str:
    if topic.startswith("cpr"):
        return "cpr"
    if topic.startswith("phleb") or topic.startswith("skill-specimen"):
        return "phleb"
    if topic.startswith("ekg"):
        return "ekg"
    return "ccma"


def normalize_difficulty(value: str | None) -> str:
    if not value:
        return "intermediate"
    key = str(value).strip().lower()
    return _DIFFICULTY_ALIASES.get(key, "intermediate")


def assign_difficulties_by_topic(facts: list[dict]) -> None:
    """Ensure each fact has beginner/intermediate/advanced (~30/40/30 per topic)."""
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for fact in facts:
        by_topic[str(fact["topic"])].append(fact)

    for _topic, items in by_topic.items():
        locked: dict[str, str] = {}
        for f in items:
            raw = normalize_difficulty(f.get("difficulty"))
            if raw in ("beginner", "advanced"):
                locked[normalize_stem(f["stem"])] = raw
        items.sort(key=lambda f: normalize_stem(f["stem"]))
        n = len(items)
        targets = {
            "beginner": int(round(n * 0.30)),
            "intermediate": int(round(n * 0.40)),
            "advanced": n - int(round(n * 0.30)) - int(round(n * 0.40)),
        }
        counts: dict[str, int] = defaultdict(int)
        for f in items:
            stem_k = normalize_stem(f["stem"])
            if stem_k in locked:
                f["difficulty"] = locked[stem_k]
                counts[f["difficulty"]] += 1
        for f in items:
            if normalize_stem(f["stem"]) in locked:
                continue
            deficits = {d: targets[d] - counts[d] for d in targets}
            label = max(deficits, key=lambda d: (deficits[d], d == "intermediate"))
            if deficits[label] <= 0:
                label = min(targets, key=lambda d: counts[d])
            f["difficulty"] = label
            counts[label] += 1


def _stem_hash(stem: str) -> int:
    return int(hashlib.sha256(normalize_stem(stem).encode("utf-8")).hexdigest()[:12], 16)


def _numeric_near_miss(text: str, salt: int) -> str | None:
    match = re.search(r"(\d+(?:\.\d+)?)(\s*(?:to|-)\s*(\d+(?:\.\d+)?))?", text)
    if not match:
        return None
    a = float(match.group(1))
    b = float(match.group(3)) if match.group(3) else None
    delta = 10 if a >= 20 else 1
    if salt % 3 == 0:
        na = a + delta
        nb = (b + delta) if b is not None else None
    elif salt % 3 == 1:
        na = max(1, a - delta)
        nb = (max(1, b - delta)) if b is not None else None
    else:
        na = a + delta / 2
        nb = (b + delta / 2) if b is not None else None
    if b is not None and match.group(2):
        rep = f"{int(na) if na == int(na) else na}{match.group(2)}{int(nb) if nb and nb == int(nb) else nb}"
        return text[: match.start()] + rep + text[match.end() :]
    na_i = int(na) if na == int(na) else na
    return text[: match.start()] + str(na_i) + text[match.end() :]


_ANTONYM_SWAPS: tuple[tuple[str, str], ...] = (
    ("before", "after"),
    ("first", "last"),
    ("increase", "decrease"),
    ("higher", "lower"),
    ("superior", "inferior"),
    ("anterior", "posterior"),
    ("proximal", "distal"),
    ("systolic", "diastolic"),
    ("left", "right"),
)


def _partial_truth_from_correct(correct: str, salt: int) -> str | None:
    text = correct
    for a, b in _ANTONYM_SWAPS:
        if a in text.lower():
            return _compact_choice(re.sub(a, b, text, count=1, flags=re.I))
        if b in text.lower():
            return _compact_choice(re.sub(b, a, text, count=1, flags=re.I))
    words = text.split()
    if len(words) > 4:
        return _compact_choice(" ".join(words[:-1]))
    near = _numeric_near_miss(correct, salt)
    return _compact_choice(near) if near else None


def _fallback_distractor(correct: str, topic: str, stem: str, salt: int) -> str:
    near = _numeric_near_miss(correct, salt + _stem_hash(stem))
    if near and near.lower() != correct.lower():
        return _compact_choice(near)
    partial = _partial_truth_from_correct(correct, salt)
    if partial and partial.lower() != correct.lower():
        return partial
    pool = _BEGINNER_POOL.get(_topic_family(topic), _BEGINNER_POOL["ccma"])
    return _compact_choice(pool[salt % len(pool)])


def _intermediate_distractors(correct: str, topic: str, stem: str, existing: Sequence[str]) -> list[str]:
    correct_l = correct.lower()
    for pattern, options in _INTERMEDIATE_SWAPS:
        if pattern.search(correct):
            picks = [o for o in options if o.lower() != correct_l]
            if len(picks) >= 3:
                return picks[:3]
    out: list[str] = []
    seen = {correct_l}
    for i, d in enumerate(existing):
        text = d.strip()
        if _FORBIDDEN_CHOICE.search(text) or _OBVIOUS_WRONG.search(text):
            text = _numeric_near_miss(correct, i + _stem_hash(stem)) or text
        if text.lower() in seen:
            near = _numeric_near_miss(text, i + 1)
            text = near or text
        seen.add(text.lower())
        out.append(text)
    attempts = 0
    while len(out) < 3 and attempts < 12:
        attempts += 1
        near = _numeric_near_miss(correct, len(out) + attempts + _stem_hash(stem))
        if near and near.lower() not in seen:
            out.append(near)
            seen.add(near.lower())
            continue
        filler = _BEGINNER_POOL[_topic_family(topic)][len(out) % 3]
        variant = _clean_choice(f"{filler}{_LENGTH_PADS[attempts % len(_LENGTH_PADS)]}")
        if variant.lower() not in seen:
            out.append(variant)
            seen.add(variant.lower())
    return out[:3]


def _sanitize_distractor_list(
    correct: str, topic: str, stem: str, existing: Sequence[str]
) -> list[str]:
    out: list[str] = []
    seen = {correct.strip().lower()}
    for i, raw in enumerate(list(existing)[:3]):
        text = _compact_choice(str(raw).strip())
        if (
            _FORBIDDEN_CHOICE.search(text)
            or _OBVIOUS_WRONG.search(text)
            or (_ABSOLUTE_GIVEAWAY.search(text) and not _ABSOLUTE_GIVEAWAY.search(correct))
            or len(text) < 4
        ):
            text = _fallback_distractor(correct, topic, stem, i)
        if text.lower() in seen:
            text = _fallback_distractor(correct, topic, stem, i + 3)
        seen.add(text.lower())
        out.append(text)
    while len(out) < 3:
        text = _fallback_distractor(correct, topic, stem, len(out) + 5)
        if text.lower() not in seen:
            out.append(text)
            seen.add(text.lower())
    return out[:3]


def _advanced_stem(topic: str, stem: str) -> str:
    if _SCENARIO_START.search(stem):
        return stem
    prefix = _SCENARIO_PREFIX.get(_topic_family(topic), "In this scenario, ")
    s = stem.strip()
    if s.endswith("?") and not _SCENARIO_START.search(s):
        lead = s[0].lower() + s[1:] if len(s) > 1 else s
        return prefix + lead
    return prefix + s


def _light_length_balance(correct: str, distractors: list[str]) -> list[str]:
    out = list(distractors)
    fact = {"correct": correct, "distractors": out}
    if not _is_correct_strictly_longest(fact):
        return out
    idx = min(range(len(out)), key=lambda i: len(out[i]))
    pad = _LENGTH_PADS[idx % len(_LENGTH_PADS)]
    if len(out[idx]) + len(pad) <= 58:
        out[idx] = _compact_choice(out[idx].rstrip(".") + pad)
    return out


def _compact_choice(text: str, limit: int = 58) -> str:
    text = text.replace("—", "-").replace("–", "-").strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) <= limit:
        return text
    for sep in (";", ","):
        if sep in text:
            candidate = text.split(sep)[0].strip()
            if len(candidate) >= 12:
                text = candidate
                break
    if len(text) > limit:
        text = text[: limit - 1].rstrip()
    return text


def _clean_choice(text: str, limit: int = 58) -> str:
    return _compact_choice(text, limit)


def harden_fact_choices(fact: dict) -> dict:
    topic = str(fact["topic"])
    difficulty = normalize_difficulty(fact.get("difficulty"))
    correct = _compact_choice(str(fact["correct"]), 58)
    stem = str(fact["stem"])
    distractors = _sanitize_distractor_list(correct, topic, stem, fact.get("distractors") or [])

    if difficulty == "intermediate":
        slot = _stem_hash(stem) % 3
        for pattern, options in _INTERMEDIATE_SWAPS:
            if pattern.search(correct) or pattern.search(stem):
                for opt in options:
                    if opt.lower() != correct.lower():
                        distractors[slot] = _compact_choice(opt)
                        break
                break
        else:
            near = _numeric_near_miss(correct, slot + _stem_hash(stem))
            if near:
                distractors[slot] = _compact_choice(near)
    elif difficulty == "advanced":
        stem = _advanced_stem(topic, stem)
        partial = _partial_truth_from_correct(correct, _stem_hash(stem))
        if partial:
            distractors[0] = partial
        if len(distractors) > 1 and "next step" not in distractors[1].lower():
            distractors[1] = _compact_choice(
                distractors[1].rstrip(".") + " when another protocol applies"
            )

    distractors = _light_length_balance(correct, distractors)
    return {**fact, "stem": stem, "correct": correct, "distractors": distractors[:3], "difficulty": difficulty}


def _is_correct_strictly_longest(fact: dict) -> bool:
    correct = fact["correct"]
    lens = [len(correct)] + [len(d) for d in fact["distractors"]]
    if len(correct) <= max(len(d) for d in fact["distractors"]):
        return False
    return len(correct) - min(lens) >= 10


def balance_correct_length_in_quiz_chunks(facts: list[dict]) -> None:
    """Ensure correct is longest for at most ~30% of questions in each seeded quiz chunk."""
    by_key: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for fact in facts:
        key = (str(fact["topic"]), normalize_difficulty(fact.get("difficulty")))
        by_key[key].append(fact)

    for (_topic, _diff), items in by_key.items():
        chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(_topic, _QUIZ_BANK_SIZE)
        for start in range(0, len(items), chunk_size):
            chunk = items[start : start + chunk_size]
            if not chunk:
                continue
            allowed = max(1, int(round(len(chunk) * 0.30)))
            guard = 0
            while guard < 40:
                guard += 1
                longest_idxs = [i for i, f in enumerate(chunk) if _is_correct_strictly_longest(f)]
                if len(longest_idxs) <= allowed:
                    break
                i = max(longest_idxs, key=lambda j: _stem_hash(chunk[j]["stem"]))
                f = chunk[i]
                target = len(f["correct"])
                ds = list(f["distractors"])
                for j in range(3):
                    text = ds[j].rstrip(".")
                    step = 0
                    while len(text) < target and len(text) + 12 <= 58 and step < 4:
                        text += _LENGTH_PADS[(j + step) % len(_LENGTH_PADS)]
                        step += 1
                    ds[j] = _compact_choice(text)
                f["distractors"] = ds


def apply_choice_hardening(facts: list[dict]) -> list[dict]:
    assign_difficulties_by_topic(facts)
    hardened = [harden_fact_choices(f) for f in facts]
    balance_correct_length_in_quiz_chunks(hardened)
    return hardened
