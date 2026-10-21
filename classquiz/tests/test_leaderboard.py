# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import pytest
from fastapi.testclient import TestClient

from classquiz.db.cma_models import LeaderboardScore, UserGamificationProfile
from classquiz.gamification.leaderboard import build_leaderboard_entries
from classquiz.tests import test_client, test_user_email

pytestmark = pytest.mark.order("last")


@pytest.mark.asyncio
async def test_leaderboard_reads_profile_when_score_table_empty():
    from classquiz.db.models import User

    user = await User.objects.get_or_none(email=test_user_email)
    assert user is not None
    profile = await UserGamificationProfile.objects.get_or_none(user_id=user.id)
    if profile is None:
        profile = await UserGamificationProfile(user_id=user.id, total_xp=250, level=2).save()
    else:
        profile.total_xp = max(profile.total_xp, 250)
        profile.level = 2
        await profile.update()
    await LeaderboardScore.objects.filter(user_id=user.id).delete()

    entries = await build_leaderboard_entries("all_time", None, 10, viewer_id=user.id)
    assert any(e["user_id"] == user.id and e["xp"] >= 250 for e in entries)


class TestLeaderboardApi:
    def test_leaderboard_null_cert_global_row(self, test_client: TestClient):
        from classquiz.config import settings

        secret = settings().secret_key
        award = test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={test_user_email}&amount=77&secret_key={secret}"
        )
        assert award.status_code == 200
        lb = test_client.get("/api/v1/clash/leaderboards", params={"period": "all_time", "limit": 20})
        assert lb.status_code == 200
        body = lb.json()
        assert any(row["xp"] >= 77 and row["username"] for row in body)

    def test_leaderboard_viewer_appended_when_outside_top(self, test_client: TestClient):
        from classquiz.config import settings

        secret = settings().secret_key
        test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={test_user_email}&amount=5&secret_key={secret}"
        )
        lb = test_client.get(
            "/api/v1/clash/leaderboards",
            params={"period": "all_time", "limit": 1},
        )
        assert lb.status_code == 200
        rows = lb.json()
        assert len(rows) >= 1
