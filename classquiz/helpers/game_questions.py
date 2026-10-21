# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Select and shuffle questions for a single hosted live game."""

from __future__ import annotations

import random
from typing import Any, Sequence

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
