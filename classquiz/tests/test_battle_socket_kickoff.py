# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Battle kickoff: roster joins must emit start_game and question 0."""

from __future__ import annotations

import json

import pytest

from classquiz.tests import test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_try_kickoff_battle_parses_kickoff_json() -> None:
    """Regression: try_kickoff_battle must not raise NameError on json.loads."""
    from unittest.mock import AsyncMock, patch

    from classquiz.battle.service import BATTLE_REDIS_PREFIX
    from classquiz.config import redis
    from classquiz.socket_server.game_sync import try_kickoff_battle

    game_pin = "908877"
    await redis.set(
        f"{BATTLE_REDIS_PREFIX}:kickoff:{game_pin}",
        json.dumps({"usernames": ["A", "B"], "kicked_off": False}),
        ex=60,
    )
    sio = AsyncMock()
    with patch("classquiz.socket_server.game_sync.start_live_game", AsyncMock()) as start_live:
        await try_kickoff_battle(sio, game_pin)
        start_live.assert_awaited_once()


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_battle_two_join_game_emits_start_and_question_zero(test_client) -> None:
    """Both roster players join_game → kickoff → start_game + set_question_number(0)."""
    from classquiz.socket_server import join_game, sio

    test_client.cookies.clear()
    quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1}).json()
    assert quizzes
    quiz_id = quizzes[0]["id"]
    create = test_client.post(
        "/api/v1/clash/battles",
        json={"quiz_id": quiz_id, "max_players": 2, "display_name": "HostGuest"},
    )
    assert create.status_code == 200, create.text
    lobby = create.json()
    code = lobby["battle_code"]
    host_name = lobby["player_slots"][0]["username"]
    join = test_client.post(
        f"/api/v1/clash/battles/{code}/join",
        json={"display_name": "GuestTwo"},
    )
    assert join.status_code == 200, join.text
    guest_name = join.json()["player_slots"][1]["username"]
    start = test_client.post(
        f"/api/v1/clash/battles/{code}/start",
        json={"host_secret": lobby["host_secret"]},
    )
    assert start.status_code == 200, start.text
    game_pin = start.json()["game_pin"]

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    for sid, name in (("pytest-sid-host", host_name), ("pytest-sid-guest", guest_name)):
        await join_game(
            sid,
            {
                "game_pin": game_pin,
                "username": name,
                "captcha": "",
                "custom_field": "",
            },
        )

    events = [e[0] for e in emitted]
    assert "start_game" in events
    q0 = [e for e in emitted if e[0] == "set_question_number" and e[2] and e[2].get("question_index") == 0]
    assert q0, f"expected question 0 emit, got {emitted}"

    sio.emit = real_emit
