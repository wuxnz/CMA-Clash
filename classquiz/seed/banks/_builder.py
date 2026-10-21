# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

from typing import Sequence


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
    return {
        "topic": topic,
        "stem": stem,
        "correct": correct,
        "distractors": list(distractors),
        "explanation": explanation,
        "references": list(references),
        "difficulty": difficulty,
    }
