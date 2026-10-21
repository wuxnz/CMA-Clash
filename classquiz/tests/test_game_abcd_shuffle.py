# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import random

import pytest

from classquiz.db.models import QuizQuestionType
from classquiz.helpers.game_questions import shuffle_abcd_answer_positions

pytestmark = pytest.mark.order("last")


def test_shuffle_abcd_answer_positions_changes_order():
    questions = [
        {
            "type": QuizQuestionType.ABCD,
            "answers": [
                {"answer": "Right", "right": True},
                {"answer": "Wrong 1", "right": False},
                {"answer": "Wrong 2", "right": False},
                {"answer": "Wrong 3", "right": False},
            ],
        }
    ]
    positions = set()
    for _ in range(20):
        q = [dict(questions[0])]
        q[0]["answers"] = [dict(a) for a in questions[0]["answers"]]
        shuffle_abcd_answer_positions(q, rng=random.Random())
        for i, ans in enumerate(q[0]["answers"]):
            if ans["right"]:
                positions.add(i)
    assert len(positions) > 1
