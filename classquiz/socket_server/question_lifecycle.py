# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Auto-close questions at deadline, score non-responders, and advance hosted games."""

from __future__ import annotations

import asyncio

from classquiz.config import redis
from classquiz.db.models import AnswerData, AnswerDataList, GamePlayer, PlayGame
from classquiz.socket_server.helpers import has_already_answered
from classquiz.socket_server.timing import load_question_timing, server_now_ms

REVEAL_SEC = 5.0

_lifecycle_tasks: dict[str, asyncio.Task] = {}
_advance_tasks: dict[str, asyncio.Task] = {}


def cancel_question_lifecycle(game_pin: str) -> None:
    for bucket in (_lifecycle_tasks, _advance_tasks):
        task = bucket.pop(game_pin, None)
        if task is not None and not task.done():
            task.cancel()


async def record_non_answers_as_wrong(game_pin: str, question_index: int) -> None:
    from classquiz.socket_server import set_answer

    players = await redis.smembers(f"game_session:{game_pin}:players")
    for raw in players:
        player = GamePlayer.model_validate_json(raw)
        if not player.username:
            continue
        if await has_already_answered(game_pin, question_index, player.username):
            continue
        data = AnswerData(
            username=player.username,
            answer="",
            right=False,
            time_taken=0,
            score=0,
        )
        await set_answer(game_pin=game_pin, q_index=question_index, data=data)


async def broadcast_question_results(sio, game_pin: str, question_index: int) -> AnswerDataList:
    answer_data_list = await AnswerDataList.get_redis_or_empty(game_pin, question_index)
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.question_show:
        game_data.question_show = False
        await game_data.save(game_pin)
    await sio.emit("question_times_up", {"question_index": question_index}, room=game_pin)
    await sio.emit(
        "question_results",
        {"question_index": question_index, "results": answer_data_list.model_dump()},
        room=game_pin,
    )
    return answer_data_list


async def _advance_after_reveal(sio, game_pin: str, question_index: int) -> None:
    try:
        await asyncio.sleep(REVEAL_SEC)
        game_data = await PlayGame.get_from_redis(game_pin)
        if game_data.current_question != question_index:
            return
        if game_data.game_mode == "battle":
            from classquiz.socket_server.game_sync import battle_maybe_advance

            await battle_maybe_advance(sio, game_pin, game_data)
            return
        next_q = question_index + 1
        if next_q >= len(game_data.questions):
            from classquiz.socket_server import generate_final_results

            results = await generate_final_results(game_data, game_pin)
            await sio.emit("final_results", results, room=game_pin)
            return
        from classquiz.socket_server.game_sync import emit_show_question

        refreshed = await PlayGame.get_from_redis(game_pin)
        await emit_show_question(sio, game_pin, refreshed, next_q)
    except asyncio.CancelledError:
        return


def _schedule_advance(sio, game_pin: str, question_index: int) -> None:
    prev = _advance_tasks.pop(game_pin, None)
    if prev is not None and not prev.done():
        prev.cancel()
    _advance_tasks[game_pin] = asyncio.create_task(_advance_after_reveal(sio, game_pin, question_index))


async def close_question_now(sio, game_pin: str, question_index: int) -> bool:
    """Finalize a question once. Returns False if it was already closed."""
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.current_question != question_index:
        return False
    if not game_data.question_show:
        return False
    cancel_question_lifecycle(game_pin)
    await record_non_answers_as_wrong(game_pin, question_index)
    await broadcast_question_results(sio, game_pin, question_index)
    _schedule_advance(sio, game_pin, question_index)
    return True


def schedule_question_deadline(sio, game_pin: str, question_index: int, answer_deadline_ms: int) -> None:
    cancel_question_lifecycle(game_pin)

    async def _run() -> None:
        try:
            wait_sec = max(0, (answer_deadline_ms - server_now_ms()) / 1000)
            await asyncio.sleep(wait_sec)
            await close_question_now(sio, game_pin, question_index)
        except asyncio.CancelledError:
            return

    _lifecycle_tasks[game_pin] = asyncio.create_task(_run())


async def try_close_question_when_complete(sio, game_pin: str, question_index: int) -> None:
    """When every connected player has answered, close immediately."""
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.current_question != question_index or not game_data.question_show:
        return
    if game_data.game_mode == "battle":
        return
    await close_question_now(sio, game_pin, question_index)
