# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Authoritative tier-appropriate stems, choices, and explanations for materialized banks."""

from __future__ import annotations

import re
from typing import Sequence

from classquiz.seed.fact_choice_hardening import (
    DISTRACTOR_GIVEAWAY_WORDS,
    normalize_difficulty,
    stem_hash,
)

_PATIENTS = (
    "A 48-year-old patient in primary care",
    "A 61-year-old patient in the outpatient lab",
    "A 34-year-old patient on the medical-surgical unit",
    "A 77-year-old patient in urgent care",
    "A 29-year-old patient in occupational health",
)

_GIVEAWAY_REPLACE = {
    "always": "typically",
    "never": "rarely",
    "only": "primarily",
    "any": "each",
    "random": "alternate",
}


def _dash_to_to(text: str) -> str:
    text = text.replace("–", " to ").replace("—", " to ")
    text = re.sub(r"(\d)\s*-\s*(\d)", r"\1 to \2", text)
    return re.sub(r"\s+", " ", text).strip()


def _clean_giveaway_distractor(text: str, correct: str) -> str:
    if not DISTRACTOR_GIVEAWAY_WORDS.search(text) or DISTRACTOR_GIVEAWAY_WORDS.search(correct):
        return text.strip()
    out = text
    for bad, repl in _GIVEAWAY_REPLACE.items():
        out = re.sub(rf"\b{bad}\b", repl, out, flags=re.IGNORECASE)
    if DISTRACTOR_GIVEAWAY_WORDS.search(out):
        for bad in _GIVEAWAY_REPLACE:
            out = re.sub(rf"\b{bad}\b", "", out, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", out).strip(" ,;")


def _pick_three(correct: str, options: Sequence[str]) -> list[str]:
    seen = {correct.strip().lower()}
    out: list[str] = []
    for opt in options:
        o = opt.strip()
        if o.lower() in seen:
            continue
        seen.add(o.lower())
        out.append(o)
        if len(out) == 3:
            break
    return out


def _balance_lengths(correct: str, distractors: list[str]) -> tuple[str, list[str]]:
    correct = correct.strip()
    ds = [_clean_giveaway_distractor(d, correct) for d in distractors]
    max_d = max(len(d) for d in ds) if ds else 0
    while len(correct) > max_d + 10:
        if correct.rstrip().endswith((" or", " and")):
            break
        if ", and " in correct:
            correct = correct.split(", and ")[0].strip()
        elif "," in correct:
            correct = correct.split(",")[0].strip()
        elif " (" in correct:
            correct = correct.split(" (")[0].strip()
        else:
            break
        max_d = max(len(d) for d in ds)
    return correct, ds


def _explanation(correct: str, distractors: list[str], base: str, why_correct: str) -> str:
    base = _dash_to_to(base)
    wrong = distractors[0] if distractors else "another option"
    s1 = (base or why_correct).strip()
    if s1 and s1[-1] not in ".!?":
        s1 += "."
    s2 = (
        f"{wrong} is a common near miss because it sounds related but does not match "
        f"the guideline or value required here."
    )
    s3 = why_correct.strip() if why_correct else f"{correct} is the best answer for this stem."
    if s3[-1] not in ".!?":
        s3 += "."
    return _dash_to_to(f"{s1} {s2} {s3}")


def _rewrite_cpr_intermediate(fact: dict) -> dict | None:
    stem_l = fact["stem"].lower()
    correct = fact["correct"]
    if "compression rate" in stem_l or "compressions per minute" in correct.lower():
        return {
            **fact,
            "stem": "During adult BLS, high-quality chest compressions should be delivered at what rate?",
            "correct": "100 to 120 compressions per minute",
            "distractors": _pick_three(
                "100 to 120 compressions per minute",
                (
                    "90 to 100 compressions per minute",
                    "110 to 130 compressions per minute",
                    "100 to 110 compressions per minute",
                ),
            ),
            "explanation": _explanation(
                "100 to 120 compressions per minute",
                ["110 to 130 compressions per minute"],
                "AHA adult BLS targets 100 to 120 compressions per minute.",
                "Rates below 100 are too slow to perfuse; rates well above 120 limit ventricular filling.",
            ),
        }
    if "30" in correct and "2" in correct and "compression" in stem_l:
        return {
            **fact,
            "stem": "A single rescuer is performing adult BLS with ventilations. What compression-to-ventilation ratio is used?",
            "correct": "30 compressions to 2 breaths",
            "distractors": _pick_three(
                "30 compressions to 2 breaths",
                (
                    "15 compressions to 2 breaths",
                    "30 compressions to 1 breath",
                    "5 compressions to 1 breath",
                ),
            ),
            "explanation": _explanation(
                "30 compressions to 2 breaths",
                ["15 compressions to 2 breaths"],
                "AHA 2020 adult BLS uses 30:2 for a single rescuer.",
                "15:2 is used for two-rescuer child CPR, not single-rescuer adult BLS.",
            ),
        }
    if "2 inch" in correct.lower() or "5 cm" in correct.lower():
        return {
            **fact,
            "stem": "For adult chest compressions, what depth is recommended?",
            "correct": "At least 2 inches (5 cm), not more than 2.4 inches (6 cm)",
            "distractors": _pick_three(
                "At least 2 inches (5 cm), not more than 2.4 inches (6 cm)",
                (
                    "At least 1 inch (2.5 cm) for all adults",
                    "At least 3 inches (7.5 cm) for all adults",
                    "2 inches (5 cm) to 2.4 inches (6 cm) maximum depth",
                ),
            ),
            "explanation": _explanation(
                "At least 2 inches (5 cm), not more than 2.4 inches (6 cm)",
                ["At least 1 inch (2.5 cm) for all adults"],
                "AHA recommends at least 2 inches with avoidance of excessive depth.",
                "Shallow compressions fail to perfuse; excessive depth risks injury.",
            ),
        }
    return None


def _rewrite_phleb_advanced(fact: dict, h: int) -> dict | None:
    topic = fact["topic"]
    if not topic.startswith("phleb") and topic != "skill-specimen-lab":
        return None
    stem_l = fact["stem"].lower()
    if "order" in stem_l or "draw" in stem_l or "culture" in stem_l or "citrate" in stem_l:
        scenarios = (
            {
                "stem": (
                    "A butterfly set is used after paired blood cultures were collected. "
                    "STAT PT/INR and CMP are ordered. Which tube should be collected next?"
                ),
                "correct": "Light blue (3.2% sodium citrate) tube",
                "distractors": (
                    "Gold SST tube before the light blue tube",
                    "Lavender EDTA before light green plasma separator",
                    "Omit the discard tube, then fill light blue citrate",
                ),
                "explanation": _explanation(
                    "Light blue (3.2% sodium citrate) tube",
                    ["Gold SST tube before the light blue tube"],
                    "CLSI GP41 order of draw places citrate early after cultures to protect coagulation studies.",
                    "SST before citrate can contaminate coagulation results; EDTA before heparin/plasma steps is also out of sequence.",
                ),
            },
            {
                "stem": (
                    "Cultures are finished on a butterfly set. The provider ordered CBC and CMP. "
                    "Which tube should you collect next?"
                ),
                "correct": "Gold serum separator (SST) tube",
                "distractors": (
                    "Lavender EDTA tube before the SST tube",
                    "Light green lithium heparin before SST",
                    "Gray fluoride tube before lavender EDTA",
                ),
                "explanation": _explanation(
                    "Gold serum separator (SST) tube",
                    ["Lavender EDTA tube before the SST tube"],
                    "After blood cultures, CLSI GP41 places serum tubes ahead of EDTA when both are drawn on the same line.",
                    "Drawing EDTA before serum can carry additive into chemistry specimens.",
                ),
            },
        )
        pick = scenarios[h % len(scenarios)]
        return {**fact, **pick}
    return None


def _rewrite_advanced(fact: dict) -> dict:
    h = stem_hash(fact["stem"])
    topic = fact["topic"]
    specialized = _rewrite_phleb_advanced(fact, h)
    if specialized:
        return specialized
    patient = _PATIENTS[h % len(_PATIENTS)]
    core = fact["stem"].strip().rstrip("?")
    if core.endswith(":"):
        core = core[:-1]
    if not re.match(r"^[A-Z]", core):
        core = core[0].upper() + core[1:] if core else core
    stem = f"{patient} presents for care. {core}?"
    base_ds = [_clean_giveaway_distractor(d, fact["correct"]) for d in fact.get("distractors") or []]
    if len(base_ds) < 3:
        base_ds.extend(
            [
                _partial_truth_from_correct(fact["correct"], h) or "Related action at the wrong step",
                _near_synonym_wrong(fact["correct"], topic),
                _context_shift(fact["correct"], topic, h),
            ]
        )
    return {
        **fact,
        "stem": stem,
        "distractors": _pick_three(fact["correct"], base_ds),
    }


def _swap_direction(text: str) -> str:
    for a, b in (("before", "after"), ("first", "last"), ("superior", "inferior"), ("left", "right")):
        if a in text.lower():
            return re.sub(a, b, text, count=1, flags=re.IGNORECASE)
        if b in text.lower():
            return re.sub(b, a, text, count=1, flags=re.IGNORECASE)
    return f"Reverse the usual sequence: {text}"


def _near_synonym_wrong(correct: str, topic: str) -> str:
    if topic.startswith("phleb"):
        return "Invert all additive tubes 10 times before labeling"
    if topic.startswith("cpr"):
        return "Pause compressions for 10 seconds after each breath"
    if topic.startswith("ekg"):
        return "Place V1 on the posterior chest when anterior leads fail"
    return "Use the same technique for pediatric and adult patients"


def _context_shift(correct: str, topic: str, h: int) -> str:
    if "tube" in correct.lower():
        return "Collect lavender EDTA before serum separator when cultures are not ordered"
    if topic.startswith("ekg"):
        return "Interpret limb lead reversal as a normal variant without repeat tracing"
    return _PATIENTS[(h + 1) % len(_PATIENTS)] + " would not change the standard for this finding"


def _rewrite_intermediate(fact: dict) -> dict:
    cpr = _rewrite_cpr_intermediate(fact)
    if cpr:
        return cpr
    correct = fact["correct"]
    ds = list(fact.get("distractors") or [])
    cleaned = [_clean_giveaway_distractor(d, correct) for d in ds]
    if len(cleaned) < 3:
        cleaned.extend(["Related step from a different protocol", "Adjacent value on the guideline chart", "Correct action at the wrong time"])
    near = _numeric_near_miss(correct, stem_hash(fact["stem"]))
    if near:
        cleaned[0] = near
    return {**fact, "distractors": _pick_three(correct, cleaned)}


def _rewrite_beginner(fact: dict) -> dict:
    correct = fact["correct"]
    ds = [_clean_giveaway_distractor(d, correct) for d in fact.get("distractors") or []]
    return {**fact, "distractors": _pick_three(correct, ds)}


def _numeric_near_miss(text: str, salt: int) -> str | None:
    m = re.search(r"(\d+)\s+to\s+(\d+)", text)
    if not m:
        m = re.search(r"(\d+)", text)
        if not m:
            return None
        val = int(m.group(1))
        delta = 10 if val >= 20 else 1
        return text[: m.start()] + str(val + delta) + text[m.end() :]
    a, b = int(m.group(1)), int(m.group(2))
    if salt % 2 == 0:
        return text.replace(m.group(0), f"{a - 10} to {b - 10}", 1)
    return text.replace(m.group(0), f"{a + 10} to {b + 10}", 1)


def polish_distractors(fact: dict) -> dict:
    correct = fact["correct"]
    topic = fact["topic"]
    h = stem_hash(fact["stem"])
    out_ds = []
    for i, d in enumerate(fact.get("distractors") or []):
        text = _clean_giveaway_distractor(str(d), correct)
        if DISTRACTOR_GIVEAWAY_WORDS.search(text) and not DISTRACTOR_GIVEAWAY_WORDS.search(correct):
            text = _partial_truth_from_correct(correct, h + i) or _context_shift(correct, topic, h + i)
        if text.lower() == correct.lower():
            text = _context_shift(correct, topic, h + i)
        out_ds.append(text.strip())
    fact = {**fact, "distractors": _pick_three(correct, out_ds)}
    return fact


def balance_all_chunks(facts: list[dict]) -> None:
    from collections import defaultdict

    from classquiz.seed.catalog import TOPIC_QUESTIONS_PER_QUIZ
    from classquiz.seed.fact_choice_hardening import is_correct_strictly_longest

    quiz_size = 28
    by_key: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for fact in facts:
        by_key[(fact["topic"], fact["difficulty"])].append(fact)
    for items in by_key.values():
        items.sort(key=lambda f: f["stem"])
        chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(items[0]["topic"], quiz_size)
        for start in range(0, len(items), chunk_size):
            chunk = items[start : start + chunk_size]
            allowed = max(1, int(len(chunk) * 0.30 + 0.999))  # ceil
            for _ in range(200):
                longest = [i for i, f in enumerate(chunk) if is_correct_strictly_longest(f)]
                if len(longest) <= allowed:
                    break
                for idx in longest:
                    f = chunk[idx]
                    for _ in range(8):
                        correct, ds = _balance_lengths(f["correct"], f["distractors"])
                        f["correct"] = correct
                        f["distractors"] = ds
                        if not is_correct_strictly_longest(f):
                            break
                        words = f["correct"].split()
                        if len(words) > 4:
                            f["correct"] = " ".join(words[:-1])
                        else:
                            break


def materialize_fact(fact: dict) -> dict:
    difficulty = normalize_difficulty(fact.get("difficulty"))
    if difficulty == "advanced":
        out = _rewrite_advanced(fact)
    elif difficulty == "intermediate":
        out = _rewrite_intermediate(fact)
    else:
        out = _rewrite_beginner(fact)

    correct, distractors = _balance_lengths(out["correct"], out["distractors"])
    expl = out.get("explanation") or fact.get("explanation") or ""
    expl = _explanation(
        correct,
        distractors,
        _dash_to_to(str(expl)),
        f"{correct} matches the exam reference for this topic.",
    )
    return {
        **out,
        "correct": correct,
        "distractors": distractors,
        "explanation": expl,
        "difficulty": difficulty,
    }
