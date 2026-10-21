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
from classquiz.socket_server.timing import (
    build_question_timing,
    load_question_timing,
    save_question_timing,
    server_now_ms,
)

INTRO_GRACE_SEC = 3.5

_battle_timer_tasks: dict[str, asyncio.Task] = {}


def _cancel_battle_timer(game_pin: str) -> None:
    task = _battle_timer_tasks.pop(game_pin, None)
    if task is not None and not task.done():
        task.cancel()


async def _prepare_question_payload(
    game_data: PlayGame,
    question_index: int,
    existing_timing: dict | None = None,
) -> dict:
    temp_return = game_data.model_dump(include={"questions"})["questions"][question_index]
    q_type = game_data.questions[question_index].type
    if q_type == QuizQuestionType.VOTING:
        for i in range(len(temp_return["answers"])):
            temp_return["answers"][i] = VotingQuizAnswer(**temp_return["answers"][i])
    temp_return["type"] = q_type
    if temp_return["type"] == QuizQuestionType.ORDER:
        random.shuffle(temp_return["answers"])
    timing = existing_timing if existing_timing is not None else build_question_timing(game_data, question_index)
    answer_phase_start = datetime.fromtimestamp(timing["answer_phase_start_ms"] / 1000)
    payload: dict = {
        "question_index": question_index,
        "question_started_at": datetime.fromtimestamp(timing["question_start_ms"] / 1000).isoformat(),
        **timing,
        "server_time_ms": server_now_ms(),
    }
    if q_type != QuizQuestionType.SLIDE:
        payload["question"] = ReturnQuestion(**temp_return).model_dump()
    if existing_timing is None:
        await save_question_timing(game_data.game_pin, timing)
        payload["_answer_phase_iso"] = answer_phase_start.isoformat()
    return payload


async def emit_show_question(sio, game_pin: str, game_data: PlayGame, question_index: int, room: str | None = None) -> None:
    """Show a question to everyone in the game room (or a single sid when room is a sid)."""
    from classquiz.socket_server.question_lifecycle import cancel_question_lifecycle

    cancel_question_lifecycle(game_pin)
    game_data.current_question = question_index
    game_data.question_show = True
    await game_data.save(game_pin)
    payload = await _prepare_question_payload(game_data, question_index)
    await redis.set(f"game:{game_pin}:current_time", payload.pop("_answer_phase_iso"), ex=7200)
    target = room or game_pin
    await sio.emit("set_question_number", payload, room=target)
    timing = await load_question_timing(game_pin)
    if game_data.game_mode == "battle":
        _schedule_battle_question_timeout(sio, game_pin, question_index)
    elif timing and timing.get("question_index") == question_index:
        from classquiz.socket_server.question_lifecycle import schedule_question_deadline

        schedule_question_deadline(sio, game_pin, question_index, timing["answer_deadline_ms"])


def _schedule_battle_question_timeout(sio, game_pin: str, question_index: int) -> None:
    _cancel_battle_timer(game_pin)

    async def _run() -> None:
        try:
            game_data = await PlayGame.get_from_redis(game_pin)
            if game_data.current_question != question_index:
                return
            timing = await load_question_timing(game_pin)
            if timing and timing.get("question_index") == question_index:
                wait_ms = max(0, timing["answer_deadline_ms"] - server_now_ms())
                await asyncio.sleep(wait_ms / 1000)
            else:
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
        timing = await load_question_timing(game_pin)
        if timing and timing.get("question_index") != game_data.current_question:
            timing = None
        payload = await _prepare_question_payload(
            game_data, game_data.current_question, existing_timing=timing
        )
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
