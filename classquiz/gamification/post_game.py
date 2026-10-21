# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Award XP once when a hosted game reaches final results (live or battle)."""

from __future__ import annotations

import json
import uuid

from classquiz.config import redis
from classquiz.db.cma_models import XpSource
from classquiz.db.models import PlayGame, Quiz as QuizModel, User
from classquiz.gamification.service import award_xp, record_answer_stats

_AWARD_KEY_PREFIX = "gamification:awarded:"


async def _already_awarded(game_pin: str) -> bool:
    return await redis.get(f"{_AWARD_KEY_PREFIX}{game_pin}") is not None


async def _mark_awarded(game_pin: str) -> None:
    await redis.set(f"{_AWARD_KEY_PREFIX}{game_pin}", "1", ex=86400)


async def award_game_xp_once(game_pin: str, game_data: PlayGame, results: dict | None = None) -> None:
    """Idempotent XP for game completion. Skips battle mode (finalize_battle handles battles)."""
    if game_data.game_mode == "battle":
        return
    if await _already_awarded(game_pin):
        return
    await _mark_awarded(game_pin)

    quiz_row = await QuizModel.objects.get_or_none(id=game_data.quiz_id)
    cert_id = quiz_row.certification_id if quiz_row else None
    topic_id = quiz_row.topic_id if quiz_row else None

    player_count = await redis.scard(f"game_session:{game_pin}:players")
    base_xp = 25 + min(int(player_count or 0) * 5, 50)
    host_id = game_data.user_id
    if await User.objects.get_or_none(id=host_id) is not None:
        await award_xp(
            host_id,
            base_xp,
            XpSource.QUIZ_PLAY,
            certification_id=cert_id,
            topic_id=topic_id,
            note=f"hosted-game:{game_data.game_id}",
        )

    if results is None:
        results = {}
        for i in range(len(game_data.questions)):
            redis_res = await redis.lrange(f"game_session:{game_pin}:{i}", 0, -1)
            if redis_res:
                results[str(i)] = [json.loads(a) for a in redis_res]

    for answers in results.values():
        if not isinstance(answers, list):
            continue
        for row in answers:
            username = row.get("username")
            if not username:
                continue
            user = await User.objects.get_or_none(username=username)
            if user is None:
                continue
            await record_answer_stats(
                user.id,
                topic_id,
                bool(row.get("right", False)),
                certification_id=cert_id,
            )


async def award_host_from_saved_game(game_pin: str, game: PlayGame, player_count: int) -> None:
    """Legacy path when results are saved manually; no-op if game completion already awarded."""
    if await _already_awarded(game_pin):
        return
    await _mark_awarded(game_pin)
    quiz_row = await QuizModel.objects.get_or_none(id=game.quiz_id)
    base_xp = 25 + min(player_count * 5, 50)
    if await User.objects.get_or_none(id=game.user_id) is not None:
        await award_xp(
            game.user_id,
            base_xp,
            XpSource.QUIZ_PLAY,
            certification_id=quiz_row.certification_id if quiz_row else None,
            topic_id=quiz_row.topic_id if quiz_row else None,
            note=f"hosted-game:{game.game_id}",
        )
