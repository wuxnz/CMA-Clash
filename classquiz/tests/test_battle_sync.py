# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import asyncio
import json

import pytest
from fastapi.testclient import TestClient


@pytest.mark.order("last")
class TestBattleSync:
    def test_guest_battle_start_marks_game_live(self, test_client: TestClient):
        from classquiz.config import redis

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
        game_pin = start.json()["game_pin"]

        async def _load_game():
            return await redis.get(f"game:{game_pin}")

        raw = asyncio.run(_load_game())
        assert raw is not None
        game = json.loads(raw)
        assert game["started"] is True
        assert game["current_question"] == 0
        assert game["question_show"] is True
