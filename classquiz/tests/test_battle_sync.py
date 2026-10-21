# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import json

import pytest
from fastapi.testclient import TestClient

from classquiz.tests import test_client  # noqa: F401


def _sync_redis():
    import redis as redis_lib

    from classquiz.config import settings

    url = str(settings().redis)
    if "?" in url:
        url = url.split("?", 1)[0]
    return redis_lib.from_url(url, decode_responses=True)


@pytest.mark.order("last")
class TestBattleSync:
    def test_guest_battle_start_defers_question_until_kickoff(self, test_client: TestClient):
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
            json={"display_name": "HostGuest"},
        )
        assert host_join.status_code == 200, host_join.text
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

        r = _sync_redis()
        raw = r.get(f"game:{game_pin}")
        assert raw is not None
        game = json.loads(raw)
        assert game["started"] is False
        assert game["current_question"] == -1
        assert r.get(f"cma_battle:kickoff:{game_pin}") is not None
