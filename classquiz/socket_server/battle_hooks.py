# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import json
import uuid

from classquiz.battle.service import BATTLE_REDIS_PREFIX
from classquiz.config import redis
from classquiz.db.models import PlayGame, Quiz
from classquiz.gamification.service import record_battle_result


async def finalize_battle(game_pin: str, game_data: PlayGame) -> None:
    if await redis.get(f"{BATTLE_REDIS_PREFIX}:done:{game_pin}") is not None:
        return
    meta_raw = await redis.get(f"{BATTLE_REDIS_PREFIX}:meta:{game_pin}")
    if meta_raw is None:
        return
    await redis.set(f"{BATTLE_REDIS_PREFIX}:done:{game_pin}", "1", ex=18000)
    meta = json.loads(meta_raw)
    scores_raw = await redis.hgetall(f"game_session:{game_pin}:player_scores")
    scores = {k: int(v) for k, v in scores_raw.items()}
    user_ids = {k: uuid.UUID(v) for k, v in meta.get("player_user_ids", {}).items()}
    await record_battle_result(
        quiz_id=uuid.UUID(str(game_data.quiz_id)),
        game_id=game_data.game_id,
        scores=scores,
        user_ids=user_ids,
    )
    quiz = await Quiz.objects.get_or_none(id=game_data.quiz_id)
    cert_id = quiz.certification_id if quiz else None
    topic_id = quiz.topic_id if quiz else None
    from classquiz.gamification.service import record_answer_stats

    for q_index in range(len(game_data.questions)):
        redis_res = await redis.lrange(f"game_session:{game_pin}:{q_index}", 0, -1)
        for raw in redis_res:
            row = json.loads(raw)
            uid = user_ids.get(row["username"])
            if uid is None:
                continue
            await record_answer_stats(uid, topic_id, row.get("right", False), cert_id)
