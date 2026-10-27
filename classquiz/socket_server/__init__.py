# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


import base64
import hashlib
import json
import os

import socketio
from cryptography.fernet import Fernet

from classquiz.config import redis, settings
from classquiz.db.models import (
    PlayGame,
    QuizQuestionType,
    GameSession,
    GamePlayer,
    AnswerDataList,
    AnswerData,
)
from pydantic import BaseModel, ValidationError
from datetime import datetime

from classquiz.socket_server.helpers import (
    check_answer,
    check_captcha,
    has_already_answered,
)
from .models import (
    RejoinGameData,
    JoinGameData,
    ReturnQuestion,
    SubmitAnswerData,
    RegisterAsAdminData,
    KickPlayerInput,
    ConnectSessionIdEvent,
)

from classquiz.socket_server.export_helpers import save_quiz_to_storage
from classquiz.socket_server.game_sync import (
    battle_maybe_advance,
    emit_show_question,
    start_live_game,
    sync_player_to_live_game,
)
from classquiz.helpers.team_mode import score_with_streak
from classquiz.socket_server.timing import server_now_ms
from classquiz.socket_server.session import detach_socket_from_prior_game, get_session, save_session

_settings = settings()
_socket_cors = _settings.parsed_cors_origins() or "*"
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=_socket_cors)
settings = _settings


def get_fernet_key() -> bytes:
    hlib = hashlib.sha256()
    hlib.update(settings.secret_key.encode("utf-8"))
    return base64.urlsafe_b64encode(hlib.hexdigest().encode("latin-1")[:32])


fernet = Fernet(get_fernet_key())


async def _emit_clock_sync(sid: str) -> None:
    await sio.emit("clock_sync", {"server_time_ms": server_now_ms()}, room=sid)


async def generate_final_results(game_data: PlayGame, game_pin: str) -> dict:
    results = {}
    for i in range(len(game_data.questions)):
        redis_res = await redis.lrange(f"game_session:{game_pin}:{i}", 0, -1)
        if not redis_res:
            continue
        else:
            results[str(i)] = [json.loads(a) for a in redis_res]
    from classquiz.gamification.post_game import award_game_xp_once

    await award_game_xp_once(game_pin, game_data, results)
    return results


def calculate_score(z: float, t: int) -> int:
    t = t * 1000
    res = (t - z) / t
    return int(res * 1000)


async def set_answer(game_pin: str, q_index: int, data: AnswerData) -> int:
    # Appending is atomic, so concurrent submissions can't overwrite each other
    key = f"game_session:{game_pin}:{q_index}"
    answer_count = await redis.rpush(key, data.model_dump_json())
    await redis.expire(key, 7200)
    return answer_count


