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

LIVE_SCOREBOARD_HOLD_SEC = 9.0


def live_post_question_hold_sec(reveal_hold_sec: float) -> float:
    """Server sleep after question_results before auto-advance (reveal + scoreboard)."""
    return reveal_hold_sec + LIVE_SCOREBOARD_HOLD_SEC

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


async def build_question_results_payload(game_pin: str, question_index: int) -> tuple[dict, AnswerDataList]:
    """Build the live question_results socket payload (standings + enriched rows)."""
    from classquiz.helpers.live_scoring import (
        assign_speed_ranks,
        build_standings,
        merge_standings_into_results,
        standings_top_n,
    )

    game_data = await PlayGame.get_from_redis(game_pin)
    question = game_data.questions[question_index]
    from classquiz.helpers.reveal_phase import compute_reveal_hold_sec, correct_answer_label

    explanation = question.explanation
    reveal_hold_sec = compute_reveal_hold_sec(explanation)
    correct_answer = correct_answer_label(question)

    answer_data_list = await AnswerDataList.get_redis_or_empty(game_pin, question_index)
    raw_scores = await redis.hgetall(f"game_session:{game_pin}:player_scores")
    player_scores = {k: int(v) for k, v in raw_scores.items()}
    result_dicts = [a.model_dump() for a in answer_data_list]
    assign_speed_ranks(result_dicts)
    standings = build_standings(player_scores)
    enriched = merge_standings_into_results(result_dicts, standings)
    for row, model in zip(enriched, answer_data_list.root, strict=True):
        model.speed_rank = row.get("speed_rank")
        model.overall_rank = row.get("overall_rank")
        model.points_behind_above = row.get("points_behind_above")
        model.player_above = row.get("player_above")
        model.points_ahead_of_next = row.get("points_ahead_of_next")
    payload = {
        "question_index": question_index,
        "reveal_hold_sec": reveal_hold_sec,
        "scoreboard_hold_sec": LIVE_SCOREBOARD_HOLD_SEC,
        "standings_top": standings_top_n(standings, 5),
        "results": enriched,
        "explanation": explanation,
        "correct_answer": correct_answer,
    }
    return payload, answer_data_list


async def broadcast_question_results(sio, game_pin: str, question_index: int) -> tuple[AnswerDataList, dict]:
    payload, answer_data_list = await build_question_results_payload(game_pin, question_index)
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.question_show:
        game_data.question_show = False
        await game_data.save(game_pin)
    await sio.emit("question_times_up", {"question_index": question_index}, room=game_pin)
    await sio.emit("question_results", payload, room=game_pin)
    return answer_data_list, payload


async def _advance_after_reveal(
    sio,
    game_pin: str,
    question_index: int,
    reveal_hold_sec: float,
    scoreboard_hold_sec: float,
) -> None:
    try:
        await asyncio.sleep(reveal_hold_sec + scoreboard_hold_sec)
        game_data = await PlayGame.get_from_redis(game_pin)
        if game_data.current_question != question_index:
            return
        if game_data.game_mode == "battle":
            next_q = question_index + 1
            if next_q >= len(game_data.questions):
                from classquiz.socket_server import generate_final_results
                from classquiz.socket_server.battle_hooks import finalize_battle

                results = await generate_final_results(game_data, game_pin)
                await sio.emit("final_results", results, room=game_pin)
                await sio.emit("battle_finished", room=game_pin)
                await finalize_battle(game_pin, game_data)
                return
            from classquiz.socket_server.game_sync import emit_show_question

            refreshed = await PlayGame.get_from_redis(game_pin)
            await emit_show_question(sio, game_pin, refreshed, next_q)
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


def _schedule_advance(
    sio,
    game_pin: str,
    question_index: int,
    reveal_hold_sec: float,
    scoreboard_hold_sec: float = LIVE_SCOREBOARD_HOLD_SEC,
) -> None:
    prev = _advance_tasks.pop(game_pin, None)
    if prev is not None and not prev.done():
        prev.cancel()
    _advance_tasks[game_pin] = asyncio.create_task(
        _advance_after_reveal(sio, game_pin, question_index, reveal_hold_sec, scoreboard_hold_sec)
    )


async def close_question_now(sio, game_pin: str, question_index: int) -> bool:
    """Finalize a question once. Returns False if it was already closed."""
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.current_question != question_index:
        return False
    if not game_data.question_show:
        return False
    cancel_question_lifecycle(game_pin)
    await record_non_answers_as_wrong(game_pin, question_index)
    _, payload = await broadcast_question_results(sio, game_pin, question_index)
    _schedule_advance(
        sio,
        game_pin,
        question_index,
        float(payload["reveal_hold_sec"]),
        float(payload["scoreboard_hold_sec"]),
    )
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
