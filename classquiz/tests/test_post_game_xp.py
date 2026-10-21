# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import json
import uuid

import pytest

from classquiz.config import redis
from classquiz.db.cma_models import UserGamificationProfile
from classquiz.db.models import PlayGame, User
from classquiz.gamification.post_game import award_game_xp_once
from classquiz.tests import test_user_email

pytestmark = pytest.mark.order("last")


@pytest.mark.asyncio
async def test_award_game_xp_once_is_idempotent():
    user = await User.objects.get_or_none(email=test_user_email)
    assert user is not None
    game_pin = "999001"
    game_id = uuid.uuid4()
    quiz_id = uuid.uuid4()
    game = PlayGame(
        quiz_id=quiz_id,
        game_pin=game_pin,
        questions=[{"type": "ABCD", "answers": [], "time": "30"}],
        game_id=game_id,
        title="Test",
        description="",
        captcha_enabled=False,
        cover_image=None,
        game_mode="kahoot",
        user_id=user.id,
    )
    await redis.set(f"game:{game_pin}", game.model_dump_json(), ex=60)
    await redis.sadd(f"game_session:{game_pin}:players", json.dumps({"username": "p1", "sid": "s1"}))
    await redis.rpush(
        f"game_session:{game_pin}:0",
        json.dumps({"username": user.username, "right": True, "answer": "a", "time_taken": 1, "score": 100}),
    )
    profile_before = await UserGamificationProfile.objects.get_or_none(user_id=user.id)
    xp_before = profile_before.total_xp if profile_before else 0

    await award_game_xp_once(game_pin, game, None)
    await award_game_xp_once(game_pin, game, None)

    profile_after = await UserGamificationProfile.objects.get_or_none(user_id=user.id)
    assert profile_after is not None
    assert profile_after.total_xp > xp_before

    await redis.delete(f"game:{game_pin}")
    await redis.delete(f"game_session:{game_pin}:players")
    await redis.delete(f"game_session:{game_pin}:0")
    await redis.delete(f"gamification:awarded:{game_pin}")
