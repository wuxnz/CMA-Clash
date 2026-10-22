# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Difficulty assignment and validation helpers for seed facts (no choice rewriting)."""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict

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

DISTRACTOR_GIVEAWAY_WORDS = re.compile(
    # "only" inside a hyphenated compound (compression-only) is a technical term,
    # not an absolute, so it must not trip the giveaway check.
    r"\b(always|never|any|random)\b|(?<![\w-])only(?![\w-])",
    re.IGNORECASE,
)


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


def stem_hash(stem: str) -> int:
    return int(hashlib.sha256(normalize_stem(stem).encode("utf-8")).hexdigest()[:12], 16)


def is_correct_strictly_longest(fact: dict) -> bool:
    correct = fact["correct"]
    distractors = fact.get("distractors") or []
    if not distractors:
        return False
    max_d = max(len(d) for d in distractors)
    if len(correct) <= max_d:
        return False
    return len(correct) - min(len(correct), min(len(d) for d in distractors)) >= 22


def distractor_has_giveaway_word(distractor: str, correct: str) -> bool:
    if not DISTRACTOR_GIVEAWAY_WORDS.search(distractor):
        return False
    return not DISTRACTOR_GIVEAWAY_WORDS.search(correct)


def assign_difficulties(facts: list[dict]) -> list[dict]:
    assign_difficulties_by_topic(facts)
    return facts
