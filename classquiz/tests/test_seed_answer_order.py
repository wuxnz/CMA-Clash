# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest

pytestmark = pytest.mark.order("last")


def test_fact_to_question_shuffles_correct_answer_position():
    from classquiz.seed.runner import _fact_to_question

    fact = {
        "stem": "Seed shuffle test stem unique 001",
        "correct": "Right choice",
        "distractors": ["Wrong A", "Wrong B", "Wrong C"],
    }
    positions = set()
    for _ in range(12):
        q = _fact_to_question(fact)
        for i, ans in enumerate(q.answers):
            if ans.right:
                positions.add(i)
    assert len(positions) > 1, "correct answer should not always be first"
