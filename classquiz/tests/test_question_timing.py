# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import uuid

from classquiz.db.models import PlayGame, QuizQuestion, QuizQuestionType
from classquiz.socket_server.timing import INTRO_MS, build_question_timing, is_kahoot_style


def test_kahoot_has_no_intro_gap() -> None:
    game = PlayGame(
        quiz_id=uuid.uuid4(),
        description="d",
        user_id=uuid.uuid4(),
        title="t",
        questions=[
            QuizQuestion(
                question="q",
                answers=[{"answer": "a", "right": True}],
                type=QuizQuestionType.ABCD,
                time="20",
            )
        ],
        game_id=uuid.uuid4(),
        game_pin="123456",
        game_mode="kahoot",
    )
    t = build_question_timing(game, 0, now_ms=1_000_000)
    assert t["intro_deadline_ms"] == t["question_start_ms"]
    assert t["answer_deadline_ms"] == t["answer_phase_start_ms"] + 20_000


def test_normal_has_intro() -> None:
    game = PlayGame(
        quiz_id=uuid.uuid4(),
        description="d",
        user_id=uuid.uuid4(),
        title="t",
        questions=[
            QuizQuestion(
                question="q",
                answers=[{"answer": "a", "right": True}],
                type=QuizQuestionType.ABCD,
                time="10",
            )
        ],
        game_id=uuid.uuid4(),
        game_pin="123456",
        game_mode="normal",
    )
    t = build_question_timing(game, 0, now_ms=0)
    assert t["intro_deadline_ms"] - t["question_start_ms"] == INTRO_MS
    assert is_kahoot_style("normal") is False
