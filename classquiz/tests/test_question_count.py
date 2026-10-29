# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""A host can choose how many questions a battle or match uses."""

from __future__ import annotations

import random

import pytest

from classquiz.helpers.game_questions import (
    MIN_QUESTIONS_PER_GAME,
    select_questions_for_game,
    validate_question_count,
)


def test_no_request_keeps_the_quiz_default():
    assert validate_question_count(30, None) is None


def test_count_within_range_is_accepted():
    assert validate_question_count(30, 12) == 12
    assert validate_question_count(30, MIN_QUESTIONS_PER_GAME) == MIN_QUESTIONS_PER_GAME
    assert validate_question_count(30, 30) == 30


@pytest.mark.parametrize("requested", [1, MIN_QUESTIONS_PER_GAME - 1, 31, 500])
def test_count_outside_range_is_rejected(requested):
    with pytest.raises(ValueError):
        validate_question_count(30, requested)


def test_chosen_count_is_the_number_drawn():
    bank = [f"question {i}" for i in range(30)]
    assert len(select_questions_for_game(bank, 12, random.Random(1))) == 12


def test_choosing_the_whole_bank_draws_every_question():
    bank = [f"question {i}" for i in range(30)]
    picked = select_questions_for_game(bank, 30, random.Random(1))
    assert sorted(picked) == sorted(bank)