@sio.event
async def rejoin_game(sid: str, data: dict):
    redis_res = await redis.get(f"game:{data['game_pin']}")
    if redis_res is None:
        await sio.emit("game_not_found", room=sid)
        return
    try:
        data = RejoinGameData(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
    redis_sid_key = f"game_session:{data.game_pin}:players:{data.username}"
    old_sid = await redis.get(redis_sid_key)
    # A fast route remount can emit rejoin twice: the connect hook may already
    # have claimed the identity for this socket before the /play view mounts.
    # Accept that retry on the same socket while still rejecting stale tabs.
    if old_sid != data.old_sid and old_sid != sid:
        await sio.emit("rejoin_rejected", {"code": "stale_sid"}, room=sid)
        return
    try:
        prior = await get_session(sid, sio, disconnect_on_error=False)
        prior_pin = prior.get("game_pin")
        if prior_pin and prior_pin != data.game_pin:
            await sio.emit("rejoin_rejected", {"code": "pin_mismatch"}, room=sid)
            return
    except ConnectionRefusedError:
        pass
    await redis.set(redis_sid_key, sid)
    await redis.srem(
        f"game_session:{data.game_pin}:players",
        GamePlayer(username=data.username, sid=data.old_sid).model_dump_json(),
    )
    await redis.sadd(
        f"game_session:{data.game_pin}:players",
        GamePlayer(username=data.username, sid=sid).model_dump_json(),
    )
    game_data = PlayGame.model_validate_json(redis_res)
    session = {
        "game_pin": data.game_pin,
        "username": data.username,
        "sid_custom": sid,
        "admin": False,
    }
    await save_session(sid, sio, session)
    await sio.enter_room(sid, data.game_pin)
    encrypted_datetime = fernet.encrypt(datetime.now().isoformat().encode("utf-8")).decode("utf-8")
    await sio.emit("time_sync", encrypted_datetime, room=sid)
    await _emit_clock_sync(sid)
    await sio.emit(
        "rejoined_game",
        game_data.to_player_data(),
        room=sid,
    )
    if game_data.started:
        await sync_player_to_live_game(sio, sid, data.game_pin, game_data)


@sio.event
async def join_game(sid: str, data: dict):
    redis_res = await redis.get(f"game:{data['game_pin']}")
    if redis_res is None:
        await sio.emit("game_not_found", room=sid)
        return
    try:
        data = JoinGameData(**data)
    except ValidationError as e:
        await sio.emit("join_error", {"code": "invalid_payload"}, room=sid)
        print(e)
        return
    game_data = PlayGame.model_validate_json(redis_res)
    game_pin = data.game_pin
    prior_sid = await redis.get(f"game_session:{data.game_pin}:players:{data.username}")
    if game_data.game_mode == "battle":
        from classquiz.socket_server.battle_sync import (
            is_battle_finished,
            is_username_in_battle_roster,
        )

        if await is_battle_finished(game_pin):
            await sio.emit("join_error", {"code": "game_finished"}, room=sid)
            return
        if not await is_username_in_battle_roster(game_pin, data.username):
            await sio.emit("join_error", {"code": "not_in_battle"}, room=sid)
            return
    if game_data.started:
        if game_data.game_mode != "battle" and prior_sid is None:
            await sio.emit("join_error", {"code": "game_already_started"}, room=sid)
            return
    # +++ START checking captcha +++
    if game_data.captcha_enabled:
        captcha_res = await check_captcha(data.captcha)
        if not captcha_res:
            await sio.emit("join_error", {"code": "captcha_failed"}, room=sid)
            return
    # --- END checking captcha ---
    if prior_sid is not None:
        # A name is the player's identity for this match. Reclaim it on a fresh
        # join (e.g. after storage/cookie loss) and replace its old socket entry.
        await redis.srem(
            f"game_session:{data.game_pin}:players",
            GamePlayer(username=data.username, sid=prior_sid).model_dump_json(),
        )
        await sio.leave_room(prior_sid, data.game_pin)

    await detach_socket_from_prior_game(sio, sid)

    session = {
        "game_pin": data.game_pin,
        "username": data.username,
        "sid_custom": sid,
        "admin": False,
    }
    await save_session(sid, sio, session)
    await sio.emit(
        "joined_game",
        game_data.to_player_data(),
        room=sid,
    )
    await redis.set(f"game_session:{data.game_pin}:players:{data.username}", sid, ex=7200)
    await GamePlayer(username=data.username, sid=sid).to_player_stack(data.game_pin)

    if data.custom_field == "":
        data.custom_field = None
    if data.custom_field is not None:
        await redis.hset(
            f"game:{data.game_pin}:players:custom_fields",
            data.username,
            data.custom_field,
        )

    await sio.emit(
        "player_joined",
        {"username": data.username, "sid": sid},
        room=f"admin:{data.game_pin}",
    )
    # +++ Time-Sync +++
    encrypted_datetime = fernet.encrypt(datetime.now().isoformat().encode("utf-8")).decode("utf-8")
    await sio.emit("time_sync", encrypted_datetime, room=sid)
    await _emit_clock_sync(sid)
    # --- Time-Sync ---
    await sio.enter_room(sid, data.game_pin)
    if game_data.team_mode:
        from classquiz.socket_server.team_live import emit_team_roster, place_unassigned

        await place_unassigned(game_pin, game_data)
        await emit_team_roster(sio, game_pin)
    if game_data.game_mode == "battle":
        from classquiz.socket_server.battle_sync import battle_player_joined_socket

        await battle_player_joined_socket(sio, data.game_pin, data.username)
    if game_data.started:
        await sync_player_to_live_game(sio, sid, data.game_pin, game_data)


@sio.event
async def start_game(sid: str, _data: dict):
    session = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_pin = session["game_pin"]
    from classquiz.socket_server.team_live import emit_team_roster, place_unassigned, reshuffle_random_teams

    game = await PlayGame.get_from_redis(game_pin)
    if game.team_mode:
        if game.team_mode["assign"] == "random":
            await reshuffle_random_teams(game_pin, game)
        else:
            await place_unassigned(game_pin, game, at_start=True)
        await emit_team_roster(sio, game_pin)
    await start_live_game(sio, game_pin, show_first_question=True)


@sio.event
async def set_team_mode(sid: str, data: dict):
    """Host sets team count and assignment (match games only, before start)."""
    from classquiz.socket_server.team_live import emit_team_roster, set_team_mode as save_team_mode

    session = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_pin = session["game_pin"]
    try:
        await save_team_mode(game_pin, int(data.get("count", 2)), str(data.get("assign", "random")))
    except ValueError as e:
        await sio.emit("team_error", {"code": str(e)}, room=sid)
        return
    await emit_team_roster(sio, game_pin)


@sio.event
async def get_team_roster(sid: str, _data: dict):
    """Send the current team roster to the asking socket (for screens that open after joins)."""
    from classquiz.socket_server.team_live import roster_payload

    session = await get_session(sid, sio)
    game_pin = session.get("game_pin")
    if not game_pin:
        return
    game = await PlayGame.get_from_redis(game_pin)
    if not game.team_mode:
        return
    await sio.emit("team_roster", await roster_payload(game_pin), room=sid)


@sio.event
async def choose_team(sid: str, data: dict):
    """Player picks a team in the lobby (choose mode, before start)."""
    from classquiz.socket_server.team_live import choose_team as pick_team, emit_team_roster

    session = await get_session(sid, sio)
    game_pin = session.get("game_pin")
    username = session.get("username")
    if not game_pin or not username:
        return
    try:
        await pick_team(game_pin, username, int(data.get("team", -1)))
    except (ValueError, TypeError) as e:
        await sio.emit("team_error", {"code": str(e)}, room=sid)
        return
    await emit_team_roster(sio, game_pin)


@sio.event
async def register_as_admin(sid: str, data: dict):
    try:
        data = RegisterAsAdminData(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
        return
    game_pin = data.game_pin
    game_id = data.game_id
    existing_session = await redis.get(f"game_session:{game_pin}")
    if existing_session is not None:
        try:
            saved_session = GameSession.model_validate_json(existing_session)
        except Exception:
            await sio.emit("already_registered_as_admin", room=sid)
            return
        if saved_session.game_id != game_id:
            await sio.emit("already_registered_as_admin", room=sid)
            return
        saved_session.admin = sid
        await saved_session.save(game_pin)
    else:
        await GameSession(admin=sid, game_id=game_id, answers=[]).save(game_pin)
    await sio.emit(
        "registered_as_admin",
        {"game_id": game_id, "game": await redis.get(f"game:{game_pin}")},
        room=sid,
    )
    session = {"game_pin": game_pin, "admin": True, "remote": False}
    await save_session(sid, sio, session)
    await sio.enter_room(sid, game_pin)
    await sio.enter_room(sid, f"admin:{data.game_pin}")
    # Replay the current lobby roster so a refreshed host page is not blank.
    try:
        _existing_players = await redis.smembers(f"game_session:{game_pin}:players")
    except Exception:
        _existing_players = set()
    for _raw in _existing_players:
        try:
            _player = GamePlayer.model_validate_json(_raw)
        except Exception:
            continue
        await sio.emit(
            "player_joined",
            {"username": _player.username, "sid": _player.sid},
            room=f"admin:{data.game_pin}",
        )
    game_data = await PlayGame.get_from_redis(game_pin)
    if game_data.started:
        await sio.emit("start_game", room=sid)
        if game_data.current_question >= 0:
            if game_data.question_show:
                from classquiz.socket_server.game_sync import sync_player_to_live_game

                await sync_player_to_live_game(sio, sid, game_pin, game_data)
            else:
                from classquiz.socket_server.question_lifecycle import build_question_results_payload

                payload, _ = await build_question_results_payload(game_pin, game_data.current_question)
                await sio.emit("question_results", payload, room=sid)


@sio.event
async def get_question_results(sid: str, data: dict):
    session = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_pin = session["game_pin"]
    question_number = int(data["question_number"])
    from classquiz.socket_server.question_lifecycle import close_question_now

    closed = await close_question_now(sio, game_pin, question_number)
    if not closed:
        # Question already closed (auto-advance or prior show_results). Re-emit only for
        # late admin sync — clients must treat question_results idempotently per index.
        from classquiz.socket_server.question_lifecycle import build_question_results_payload

        game_data = await PlayGame.get_from_redis(game_pin)
        if not game_data.question_show and game_data.current_question == question_number:
            payload, _ = await build_question_results_payload(game_pin, question_number)
            await sio.emit("question_results", payload, room=game_pin)


@sio.event
async def set_question_number(sid: str, data: str):
    # data is just a number (as a str) of the question
    session = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_pin = session["game_pin"]
    game_data = await PlayGame.get_from_redis(session["game_pin"])
    question_index = int(float(data))
    if game_data.questions[question_index].type == QuizQuestionType.SLIDE:
        game_data.current_question = question_index
        game_data.question_show = True
        await game_data.save(game_pin)
        await sio.emit("set_question_number", {"question_index": question_index}, room=sid)
        return
    await emit_show_question(sio, game_pin, game_data, question_index)


async def advance_player_streak(game_pin: str, username: str, question_index: int, correct: bool) -> int:
    """Read the player's streak, advance it for this answer, store it, and return the new value."""
    from classquiz.helpers.team_mode import advance_streak

    key = f"game_session:{game_pin}:streak:{username}"
    prev_streak, prev_question = 0, None
    raw = await redis.get(key)
    if raw:
        stored = json.loads(raw)
        prev_streak, prev_question = int(stored["n"]), int(stored["q"])
    streak = advance_streak(prev_streak, prev_question, question_index, correct)
    await redis.set(key, json.dumps({"n": streak, "q": question_index}), ex=7200)
    return streak


async def _score_live_answer(
    game_pin: str,
    question_index: int,
    question_time_sec: int,
    answer_right: bool,
    latency_ms: int,
) -> tuple[int, int, int, float]:
    """Return base_score, speed_bonus, total_score, time_taken_ms (server timing)."""
    from classquiz.helpers.live_scoring import score_correct_answer
    from classquiz.socket_server.timing import load_question_timing, server_now_ms

    if not answer_right:
        return 0, 0, 0, 0.0

    submitted_ms = server_now_ms()
    timing = await load_question_timing(game_pin)
    if timing and timing.get("question_index") == question_index:
        phase_start = int(timing["answer_phase_start_ms"])
        deadline = int(timing["answer_deadline_ms"])
        time_taken = float(max(0, submitted_ms - phase_start - latency_ms))
        base, bonus, total = score_correct_answer(submitted_ms - latency_ms, phase_start, deadline)
        return base, bonus, total, time_taken

    raw_start = await redis.get(f"game:{game_pin}:current_time")
    if not raw_start:
        window_ms = max(1000, question_time_sec * 1000)
        base, bonus, total = score_correct_answer(submitted_ms - latency_ms, submitted_ms - window_ms, submitted_ms)
        return base, bonus, total, 0.0

    time_q_started = datetime.fromisoformat(raw_start)
    now = datetime.now()
    diff_ms = abs((now - time_q_started).total_seconds() * 1000) - latency_ms
    window_ms = max(1000, question_time_sec * 1000)
    phase_start = int(now.timestamp() * 1000) - int(diff_ms)
    deadline = phase_start + window_ms
    base, bonus, total = score_correct_answer(int(now.timestamp() * 1000) - latency_ms, phase_start, deadline)
    return base, bonus, total, float(diff_ms)


@sio.event
async def submit_answer(sid: str, data: dict):
    try:
        data = SubmitAnswerData(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
        return
    data.answer = str(data.answer)
    session = await get_session(sid, sio)
    question_index = int(float(data.question_index))
    game_pin = session["game_pin"]
    game_data = await PlayGame.get_from_redis(game_pin)

    if question_index != game_data.current_question:
        await sio.emit("question_not_active", room=sid)
        return

    already_answered = await has_already_answered(game_pin, question_index, session["username"])
    if already_answered:
        await sio.emit("already_replied", room=sid)
        return

    answer_right, answer = check_answer(game_data, data)
    latency = int(float(session.get("ping", 0)))
    q_time = int(float(game_data.questions[question_index].time))
    base_score, speed_bonus, _unused_total, time_taken = await _score_live_answer(
        game_pin, question_index, q_time, answer_right, latency
    )
    # Streaks apply to every game type (battle, standard and on-device matches) because they
    # all come through this handler.
    if game_data.team_mode:
        # Team games: keep the vote only. Points and streaks are settled for the whole team
        # when the question closes (team_live.resolve_team_round).
        streak, streak_bonus, score = 0, 0, 0
    else:
        streak = await advance_player_streak(game_pin, session["username"], question_index, answer_right)
        if answer_right:
            score = score_with_streak(base_score, speed_bonus, streak)
        else:
            score = 0
        streak_bonus = score - (base_score + speed_bonus) if answer_right else 0
        await redis.hincrby(f"game_session:{game_pin}:player_scores", session["username"], score)
    answer_data = AnswerData(
        username=session["username"],
        answer=answer,
        right=answer_right,
        time_taken=time_taken,
        score=score,
        base_score=base_score,
        speed_bonus=speed_bonus,
        streak=streak,
        streak_bonus=streak_bonus,
    )
    game_pin = session["game_pin"]
    answer_count = await set_answer(game_pin=game_pin, q_index=question_index, data=answer_data)
    if game_data.game_mode == "battle":
        from classquiz.socket_server.battle_sync import battle_roster_size

        player_count = await battle_roster_size(game_pin)
    else:
        player_count = await redis.scard(f"game_session:{game_pin}:players")
    await sio.emit("player_answer", {}, room=f"admin:{game_pin}")
    if player_count > 0 and answer_count >= player_count:
        game_data = await PlayGame.get_from_redis(game_pin)
        await sio.emit("everyone_answered", {}, room=game_pin)
        if game_data.game_mode == "battle":
            game_data.question_show = False
            await game_data.save(game_pin)
            await battle_maybe_advance(sio, session["game_pin"], game_data)
        else:
            from classquiz.socket_server.question_lifecycle import try_close_question_when_complete

            await try_close_question_when_complete(sio, game_pin, question_index)


@sio.event
async def get_final_results(sid: str, _data: dict):
    session: dict = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_data = await PlayGame.get_from_redis(session["game_pin"])
    results = await generate_final_results(game_data, session["game_pin"])
    await sio.emit("final_results", results, room=session["game_pin"])


@sio.event
async def get_export_token(sid: str):
    session = await get_session(sid, sio)
    if not session["admin"]:
        return
    game_data = await PlayGame.get_from_redis(session["game_pin"])
    results = await generate_final_results(game_data, session["game_pin"])
    token = os.urandom(32).hex()
    await redis.set(f"export_token:{token}", json.dumps(results), ex=7200)
    await sio.emit("export_token", token, room=sid)


@sio.event
async def show_solutions(sid: str, _data: dict):
    session: dict = await get_session(sid, sio)
    game_data = await PlayGame.get_from_redis(session["game_pin"])
    if not session["admin"]:
        return
    await sio.emit(
        "solutions",
        game_data.questions[game_data.current_question].model_dump(),
        room=session["game_pin"],
    )


@sio.event
async def echo_time_sync(sid: str, data: str):
    then_dec = fernet.decrypt(data).decode("utf-8")
    then = datetime.fromisoformat(then_dec)
    now = datetime.now()
    delta = now - then
    session = await get_session(sid, sio)
    session["ping"] = delta.microseconds / 1000
    await save_session(sid, sio, session)
    await _emit_clock_sync(sid)


@sio.event
async def kick_player(sid: str, data: dict):
    try:
        data = KickPlayerInput(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
        return

    session: dict = await get_session(sid, sio)
    if not session["admin"]:
        return

    player_sid = await redis.get(f"game_session:{session['game_pin']}:players:{data.username}")
    await redis.srem(
        f"game_session:{session['game_pin']}:players",
        GamePlayer(username=data.username, sid=player_sid).model_dump_json(),
    )
    await sio.leave_room(player_sid, session["game_pin"])
    await sio.emit("kick", room=player_sid)


class _RegisterAsRemoteInput(BaseModel):
    game_pin: str
    game_id: str


@sio.event
async def register_as_remote(sid: str, data: dict):
    try:
        data = _RegisterAsRemoteInput(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
        return
    await sio.emit(
        "registered_as_admin",
        {"game_id": data.game_id, "game": await redis.get(f"game:{data.game_pin}")},
        room=sid,
    )
    await sio.emit("control_visibility", {"visible": False}, room=f"admin:{data.game_pin}")
    session = await get_session(sid, sio)
    session["game_pin"] = data.game_pin
    session["admin"] = True
    session["remote"] = True
    await save_session(sid, sio, session)
    await sio.enter_room(sid, data.game_pin)
    await sio.enter_room(sid, f"admin:{data.game_pin}")


class _SetControlVisibilityInput(BaseModel):
    visible: bool


@sio.event
async def set_control_visibility(sid: str, data: dict):
    try:
        data = _SetControlVisibilityInput(**data)
    except ValidationError as e:
        await sio.emit("error", room=sid)
        print(e)
        return
    session: dict = await get_session(sid, sio)
    await sio.emit(
        "control_visibility",
        {"visible": data.visible},
        room=f"admin:{session['game_pin']}",
    )


@sio.event
async def save_quiz(sid: str):
    session: dict = await get_session(sid, sio)
    if not session["admin"]:
        return
    await save_quiz_to_storage(session["game_pin"])
    await sio.emit("results_saved_successfully")


@sio.event
async def connect(sid: str, _environ, _auth):
    session_id = os.urandom(16).hex()
    print("Connection opened with handler")
    sio_session = {"session_id": session_id}
    await sio.save_session(sid, sio_session)
    await sio.emit("session_id", ConnectSessionIdEvent(session_id=session_id).dict(), room=sid)
