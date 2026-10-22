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


class TestSystemAccountsAreNotRanked:
    """Machine accounts must never appear on the leaderboard or occupy a rank slot."""

    @staticmethod
    def _award(test_client: TestClient, email: str, amount: int) -> None:
        from classquiz.config import settings

        test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp"
            f"?email={email}&amount={amount}&secret_key={settings().secret_key}"
        )

    def test_machine_accounts_absent_from_leaderboard(self, test_client: TestClient):
        # Give the seeded machine accounts a score that would top the board.
        self._award(test_client, "content@cmaclash.local", 100000)
        self._award(test_client, "demo@cmaclash.local", 90000)

        for period in ("all_time", "weekly"):
            lb = test_client.get(
                "/api/v1/clash/leaderboards",
                params={"period": period, "limit": 100},
            )
            assert lb.status_code == 200
            rows = lb.json()
            usernames = {row["username"] for row in rows}
            assert "cmaclash_content" not in usernames, period
            assert "demo" not in usernames, period
            # Filtered accounts must not leave holes in the ranking.
            ranks = [row["rank"] for row in rows]
            assert ranks == list(range(1, len(rows) + 1)), f"rank gap: {ranks}"

    def test_machine_account_does_not_take_a_rank_slot(self, test_client: TestClient):
        self._award(test_client, "content@cmaclash.local", 100000)
        lb = test_client.get("/api/v1/clash/leaderboards", params={"period": "all_time", "limit": 1})
        assert lb.status_code == 200
        rows = lb.json()
        assert rows, "expected at least one ranked player"
        assert rows[0]["username"] != "cmaclash_content"

    def test_is_system_account_classification(self):
        from classquiz.gamification.system_accounts import is_system_account

        assert is_system_account("content@cmaclash.local")
        assert is_system_account("demo@cmaclash.local")
        assert is_system_account("cmaclash-verify-abc@mailinator.com")
        assert is_system_account("cmae2e1@mailinator.com")
        assert is_system_account("x@demo.local")
        assert is_system_account(None, "cmaclash_content")
        assert not is_system_account("demondemands@gmail.com", "Kayvon")
        assert not is_system_account("player@gmail.com", "player")
        assert not is_system_account(None, None)

    def test_sql_predicate_matches_the_helper(self):
        from classquiz.gamification.system_accounts import (
            system_account_params,
            system_account_sql,
        )

        sql = system_account_sql("u")
        params = system_account_params()
        assert "sys_emails" in sql and "sys_usernames" in sql
        assert "content@cmaclash.local" in params["sys_emails"]
        assert "demo@cmaclash.local" in params["sys_emails"]
        assert "cmaclash_content" in params["sys_usernames"]
        assert "mailinator.com" in params["sys_email_domains"]
        assert "%s" not in sql, "the predicate must not interpolate raw values"
