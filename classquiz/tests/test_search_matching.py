# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Search must reach the certification, the topic and the question text.

A title/description-only index makes whole collections look empty: searching
"EKG" found nothing even though the site is full of EKG question sets.
"""

from __future__ import annotations

import pytest

from classquiz.tests import ValueStorage, test_client  # noqa: F401

pytestmark = pytest.mark.order("last")


@pytest.fixture(scope="module", autouse=True)
def _seeded_database():
    """Seed before the app fixture connects the database in its own event loop."""
    import asyncio

    from classquiz.seed.runner import run_seed

    asyncio.run(run_seed(force=True))


def test_searchable_attributes_cover_topic_and_question_text() -> None:
    from classquiz.helpers import SEARCHABLE_ATTRIBUTES

    for attribute in ("title", "description", "certification", "topic", "stems"):
        assert attribute in SEARCHABLE_ATTRIBUTES


def test_quiz_question_text_joins_every_stem() -> None:
    from classquiz.helpers import quiz_question_text

    class FakeQuiz:
        questions = [
            {"question": "Which leads form the EKG?", "answers": [{"answer": "I, II, V1", "right": True}]},
            {"question": "What is the normal heart rate?", "answers": [{"answer": "60-100", "right": True}]},
        ]

    text = quiz_question_text(FakeQuiz())
    assert "Which leads form the EKG?" in text
    assert "What is the normal heart rate?" in text


def test_search_finds_quiz_by_certification_name(test_client) -> None:
    resp = test_client.get("/api/v1/search/", params={"q": "EKG Technician"})
    assert resp.status_code == 200
    hits = resp.json()["hits"]
    assert hits, "searching a certification name must return hits"


def test_search_finds_quiz_by_question_text(test_client) -> None:
    listing = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1})
    assert listing.status_code == 200
    quizzes = listing.json()
    assert quizzes, "the seeded library must contain public quizzes"
    quiz_id = quizzes[0]["id"]

    quiz = test_client.get(f"/api/v1/quiz/get/public/{quiz_id}")
    assert quiz.status_code == 200
    questions = quiz.json()["questions"]
    assert questions
    words = [word for word in questions[0]["question"].split() if len(word) > 6]
    assert words, "a seeded question must contain a searchable word"

    resp = test_client.get("/api/v1/search/", params={"q": words[0]})
    assert resp.status_code == 200
    hit_ids = [str(hit["id"]) for hit in resp.json()["hits"]]
    assert str(quiz_id) in hit_ids
