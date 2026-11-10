# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""A player who refreshes a started match can rejoin it on the same name and PIN."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from classquiz.tests import test_client  # noqa: F401


def _events(emit: AsyncMock) -> list[str]:
    return [call.args[0] for call in emit.call_args_list]


def test_started_match_rejoins_after_refresh(test_client: TestClient) -> None:
    from classquiz.socket_server import join_game, rejoin_game, sio
    from classquiz.socket_server.game_sync import start_live_game
    from classquiz.tests.test_server import TestUsers

    TestUsers.ensure_logged_in(test_client)
    quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 5}).json()
    assert quizzes
    start = test_client.post(f"/api/v1/quiz/start/{quizzes[0]['id']}?game_mode=kahoot&captcha_enabled=False")
    assert start.status_code == 200, start.text
    game_pin = start.json()["game_pin"]
    username = "RefreshAda"
    first_sid = "pytest-match-rejoin-first"
    second_sid = "pytest-match-rejoin-second"
    third_sid = "pytest-match-rejoin-third"

    # No real socket connects in this test, so keep each socket's session in memory.
    sessions: dict[str, dict] = {}

    async def fake_get_session(sid, _sio, disconnect_on_error=True):
        if sid in sessions:
            return sessions[sid]
        if disconnect_on_error:
            raise ConnectionRefusedError("session not available")
        return {}

    async def fake_save_session(sid, _sio, data, disconnect_on_error=True):
        sessions[sid] = data

    async def fake_detach(_sio, _sid):
        return None

    async def scenario() -> dict[str, list[str]]:
        seen: dict[str, list[str]] = {}
        with (
            patch.object(sio, "emit", new=AsyncMock()) as emit,
            patch.object(sio, "enter_room", new=AsyncMock()),
            patch.object(sio, "leave_room", new=AsyncMock()),
            patch("classquiz.socket_server.get_session", new=fake_get_session),
            patch("classquiz.socket_server.save_session", new=fake_save_session),
            patch("classquiz.socket_server.detach_socket_from_prior_game", new=fake_detach),
        ):
            await join_game(first_sid, {"game_pin": game_pin, "username": username, "captcha": "", "custom_field": ""})
            seen["join"] = _events(emit)
            emit.reset_mock()

            await start_live_game(AsyncMock(), game_pin, show_first_question=True)

            # The page refreshes: the socket is new and names the old one in its saved session.
            await rejoin_game(second_sid, {"game_pin": game_pin, "username": username, "old_sid": first_sid})
            seen["rejoin"] = _events(emit)
            emit.reset_mock()

            # The player types the same name and PIN again instead of using the saved session.
            await join_game(third_sid, {"game_pin": game_pin, "username": username, "captcha": "", "custom_field": ""})
            seen["rejoin_by_code"] = _events(emit)
        return seen

    # Run on the app's own event loop so the Redis connections are shared.
    seen = test_client.portal.call(scenario)

    assert "joined_game" in seen["join"], seen
    assert "rejoined_game" in seen["rejoin"], seen
    assert "rejoin_rejected" not in seen["rejoin"], seen
    assert "joined_game" in seen["rejoin_by_code"], seen
    assert "join_error" not in seen["rejoin_by_code"], seen
