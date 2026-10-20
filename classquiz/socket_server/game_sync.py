# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Server-driven live game start and question sync (battles + hosted quizzes)."""

from __future__ import annotations

import asyncio
import json
import random
from datetime import datetime

from classquiz.config import redis
from classquiz.db.models import PlayGame, QuizQuestionType, VotingQuizAnswer
from classquiz.socket_server.models import ReturnQuestion

INTRO_GRACE_SEC = 4

_battle_timer_tasks: dict[str, asyncio.Task] = {}


def _cancel_battle_timer(game_pin: str) -> None:
    task = _battle_timer_tasks.pop(game_pin, None)
    if task is not None and not task.done():
        task.cancel()


async def _prepare_question_payload(game_data: PlayGame, question_index: int) -> dict:
    temp_return = game_data.model_dump(include={"questions"})["questions"][question_index]
    q_type = game_data.questions[question_index].type
    if q_type == QuizQuestionType.VOTING:
        for i in range(len(temp_return["answers"])):
            temp_return["answers"][i] = VotingQuizAnswer(**temp_return["answers"][i])
    temp_return["type"] = q_type
    if temp_return["type"] == QuizQuestionType.ORDER:
        random.shuffle(temp_return["answers"])
    started_at = datetime.now().isoformat()
    payload: dict = {
        "question_index": question_index,
        "question_started_at": started_at,
    }
    if q_type != QuizQuestionType.SLIDE:
        payload["question"] = ReturnQuestion(**temp_return).model_dump()
    return payload


async def emit_show_question(sio, game_pin: str, game_data: PlayGame, question_index: int, room: str | None = None) -> None:
    """Show a question to everyone in the game room (or a single sid when room is a sid)."""
    game_data.current_question = question_index
    game_data.question_show = True
    await game_data.save(game_pin)
    started_at = datetime.now().isoformat()
    await redis.set(f"game:{game_pin}:current_time", started_at, ex=7200)
    payload = await _prepare_question_payload(game_data, question_index)
    target = room or game_pin
    await sio.emit("set_question_number", payload, room=target)
    if game_data.game_mode == "battle":
        _schedule_battle_question_timeout(sio, game_pin, question_index)


def _schedule_battle_question_timeout(sio, game_pin: str, question_index: int) -> None:
    _cancel_battle_timer(game_pin)

    async def _run() -> None:
        try:
            game_data = await PlayGame.get_from_redis(game_pin)
            if game_data.current_question != question_index:
                return
            q_time = int(float(game_data.questions[question_index].time))
            await asyncio.sleep(INTRO_GRACE_SEC + max(1, q_time))
            game_data = await PlayGame.get_from_redis(game_pin)
            if game_data.current_question != question_index:
                return
            if not game_data.question_show:
                return
            game_data.question_show = False
            await game_data.save(game_pin)
            await sio.emit("everyone_answered", room=game_pin)
            await battle_maybe_advance(sio, game_pin, game_data)
        except asyncio.CancelledError:
            return

    _battle_timer_tasks[game_pin] = asyncio.create_task(_run())


async def start_live_game(sio, game_pin: str, show_first_question: bool = True) -> PlayGame:
    """Mark game started and optionally show question 0 to the room."""
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.started and game_data.current_question >= 0:
        return game_data
    game_data.started = True
    await game_data.save(game_pin)
    await redis.delete(f"game_in_lobby:{game_data.user_id.hex}")
    await sio.emit("start_game", room=game_pin)
    if show_first_question and game_data.questions:
        await emit_show_question(sio, game_pin, game_data, 0)
    return game_data


async def sync_player_to_live_game(sio, sid: str, game_pin: str, game_data: PlayGame) -> None:
    """Catch up a player who joined after the host started (battle late join)."""
    if not game_data.started:
        return
    if game_data.current_question < 0:
        await sio.emit("start_game", room=sid)
        return
    await sio.emit("start_game", room=sid)
    if game_data.question_show and game_data.current_question >= 0:
        payload = await _prepare_question_payload(game_data, game_data.current_question)
        started = await redis.get(f"game:{game_pin}:current_time")
        if started:
            payload["question_started_at"] = started
        await sio.emit("set_question_number", payload, room=sid)


async def try_kickoff_battle(sio, game_pin: str) -> None:
    """Start the live battle (question 0) once — after roster sync or max wait."""
    from classquiz.battle.service import BATTLE_REDIS_PREFIX

    kickoff_key = f"{BATTLE_REDIS_PREFIX}:kickoff:{game_pin}"
    raw = await redis.get(kickoff_key)
    if raw:
        data = json.loads(raw)
        if data.get("kicked_off"):
            return
        data["kicked_off"] = True
        await redis.set(kickoff_key, json.dumps(data), ex=18000)
    await start_live_game(sio, game_pin, show_first_question=True)


async def begin_battle_from_rest(sio, game_pin: str) -> None:
    """Called when a battle lobby starts via REST — wait for players before question 0."""
    from classquiz.socket_server.battle_sync import schedule_battle_kickoff

    await schedule_battle_kickoff(sio, game_pin)


async def battle_maybe_advance(sio, game_pin: str, game_data: PlayGame) -> None:
    _cancel_battle_timer(game_pin)
    next_q = game_data.current_question + 1
    if next_q >= len(game_data.questions):
        from classquiz.socket_server import generate_final_results
        from classquiz.socket_server.battle_hooks import finalize_battle

        results = await generate_final_results(game_data, game_pin)
        await sio.emit("final_results", results, room=game_pin)
        await sio.emit("battle_finished", room=game_pin)
        await finalize_battle(game_pin, game_data)
        return
    refreshed = await PlayGame.get_from_redis(game_pin)
    await emit_show_question(sio, game_pin, refreshed, next_q)
