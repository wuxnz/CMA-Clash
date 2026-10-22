# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest

pytestmark = pytest.mark.order("last")


def test_fact_to_question_shuffles_correct_answer_position():
    """The keyed answer must not always land in the same slot.

    The seeder derives its shuffle seed from the question stem, so one stem always
    produces one layout. Sample several stems to cover the real distribution.
    """
    from classquiz.seed.runner import _fact_to_question

    positions = set()
    for index in range(24):
        fact = {
            "stem": f"Seed shuffle test stem unique {index:03d}",
            "correct": "Right choice",
            "distractors": ["Wrong A", "Wrong B", "Wrong C"],
        }
        question = _fact_to_question(fact)
        for i, answer in enumerate(question.answers):
            if answer.right:
                positions.add(i)
    assert len(positions) > 1, "correct answer should not always be in the same position"
    assert positions == {0, 1, 2, 3}, "correct answer should reach every option slot"


def test_fact_to_question_shuffle_is_stable_for_one_stem():
    """The same stem must always seed the same layout, so reseeding is idempotent."""
    from classquiz.seed.runner import _fact_to_question

    fact = {
        "stem": "Seed shuffle test stem stable 001",
        "correct": "Right choice",
        "distractors": ["Wrong A", "Wrong B", "Wrong C"],
    }
    layouts = []
    for _ in range(3):
        question = _fact_to_question(fact)
        layouts.append([a.answer for a in question.answers])
    assert layouts[0] == layouts[1] == layouts[2]
