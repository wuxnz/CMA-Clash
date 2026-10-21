# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import pytest

from classquiz.tests import ValueStorage, test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_timeout_marks_missing_players_wrong(test_client) -> None:
    from unittest.mock import AsyncMock

    from classquiz.config import redis
    from classquiz.db.models import PlayGame
    from classquiz.socket_server import join_game, register_as_admin, sio, start_game
    from classquiz.socket_server.question_lifecycle import close_question_now

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    assert start.status_code == 200, start.text
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    mock_sio = AsyncMock()
    await register_as_admin("pytest-admin-lc", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-lc",
        {
            "game_pin": game_pin,
            "username": "LonelyPlayer",
            "captcha": "",
            "custom_field": "",
        },
    )
    await start_game("pytest-admin-lc", {})

    closed = await close_question_now(mock_sio, game_pin, 0)
    assert closed is True

    rows = await redis.lrange(f"game_session:{game_pin}:0", 0, -1)
    assert rows, "expected a stored answer row for non-responder"
    assert '"right":false' in rows[0] or '"right": false' in rows[0]

    game_data = await PlayGame.get_from_redis(game_pin)
    assert game_data.question_show is False


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_early_complete_closes_question(test_client) -> None:
    from unittest.mock import AsyncMock

    from classquiz.socket_server import join_game, register_as_admin, sio, start_game, submit_answer
    from classquiz.socket_server.question_lifecycle import try_close_question_when_complete

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    mock_sio = AsyncMock()
    await register_as_admin("pytest-admin-ec", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-ec",
        {"game_pin": game_pin, "username": "OnlyOne", "captcha": "", "custom_field": ""},
    )
    await start_game("pytest-admin-ec", {})
    await submit_answer(
        "pytest-player-ec",
        {"question_index": 0, "answer": "Yes"},
    )
    await try_close_question_when_complete(mock_sio, game_pin, 0)
    events = [call.args[0] for call in mock_sio.emit.call_args_list]
    assert "question_results" in events
