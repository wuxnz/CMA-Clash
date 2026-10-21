# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Regression: advancing a live kahoot game broadcasts Q2 to the game_pin room."""

from __future__ import annotations

import pytest

from classquiz.tests import ValueStorage, test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_players_in_game_room_receive_second_question(test_client) -> None:
    from unittest.mock import patch

    from classquiz.socket_server import join_game, register_as_admin, sio, start_game, submit_answer
    from classquiz.socket_server.question_lifecycle import _advance_after_reveal, close_question_now

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    await register_as_admin("pytest-admin-room", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-room",
        {"game_pin": game_pin, "username": "RoomP1", "captcha": "", "custom_field": ""},
    )
    await start_game("pytest-admin-room", {})
    await submit_answer("pytest-player-room", {"question_index": 0, "answer": "Yes"})
    await close_question_now(sio, game_pin, 0)

    emitted.clear()
    with patch("classquiz.socket_server.question_lifecycle.REVEAL_SEC", 0):
        await _advance_after_reveal(sio, game_pin, 0)

    q1 = [
        e
        for e in emitted
        if e[0] == "set_question_number"
        and e[1] == game_pin
        and isinstance(e[2], dict)
        and e[2].get("question_index") == 1
    ]
    assert q1, f"expected Q2 broadcast to room {game_pin}, got {emitted}"
    payload = q1[0][2]
    assert payload.get("question"), "players need question payload on advance"
    qr = [e for e in emitted if e[0] == "question_results"]
    for event, room, data in qr:
        assert room == game_pin
        assert isinstance(data, dict) and "question_index" in data and "results" in data

    sio.emit = real_emit
