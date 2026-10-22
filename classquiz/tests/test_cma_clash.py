# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import os
import subprocess
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from classquiz.gamification.service import level_from_xp, xp_for_level
from classquiz.tests import test_client, test_user_email, test_user_password, ValueStorage

pytestmark = pytest.mark.order("last")

REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_seed() -> None:
    """Run the content seed in a subprocess (fresh event loop, same environment)."""
    env = {**os.environ, "CMA_CLASH_SKIP_SEED": ""}
    subprocess.run(
        [sys.executable, "-m", "classquiz.seed.runner"],
        check=True,
        env=env,
        cwd=str(REPO_ROOT),
    )


def _log_in(tc: TestClient) -> int:
    from classquiz.tests.test_server import TestUsers

    return TestUsers.log_in(tc)


class TestGamification:
    def test_battle_score_formula(self):
        from classquiz.socket_server import calculate_score

        assert calculate_score(0, 30) == 1000
        assert calculate_score(15000, 30) < 1000

    def test_xp_levels(self):
        assert xp_for_level(1) == 0
        assert level_from_xp(0) == 1
        assert level_from_xp(150) >= 2

    def test_award_xp_persists(self, test_client: TestClient):
        from classquiz.config import settings

        secret = settings().secret_key
        resp = test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={test_user_email}&amount=40&secret_key={secret}"
        )
        assert resp.status_code == 200
        first_xp = resp.json()["total_xp"]
        resp2 = test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={test_user_email}&amount=5&secret_key={secret}"
        )
        assert resp2.status_code == 200
        assert resp2.json()["total_xp"] == first_xp + 5


class TestClashApi:
    def test_topics_endpoint_returns_study_guides(self, test_client: TestClient):
        """The topic payload must serialize (FK relation included) and carry study content."""
        from classquiz.seed.catalog import CERTIFICATIONS

        _run_seed()
        resp = test_client.get("/api/v1/clash/topics")
        assert resp.status_code == 200, resp.text
        topics = resp.json()
        assert topics
        slugs = {topic["slug"] for topic in topics}
        expected = {slug for cert in CERTIFICATIONS for slug, _name, _order in cert["topics"]}
        assert expected.issubset(slugs)
        for topic in topics:
            assert topic["certification_id"], topic["slug"]
            for block in topic["study_content"] or []:
                assert block["title"] and block["summary"]
                assert block["url"].startswith("https://")
                assert block["source"]

    def test_single_topic_endpoint(self, test_client: TestClient):
        resp = test_client.get("/api/v1/clash/topics/ccma-diabetes")
        assert resp.status_code == 200, resp.text
        topic = resp.json()
        assert topic["slug"] == "ccma-diabetes"
        assert topic["certification_id"]
        assert len(topic["study_content"]) >= 4

    def test_certifications_and_seed(self, test_client: TestClient):
        _run_seed()
        resp = test_client.get("/api/v1/clash/certifications")
        assert resp.status_code == 200
        certs = resp.json()
        assert any(c["slug"] == "ccma" for c in certs)
        resp = test_client.get("/api/v1/clash/quizzes", params={"certification_slug": "ccma", "page_size": 50})
        assert resp.status_code == 200
        quizzes = resp.json()
        assert len(quizzes) >= 8
        from classquiz.config import settings
        from classquiz.seed.runner import SEED_USER_EMAIL

        quiz_id = quizzes[0]["id"]
        secret = settings().secret_key
        battle_script = f"""
from fastapi.testclient import TestClient
from classquiz import app as fastapi_app
from classquiz.config import settings
from classquiz.seed.runner import SEED_USER_EMAIL

secret = settings().secret_key
quiz_id = "{quiz_id}"
with TestClient(fastapi_app) as client:
    create = client.post(
        f"/api/v1/internal/testing/battle-lobby?quiz_id={{quiz_id}}&email={{SEED_USER_EMAIL}}&secret_key={{secret}}"
    )
    assert create.status_code == 200, create.text
    code = create.json()["battle_code"]
    assert client.get(f"/api/v1/clash/battles/{{code}}").status_code == 200
"""
        subprocess.run([sys.executable, "-c", battle_script], check=True, env=os.environ, cwd=str(REPO_ROOT))

    def test_leaderboard_and_profile(self, test_client: TestClient):
        from classquiz.config import settings

        secret = settings().secret_key
        award = test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={test_user_email}&amount=100&secret_key={secret}"
        )
        assert award.status_code == 200
        assert award.json()["total_xp"] >= 100
        lb = test_client.get("/api/v1/clash/leaderboards", params={"period": "all_time", "limit": 10})
        assert lb.status_code == 200
        assert any(row["xp"] >= 100 for row in lb.json())
