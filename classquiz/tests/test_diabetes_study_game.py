# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Every Diabetes Study Guide question can be drawn into a battle or match."""

from __future__ import annotations

from classquiz.helpers.game_questions import select_questions_for_game
from classquiz.seed.banks import load_all_facts
from classquiz.seed.catalog import TOPIC_QUESTIONS_PER_GAME
from classquiz.seed.runner import _fact_to_question

TOPIC = "diabetes-study-guide"


def _facts() -> list[dict]:
    return [f for f in load_all_facts() if f["topic"] == TOPIC]


def test_bank_has_thirty_questions_with_one_correct_answer_each():
    facts = _facts()
    assert len(facts) == 30
    for fact in facts:
        assert len(fact["distractors"]) == 3
        assert fact["correct"] not in fact["distractors"]


def test_game_draw_covers_the_whole_bank():
    facts = _facts()
    draw = TOPIC_QUESTIONS_PER_GAME[TOPIC]
    assert draw == len(facts)
    questions = [_fact_to_question(fact) for fact in facts]
    picked = select_questions_for_game(questions, draw)
    assert len(picked) == len(facts)
    assert {q.question for q in picked} == {fact["stem"] for fact in facts}


def test_each_game_question_has_four_choices_and_one_right_answer():
    for fact in _facts():
        question = _fact_to_question(fact)
        assert len(question.answers) == 4
        right = [answer.answer for answer in question.answers if answer.right]
        assert right == [fact["correct"]]
