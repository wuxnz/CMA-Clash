# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import uuid

import pytest
from fastapi.testclient import TestClient

from classquiz.gamification.service import award_xp, get_or_create_profile, level_from_xp, xp_for_level
from classquiz.tests import test_client, test_user_email, ValueStorage
from classquiz.tests.test_server import TestUsers


class TestGamification:
    def test_battle_score_formula(self):
        from classquiz.socket_server import calculate_score

        assert calculate_score(0, 30) == 1000
        assert calculate_score(15000, 30) < 1000

    @pytest.mark.asyncio
    async def test_xp_levels(self):
        assert xp_for_level(1) == 0
        assert level_from_xp(0) == 1
        assert level_from_xp(150) >= 2

    @pytest.mark.asyncio
    async def test_award_xp_persists(self, test_client: TestClient):
        TestUsers.log_in(test_client)
        user_resp = test_client.get("/api/v1/users/me", cookies=ValueStorage.cookies)
        user_id = uuid.UUID(user_resp.json()["id"])
        from classquiz.db.cma_models import XpSource

        profile = await award_xp(user_id, 40, XpSource.QUIZ_PLAY)
        assert profile.total_xp >= 40
        again = await get_or_create_profile(user_id)
        assert again.total_xp == profile.total_xp


class TestClashApi:
    @pytest.mark.asyncio
    async def test_certifications_and_seed(self, test_client: TestClient):
        from classquiz.seed.runner import run_seed, seed_counts

        await run_seed()
        counts = await seed_counts()
        assert counts["total_questions"] >= 300
        resp = test_client.get("/api/v1/clash/certifications")
        assert resp.status_code == 200
        certs = resp.json()
        assert any(c["slug"] == "ccma" for c in certs)
        resp = test_client.get("/api/v1/clash/quizzes", params={"certification_slug": "ccma", "page_size": 5})
        assert resp.status_code == 200
        assert len(resp.json()) > 0

    @pytest.mark.asyncio
    async def test_leaderboard_and_profile(self, test_client: TestClient):
        TestUsers.log_in(test_client)
        from classquiz.db.cma_models import XpSource
        from classquiz.db.models import User

        user = await User.objects.get(email=test_user_email)
        await award_xp(user.id, 100, XpSource.QUIZ_PLAY)
        resp = test_client.get("/api/v1/clash/me/gamification", cookies=ValueStorage.cookies)
        assert resp.status_code == 200
        assert resp.json()["total_xp"] >= 100
        lb = test_client.get("/api/v1/clash/leaderboards", params={"period": "all_time", "limit": 10})
        assert lb.status_code == 200


class TestBattle:
    @pytest.mark.asyncio
    async def test_battle_lobby_flow(self, test_client: TestClient):
        from classquiz.seed.runner import run_seed

        await run_seed()
        TestUsers.log_in(test_client)
        quizzes = test_client.get("/api/v1/clash/quizzes", params={"page_size": 1}).json()
        quiz_id = quizzes[0]["id"]
        create = test_client.post("/api/v1/clash/battles", json={"quiz_id": quiz_id, "max_players": 2})
        assert create.status_code == 200
        code = create.json()["battle_code"]
        get_lobby = test_client.get(f"/api/v1/clash/battles/{code}")
        assert get_lobby.status_code == 200
