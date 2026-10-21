# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import pytest

from classquiz.tests import ValueStorage, test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_rejoin_stale_sid_emits_rejected(test_client) -> None:
    from classquiz.socket_server import join_game, rejoin_game, register_as_admin, sio

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert start.status_code == 200, start.text
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    await register_as_admin("pytest-admin-rejoin", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-rejoin",
        {
            "game_pin": game_pin,
            "username": "RejoinPlayer",
            "captcha": "",
            "custom_field": "",
        },
    )

    emitted: list[tuple] = []
    real_emit = sio.emit

    async def record_emit(event, data=None, room=None, **kwargs):
        emitted.append((event, room, data))
        return await real_emit(event, data=data, room=room, **kwargs)

    sio.emit = record_emit

    await rejoin_game(
        "pytest-player-rejoin",
        {
            "username": "RejoinPlayer",
            "game_pin": game_pin,
            "old_sid": "wrong-sid",
        },
    )

    rejected = [e for e in emitted if e[0] == "rejoin_rejected"]
    assert rejected
    assert rejected[-1][2].get("code") == "stale_sid"
