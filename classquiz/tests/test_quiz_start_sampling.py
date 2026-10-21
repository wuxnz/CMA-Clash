# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import json
import uuid

import pytest
from fastapi.testclient import TestClient

from classquiz.db.models import Quiz, QuizQuestion, QuizQuestionType, ABCDQuizAnswer, User
from classquiz.tests import ValueStorage, test_user_email

pytestmark = pytest.mark.order("last")


@pytest.mark.asyncio
async def test_start_quiz_samples_questions_into_redis_game(test_client: TestClient):
    from classquiz.auth import get_password_hash
    from classquiz.config import redis
    from classquiz.helpers.avatar import gzipped_user_avatar
    from classquiz.tests.test_server import TestUsers

    TestUsers.log_in(test_client)
    user = await User.objects.get_or_none(email=test_user_email)
    if user is None:
        user = await User(
            email=test_user_email,
            username="sample_host",
            password=get_password_hash("test"),
            verified=True,
            verify_key=None,
            require_password=True,
            avatar=gzipped_user_avatar(),
        ).save()

    bank = []
    for i in range(20):
        bank.append(
            QuizQuestion(
                question=f"Stem {i}",
                time="30",
                type=QuizQuestionType.ABCD,
                answers=[
                    ABCDQuizAnswer(right=True, answer="A"),
                    ABCDQuizAnswer(right=False, answer="B"),
                    ABCDQuizAnswer(right=False, answer="C"),
                    ABCDQuizAnswer(right=False, answer="D"),
                ],
            )
        )
    quiz = await Quiz(
        id=uuid.uuid4(),
        public=False,
        title="Sampling test quiz",
        description="",
        user_id=user.id,
        questions=[q.model_dump() for q in bank],
        questions_per_game=10,
    ).save()

    resp = test_client.post(
        f"/api/v1/quiz/start/{quiz.id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert resp.status_code == 200
    data = resp.json()
    pin = data["game_pin"]
    raw = await redis.get(f"game:{pin}")
    assert raw is not None
    game = json.loads(raw)
    assert len(game["questions"]) == 10
    stems = {q["question"] for q in game["questions"]}
    assert len(stems) == 10
