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
    qr = next(c for c in mock_sio.emit.call_args_list if c.args[0] == "question_results")
    assert qr.args[1]["question_index"] == 0
    assert isinstance(qr.args[1]["results"], list)


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_advance_after_reveal_emits_next_question_to_game_room(test_client) -> None:
    from unittest.mock import AsyncMock, patch

    from classquiz.socket_server import join_game, register_as_admin, start_game, submit_answer
    from classquiz.socket_server.question_lifecycle import _advance_after_reveal, close_question_now

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    mock_sio = AsyncMock()
    await register_as_admin("pytest-admin-adv", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-adv",
        {"game_pin": game_pin, "username": "AdvP1", "captcha": "", "custom_field": ""},
    )
    await start_game("pytest-admin-adv", {})
    await submit_answer("pytest-player-adv", {"question_index": 0, "answer": "Yes"})
    await close_question_now(mock_sio, game_pin, 0)

    mock_sio.reset_mock()
    with patch("classquiz.socket_server.question_lifecycle.live_post_question_hold_sec", lambda: 0):
        await _advance_after_reveal(mock_sio, game_pin, 0)

    set_calls = [c for c in mock_sio.emit.call_args_list if c.args[0] == "set_question_number"]
    assert set_calls, "expected set_question_number after reveal"
    assert set_calls[0].kwargs.get("room") == game_pin
    assert set_calls[0].args[1]["question_index"] == 1


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_submit_answer_increments_redis_total_once(test_client) -> None:
    import json

    from classquiz.config import redis
    from classquiz.socket_server import join_game, register_as_admin, start_game, submit_answer
    from classquiz.socket_server.question_lifecycle import close_question_now

    start = test_client.post(
        f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False",
        cookies=ValueStorage.cookies,
    )
    body = start.json()
    game_pin = body["game_pin"]
    game_id = body["game_id"]

    await register_as_admin("pytest-admin-score", {"game_pin": game_pin, "game_id": game_id})
    await join_game(
        "pytest-player-score",
        {"game_pin": game_pin, "username": "Scorer", "captcha": "", "custom_field": ""},
    )
    await start_game("pytest-admin-score", {})

    before = int(await redis.hget(f"game_session:{game_pin}:player_scores", "Scorer") or 0)
    await submit_answer("pytest-player-score", {"question_index": 0, "answer": "Yes"})
    after_submit = int(await redis.hget(f"game_session:{game_pin}:player_scores", "Scorer") or 0)
    rows = await redis.lrange(f"game_session:{game_pin}:0", 0, -1)
    row_score = json.loads(rows[0])["score"]

    assert after_submit - before == row_score
    assert row_score > 0

    from unittest.mock import AsyncMock

    mock_sio = AsyncMock()
    await close_question_now(mock_sio, game_pin, 0)
    after_close = int(await redis.hget(f"game_session:{game_pin}:player_scores", "Scorer") or 0)
    assert after_close == after_submit
