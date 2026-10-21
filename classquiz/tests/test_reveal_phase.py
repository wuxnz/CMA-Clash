# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.db.models import ABCDQuizAnswer, QuizQuestion, QuizQuestionType
from classquiz.helpers.reveal_phase import compute_reveal_hold_sec, correct_answer_label, count_words


def test_count_words() -> None:
    assert count_words("") == 0
    assert count_words("one two three") == 3


def test_compute_reveal_hold_sec_bounds() -> None:
    assert compute_reveal_hold_sec(None) == 8.0
    assert compute_reveal_hold_sec("") == 8.0
    short = " ".join(["word"] * 14)
    assert compute_reveal_hold_sec(short) == 8.0
    assert compute_reveal_hold_sec(" ".join(["word"] * 15)) == 9.0
    long_text = " ".join(["word"] * 200)
    assert compute_reveal_hold_sec(long_text) == 20.0


def test_correct_answer_label_abcd() -> None:
    q = QuizQuestion(
        question="Stem",
        time="30",
        type=QuizQuestionType.ABCD,
        answers=[
            ABCDQuizAnswer(answer="Yes", right=True, color="#0f0"),
            ABCDQuizAnswer(answer="No", right=False, color="#f00"),
        ],
    )
    assert correct_answer_label(q) == "Yes"
