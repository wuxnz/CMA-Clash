# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Select and shuffle questions for a single hosted live game."""

from __future__ import annotations

import random
from typing import Any, Sequence

from classquiz.db.models import QuizQuestionType

DEFAULT_QUESTIONS_PER_GAME = 10
MIN_QUESTIONS_PER_GAME = 8


def resolve_questions_per_game(bank_size: int, configured: int | None) -> int:
    """Return how many questions to draw for one hosted game."""
    if bank_size <= 0:
        return 0
    if configured is None:
        configured = DEFAULT_QUESTIONS_PER_GAME
    draw = max(MIN_QUESTIONS_PER_GAME, configured)
    return min(draw, bank_size)


def validate_question_count(bank_size: int, requested: int | None) -> int | None:
    """Return the requested question count if a game can use it, else raise ValueError.

    A host may pick any count from MIN_QUESTIONS_PER_GAME up to the size of the quiz bank.
    """
    if requested is None:
        return None
    if requested < MIN_QUESTIONS_PER_GAME or requested > bank_size:
        raise ValueError(f"question_count must be between {MIN_QUESTIONS_PER_GAME} and {bank_size}")
    return requested


def select_questions_for_game(
    questions: Sequence[Any],
    questions_per_game: int | None = None,
    rng: random.Random | None = None,
) -> list[Any]:
    """
    Random sample without replacement, then shuffle order.
    If the bank is smaller than the configured draw, use every question.
    """
    bank = list(questions)
    if not bank:
        return []
    draw = resolve_questions_per_game(len(bank), questions_per_game)
    picker = rng or random.Random()
    if draw >= len(bank):
        selected = list(bank)
    else:
        selected = picker.sample(bank, draw)
    picker.shuffle(selected)
    return selected


def _abcd_type(question: Any) -> bool:
    qtype = question.get("type") if isinstance(question, dict) else getattr(question, "type", None)
    return qtype in (QuizQuestionType.ABCD, "ABCD")


def shuffle_abcd_answer_positions(
    questions: Sequence[Any],
    rng: random.Random | None = None,
) -> None:
    """Shuffle ABCD option order once per game session (live, battle, hosted)."""
    picker = rng or random.Random()
    for question in questions:
        if not _abcd_type(question):
            continue
        answers = question["answers"] if isinstance(question, dict) else question.answers
        picker.shuffle(answers)
