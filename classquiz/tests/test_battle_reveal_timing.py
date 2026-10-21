# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Battle reveal: question_results must not be followed immediately by the next question."""

from __future__ import annotations

import pytest

from classquiz.tests import test_client  # noqa: F401


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_battle_maybe_advance_schedules_hold_before_next_question(test_client) -> None:
    from unittest.mock import AsyncMock, patch

    from classquiz.socket_server import join_game, sio, submit_answer
    from classquiz.socket_server.game_sync import battle_maybe_advance

    test_client.cookies.clear()
    quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1}).json()
    assert quizzes
    quiz_id = quizzes[0]["id"]
    create = test_client.post(
        "/api/v1/clash/battles",
        json={"quiz_id": quiz_id, "max_players": 2},
    )
    assert create.status_code == 200, create.text
    lobby = create.json()
    code = lobby["battle_code"]
    host_join = test_client.post(
        f"/api/v1/clash/battles/{code}/join",
        json={"display_name": "HoldHost"},
    )
    assert host_join.status_code == 200, host_join.text
    host_name = host_join.json()["player_slots"][0]["username"]
    guest_join = test_client.post(
        f"/api/v1/clash/battles/{code}/join",
        json={"display_name": "HoldGuest"},
    )
    assert guest_join.status_code == 200, guest_join.text
    guest_name = guest_join.json()["player_slots"][1]["username"]
    start = test_client.post(
        f"/api/v1/clash/battles/{code}/start",
        json={"host_secret": lobby["host_secret"]},
    )
    assert start.status_code == 200, start.text
    game_pin = start.json()["game_pin"]

    for sid, name in (("pytest-battle-hold-host", host_name), ("pytest-battle-hold-guest", guest_name)):
        await join_game(
            sid,
            {
                "game_pin": game_pin,
                "username": name,
                "captcha": "",
                "custom_field": "",
            },
        )

    from unittest.mock import patch

    with patch("classquiz.socket_server.battle_maybe_advance", AsyncMock()):
        await submit_answer("pytest-battle-hold-host", {"question_index": 0, "answer": "Yes"})
        await submit_answer("pytest-battle-hold-guest", {"question_index": 0, "answer": "No"})

    mock_sio = AsyncMock()
    from classquiz.db.models import PlayGame

    game_data = await PlayGame.get_from_redis(game_pin)
    await battle_maybe_advance(mock_sio, game_pin, game_data)

    events = [call.args[0] for call in mock_sio.emit.call_args_list]
    assert "question_results" in events
    assert "set_question_number" not in events

    qr = next(c for c in mock_sio.emit.call_args_list if c.args[0] == "question_results")
    payload = qr.args[1]
    assert payload["reveal_hold_sec"] >= 8.0
    assert payload["scoreboard_hold_sec"] == 9.0

    from classquiz.socket_server.question_lifecycle import _advance_after_reveal

    mock_sio.reset_mock()
    with patch("asyncio.sleep", new_callable=AsyncMock):
        await _advance_after_reveal(
            mock_sio,
            game_pin,
            0,
            float(payload["reveal_hold_sec"]),
            float(payload["scoreboard_hold_sec"]),
        )

    set_calls = [c for c in mock_sio.emit.call_args_list if c.args[0] == "set_question_number"]
    assert set_calls, "expected next question after reveal + scoreboard hold"
    assert set_calls[0].args[1]["question_index"] == 1


@pytest.mark.order("last")
@pytest.mark.asyncio
async def test_battle_maybe_advance_is_idempotent_per_question(test_client) -> None:
    from unittest.mock import AsyncMock

    from classquiz.socket_server import join_game, sio, submit_answer
    from classquiz.socket_server.game_sync import battle_maybe_advance

    test_client.cookies.clear()
    quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1}).json()
    quiz_id = quizzes[0]["id"]
    create = test_client.post(
        "/api/v1/clash/battles",
        json={"quiz_id": quiz_id, "max_players": 2},
    )
    lobby = create.json()
    code = lobby["battle_code"]
    host_name = test_client.post(
        f"/api/v1/clash/battles/{code}/join",
        json={"display_name": "IdemA"},
    ).json()["player_slots"][0]["username"]
    guest_name = test_client.post(
        f"/api/v1/clash/battles/{code}/join",
        json={"display_name": "IdemB"},
    ).json()["player_slots"][1]["username"]
    game_pin = test_client.post(
        f"/api/v1/clash/battles/{code}/start",
        json={"host_secret": lobby["host_secret"]},
    ).json()["game_pin"]

    for sid, name in (("pytest-battle-idem-a", host_name), ("pytest-battle-idem-b", guest_name)):
        await join_game(
            sid,
            {"game_pin": game_pin, "username": name, "captcha": "", "custom_field": ""},
        )

    from unittest.mock import patch

    with patch("classquiz.socket_server.battle_maybe_advance", AsyncMock()):
        await submit_answer("pytest-battle-idem-a", {"question_index": 0, "answer": "Yes"})
        await submit_answer("pytest-battle-idem-b", {"question_index": 0, "answer": "No"})

    mock_sio = AsyncMock()
    from classquiz.db.models import PlayGame

    game_data = await PlayGame.get_from_redis(game_pin)
    await battle_maybe_advance(mock_sio, game_pin, game_data)
    first_results = [c for c in mock_sio.emit.call_args_list if c.args[0] == "question_results"]
    assert len(first_results) == 1

    mock_sio.reset_mock()
    game_data = await PlayGame.get_from_redis(game_pin)
    await battle_maybe_advance(mock_sio, game_pin, game_data)
    assert not [c for c in mock_sio.emit.call_args_list if c.args[0] == "question_results"]
