# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


import json
from datetime import datetime

from classquiz.config import redis
from classquiz.db.models import PlayGame, GameResults


async def save_quiz_to_storage(game_pin: str):
    game = PlayGame.model_validate_json(await redis.get(f"game:{game_pin}"))
    player_count = await redis.scard(f"game_session:{game_pin}:players")
    answers = []
    for i in range(len(game.questions)):
        redis_res = await redis.lrange(f"game_session:{game_pin}:{i}", 0, -1)
        answers.append([json.loads(a) for a in redis_res])
    player_scores = await redis.hgetall(f"game_session:{game_pin}:player_scores")
    custom_field_data = await redis.hgetall(f"game:{game_pin}:players:custom_fields")
    q_return = []
    for q in game.questions:
        q_return.append(q.model_dump())
    data = GameResults(
        id=game.game_id,
        quiz=game.quiz_id,
        user=game.user_id,
        timestamp=datetime.now(),
        player_count=player_count,
        answers=json.dumps(answers),
        player_scores=json.dumps(player_scores),
        custom_field_data=json.dumps(custom_field_data),
        title=game.title,
        description=game.description,
        questions=json.dumps(q_return),
    )
    await data.save()
    from classquiz.db.cma_models import XpSource
    from classquiz.gamification.service import award_xp
    from classquiz.db.models import Quiz as QuizModel

    quiz_row = await QuizModel.objects.get_or_none(id=game.quiz_id)
    base_xp = 25 + min(player_count * 5, 50)
    await award_xp(
        game.user_id,
        base_xp,
        XpSource.QUIZ_PLAY,
        certification_id=quiz_row.certification_id if quiz_row else None,
        topic_id=quiz_row.topic_id if quiz_row else None,
        note=f"hosted-game:{game.game_id}",
    )
    if game.game_mode == "battle":
        from classquiz.socket_server.battle_hooks import finalize_battle

        await finalize_battle(game_pin, game)
