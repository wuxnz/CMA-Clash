# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest
from fastapi.testclient import TestClient


@pytest.mark.order("last")
class TestAnonymousHost:
    def test_anonymous_start_public_quiz(self, test_client: TestClient):
        from classquiz.tests.test_server import TestUsers

        TestUsers.ensure_logged_in(test_client)
        quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 5}).json()
        assert quizzes
        quiz_id = quizzes[0]["id"]
        test_client.cookies.clear()
        resp = test_client.post(f"/api/v1/quiz/start/{quiz_id}?game_mode=kahoot&captcha_enabled=False")
        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body.get("game_pin")
        assert body.get("game_id")

    def test_anonymous_start_private_quiz_forbidden(self, test_client: TestClient):
        from classquiz.tests.test_server import TestUsers, ValueStorage

        TestUsers.ensure_logged_in(test_client)
        resp = test_client.post(
            f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False"
        )
        assert resp.status_code == 200
        test_client.cookies.clear()
        denied = test_client.post(
            f"/api/v1/quiz/start/{ValueStorage.quiz_id}?game_mode=kahoot&captcha_enabled=False"
        )
        assert denied.status_code == 404

    def test_guest_battle_create_and_join(self, test_client: TestClient):
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
        assert lobby.get("host_secret")
        join = test_client.post(
            f"/api/v1/clash/battles/{code}/join",
            json={"display_name": "GuestTwo"},
        )
        assert join.status_code == 200, join.text
        start = test_client.post(
            f"/api/v1/clash/battles/{code}/start",
            json={"host_secret": lobby["host_secret"]},
        )
        assert start.status_code == 200, start.text
        body = start.json()
        assert body.get("game_pin")
        assert body.get("status") == "started"
