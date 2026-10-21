# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Hosted quiz socket flow: kahoot vs normal game modes."""

from __future__ import annotations

import pytest

from classquiz.tests import ValueStorage, test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_kahoot_start_emits_question_with_answers(test_client) -> None:
    from classquiz.config import redis
    from classquiz.socket_server import join_game, register_as_admin, sio, start_game

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert start.status_code == 200, start.text
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    await register_as_admin("pytest-admin", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player",
        {
            "game_pin": game_pin,
            "username": "PlayerOne",
            "captcha": "",
            "custom_field": "",
        },
    )
    await start_game("pytest-admin", {})

    q_events = [
        e
        for e in emitted
        if e[0] == "set_question_number" and e[2] and e[2].get("question_index") == 0
    ]
    assert q_events, f"expected question 0 broadcast, got {emitted}"
    payload = q_events[0][2]
    assert payload.get("question"), "players need question payload to render answers"
    answers = payload["question"].get("answers")
    assert isinstance(answers, list) and len(answers) > 0
    assert payload.get("answer_deadline_ms") > payload.get("answer_phase_start_ms")
    assert payload.get("intro_deadline_ms") == payload.get("question_start_ms")
    assert payload.get("server_time_ms") is not None

    from classquiz.socket_server.timing import load_question_timing

    stored_timing = await load_question_timing(game_pin)
    assert stored_timing is not None
    assert stored_timing["answer_deadline_ms"] == payload["answer_deadline_ms"]

    stored = await redis.get(f"game:{game_pin}")
    assert stored is not None
    assert '"game_mode":"kahoot"' in stored or '"game_mode": "kahoot"' in stored

    sio.emit = real_emit


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_normal_start_waits_for_host_question(test_client) -> None:
    from classquiz.socket_server import join_game, register_as_admin, sio, start_game

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=normal&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert start.status_code == 200, start.text
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    await register_as_admin("pytest-admin-n", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-n",
        {
            "game_pin": game_pin,
            "username": "PlayerNorm",
            "captcha": "",
            "custom_field": "",
        },
    )
    await start_game("pytest-admin-n", {})

    assert any(e[0] == "start_game" for e in emitted)
    assert not any(e[0] == "set_question_number" for e in emitted), (
        "normal mode should not auto-show question 0 on start"
    )

    sio.emit = real_emit


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_rejoin_sync_keeps_deadlines(test_client) -> None:
    from classquiz.db.models import PlayGame
    from classquiz.socket_server import join_game, register_as_admin, sio, start_game
    from classquiz.socket_server.game_sync import sync_player_to_live_game
    from classquiz.socket_server.timing import load_question_timing

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert start.status_code == 200, start.text
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    await register_as_admin("pytest-admin-r", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-r",
        {
            "game_pin": game_pin,
            "username": "PlayerRejoin",
            "captcha": "",
            "custom_field": "",
        },
    )
    await start_game("pytest-admin-r", {})

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    game_data = await PlayGame.get_from_redis(game_pin)
    timing_before = await load_question_timing(game_pin)
    assert timing_before is not None

    await sync_player_to_live_game(sio, "pytest-rejoin-sid", game_pin, game_data)

    sync_events = [e for e in emitted if e[0] == "set_question_number" and e[1] == "pytest-rejoin-sid"]
    assert sync_events, emitted
    payload = sync_events[0][2]
    assert payload["answer_deadline_ms"] == timing_before["answer_deadline_ms"]
    assert payload["intro_deadline_ms"] == timing_before["intro_deadline_ms"]

    sio.emit = real_emit


@pytest.mark.order("last")
def test_to_player_data_is_object_not_tuple() -> None:
    import uuid

    from classquiz.db.models import PlayGame, QuizQuestion, QuizQuestionType

    game = PlayGame(
        quiz_id=uuid.uuid4(),
        description="d",
        user_id=uuid.uuid4(),
        title="t",
        questions=[
            QuizQuestion(
                question="q",
                answers=[{"answer": "a", "right": True, "color": "#f00"}],
                type=QuizQuestionType.ABCD,
                time="30",
            )
        ],
        game_id=uuid.uuid4(),
        game_pin="123456",
        game_mode="kahoot",
    )
    data = game.to_player_data()
    assert isinstance(data, dict)
    assert data.get("game_mode") == "kahoot"
    assert data.get("question_count") == 1
