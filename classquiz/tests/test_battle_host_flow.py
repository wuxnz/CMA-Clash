# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Battle host flow: no ghost player when guest host creates a lobby."""

import pytest
from fastapi.testclient import TestClient

from classquiz.tests import test_client  # noqa: F401


@pytest.mark.order("last")
class TestBattleHostFlow:
    def test_guest_create_lobby_has_no_players_until_join(self, test_client: TestClient):
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
        assert lobby.get("host_secret")
        assert lobby["player_slots"] == []
        assert lobby.get("guest_player_id") is None

        code = lobby["battle_code"]
        host_join = test_client.post(
            f"/api/v1/clash/battles/{code}/join",
            json={"display_name": "HostGuest"},
        )
        assert host_join.status_code == 200, host_join.text
        host_body = host_join.json()
        assert len(host_body["player_slots"]) == 1
        host_player_id = host_body["guest_player_id"]
        assert host_player_id

        rejoin = test_client.post(
            f"/api/v1/clash/battles/{code}/join",
            json={"display_name": "HostGuest", "guest_player_id": host_player_id},
        )
        assert rejoin.status_code == 200, rejoin.text
        assert len(rejoin.json()["player_slots"]) == 1

        guest_join = test_client.post(
            f"/api/v1/clash/battles/{code}/join",
            json={"display_name": "GuestTwo"},
        )
        assert guest_join.status_code == 200, guest_join.text
        assert len(guest_join.json()["player_slots"]) == 2

        start = test_client.post(
            f"/api/v1/clash/battles/{code}/start",
            json={"host_secret": lobby["host_secret"]},
        )
        assert start.status_code == 200, start.text
        assert start.json().get("game_pin")

    def test_logged_in_host_is_single_player_without_display_name(self, test_client: TestClient):
        from classquiz.tests.test_server import TestUsers

        TestUsers.ensure_logged_in(test_client)
        me = test_client.get("/api/v1/users/me").json()
        quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1}).json()
        assert quizzes
        quiz_id = quizzes[0]["id"]
        create = test_client.post(
            "/api/v1/clash/battles",
            json={"quiz_id": quiz_id, "max_players": 2},
        )
        assert create.status_code == 200, create.text
        lobby = create.json()
        assert len(lobby["player_slots"]) == 1
        assert lobby["player_slots"][0]["user_id"] == me["id"]
        assert lobby["player_slots"][0]["username"] == me["username"]

        code = lobby["battle_code"]
        again = test_client.post(f"/api/v1/clash/battles/{code}/join")
        assert again.status_code == 200, again.text
        assert len(again.json()["player_slots"]) == 1
