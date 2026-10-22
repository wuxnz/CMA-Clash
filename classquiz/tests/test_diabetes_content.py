# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.seed.banks import load_all_facts
from classquiz.seed.catalog import TOPIC_QUESTIONS_PER_QUIZ
from classquiz.seed.runner import QUESTIONS_PER_QUIZ


def _facts_for(topic: str):
    return [f for f in load_all_facts() if f["topic"] == topic]


def test_diabetes_topic_question_count():
    facts = _facts_for("ccma-diabetes")
    assert len(facts) == 130


def test_diabetes_quiz_set_chunks():
    facts = _facts_for("ccma-diabetes")
    chunk = TOPIC_QUESTIONS_PER_QUIZ.get("ccma-diabetes", QUESTIONS_PER_QUIZ)
    assert chunk == 28
    # The topic must supply at least four full 28-question sets. The seeded runner
    # chunks per difficulty, so a short final chunk is expected and is not an error.
    assert len(facts) >= 4 * chunk
    assert len(facts) // chunk == 4


def test_phleb_glucose_topic_meets_minimum():
    facts = _facts_for("phleb-glucose")
    assert len(facts) >= 28


def test_diabetes_unique_stems():
    facts = _facts_for("ccma-diabetes")
    stems = [f["stem"] for f in facts]
    assert len(stems) == len(set(stems))


def test_diabetes_one_correct_answer_per_question():
    for fact in _facts_for("ccma-diabetes") + _facts_for("phleb-glucose"):
        assert fact["correct"]
        assert len(fact["distractors"]) == 3
        assert fact["correct"] not in fact["distractors"]


def test_diabetes_quiz_titles_unique():
    topic_name = "Diabetes"
    chunk = TOPIC_QUESTIONS_PER_QUIZ["ccma-diabetes"]
    count = len(_facts_for("ccma-diabetes"))
    titles = [f"{topic_name}: Set {i + 1}" for i in range(count // chunk)]
    assert titles == [
        "Diabetes: Set 1",
        "Diabetes: Set 2",
        "Diabetes: Set 3",
        "Diabetes: Set 4",
    ]
    assert len(titles) == len(set(titles))