# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

from typing import Sequence

from classquiz.seed.choice_quality import normalize_abcd_choice_lengths

_BALANCE_TOPIC_PREFIXES = ("ekg-", "cpr-", "phleb-")


def fact(
    topic: str,
    stem: str,
    correct: str,
    distractors: Sequence[str],
    explanation: str,
    references: Sequence[str],
    difficulty: str = "intermediate",
) -> dict:
    if len(distractors) != 3:
        raise ValueError("ABCD questions require exactly three distractors")
    distractor_list = list(distractors)
    if any(topic.startswith(p) for p in _BALANCE_TOPIC_PREFIXES):
        correct, distractor_list = normalize_abcd_choice_lengths(stem, correct, distractor_list)
    return {
        "topic": topic,
        "stem": stem,
        "correct": correct,
        "distractors": distractor_list,
        "explanation": explanation,
        "references": list(references),
        "difficulty": difficulty,
    }
