# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import uuid

import pytest
from fastapi.testclient import TestClient

import classquiz.auth as auth_module
from classquiz.db.cma_models import UserGamificationProfile, XpEvent
from classquiz.db.models import User
from classquiz.tests import test_client  # noqa: F401

pytestmark = pytest.mark.order("last")


def _log_in_admin(tc: TestClient, email: str, password: str) -> None:
    from classquiz.tests.test_server import TestUsers

    resp = tc.post("/api/v1/login/start", json={"email": email})
    assert resp.status_code == 200
    login = tc.post(
        "/api/v1/login/finish",
        json={"email": email, "password": password, "token": resp.json()["token"]},
    )
    assert login.status_code == 200
    TestUsers.apply_cookies(tc, login.cookies)


class TestAdminEmails:
    @pytest.mark.asyncio
    async def test_user_is_site_admin_from_admin_emails(self, monkeypatch):
        class _User:
            email = "listed-admin@example.com"
            id = uuid.uuid4()

        monkeypatch.setattr(auth_module.settings, "admin_emails", "Listed-Admin@Example.com,other@x.com")
        assert await auth_module.user_is_site_admin(_User()) is True

    def test_admin_emails_grants_delete_access(self, test_client: TestClient, monkeypatch):
        from classquiz.config import settings

        victim_email = f"victim-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/register",
            json={
                "email": victim_email,
                "username": f"victim-{uuid.uuid4().hex[:8]}",
                "password": "victim-pass-123",
            },
        )
        secret = settings().secret_key
        test_client.get(f"/api/v1/internal/testing/user/{victim_email}?secret_key={secret}")
        test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={victim_email}&amount=10&secret_key={secret}"
        )

        admin_email = f"extra-admin-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/register",
            json={
                "email": admin_email,
                "username": f"extra-admin-{uuid.uuid4().hex[:8]}",
                "password": "admin-pass-123",
            },
        )
        test_client.get(f"/api/v1/internal/testing/user/{admin_email}?secret_key={secret}")

        monkeypatch.setattr(auth_module.settings, "admin_emails", admin_email)
        _log_in_admin(test_client, admin_email, "admin-pass-123")

        delete_resp = test_client.delete(f"/api/v1/admin/user/email?email={victim_email}")
        assert delete_resp.status_code == 200
        assert delete_resp.json()["deleted"] == 1

    @pytest.mark.asyncio
    async def test_admin_delete_removes_gamification_rows(self, test_client: TestClient):
        from classquiz.config import settings

        email = f"del-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/register",
            json={
                "email": email,
                "username": f"del-{uuid.uuid4().hex[:8]}",
                "password": "del-pass-123",
            },
        )
        secret = settings().secret_key
        user = await User.objects.get(email=email)
        test_client.post(
            f"/api/v1/internal/testing/gamification/award-xp?email={email}&amount=15&secret_key={secret}"
        )
        assert await UserGamificationProfile.objects.get_or_none(user_id=user.id) is not None
        assert await XpEvent.objects.filter(user_id=user.id).count() > 0

        from classquiz.tests.test_server import TestUsers

        TestUsers.ensure_logged_in(test_client)
        resp = test_client.delete(f"/api/v1/admin/user/email?email={email}")
        assert resp.status_code == 200
        assert await UserGamificationProfile.objects.get_or_none(user_id=user.id) is None
        assert await XpEvent.objects.filter(user_id=user.id).count() == 0


class TestAdminApi:
    def test_admin_me_forbidden_for_non_admin(self, test_client: TestClient):
        from classquiz.tests.test_server import TestUsers

        TestUsers.ensure_logged_in(test_client)
        resp = test_client.get("/api/v1/admin/me")
        assert resp.status_code == 403

    def test_admin_me_ok_for_listed_admin(self, test_client: TestClient, monkeypatch):
        from classquiz.config import settings

        admin_email = f"api-admin-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/register",
            json={
                "email": admin_email,
                "username": f"api-admin-{uuid.uuid4().hex[:8]}",
                "password": "admin-pass-123",
            },
        )
        secret = settings().secret_key
        test_client.get(f"/api/v1/internal/testing/user/{admin_email}?secret_key={secret}")
        monkeypatch.setattr(auth_module.settings, "admin_emails", admin_email)
        _log_in_admin(test_client, admin_email, "admin-pass-123")

        resp = test_client.get("/api/v1/admin/me")
        assert resp.status_code == 200
        assert resp.json()["email"] == admin_email

    def test_admin_users_list_and_search(self, test_client: TestClient, monkeypatch):
        from classquiz.config import settings
        from classquiz.tests import test_user_email

        admin_email = f"list-admin-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/register",
            json={
                "email": admin_email,
                "username": f"list-admin-{uuid.uuid4().hex[:8]}",
                "password": "admin-pass-123",
            },
        )
        secret = settings().secret_key
        test_client.get(f"/api/v1/internal/testing/user/{admin_email}?secret_key={secret}")
        monkeypatch.setattr(auth_module.settings, "admin_emails", admin_email)
        _log_in_admin(test_client, admin_email, "admin-pass-123")

        denied = test_client.get("/api/v1/admin/users")
        assert denied.status_code == 200
        payload = denied.json()
        assert "items" in payload
        assert payload["page_size"] <= 50

        search = test_client.get("/api/v1/admin/users", params={"q": test_user_email.split("@")[0]})
        assert search.status_code == 200
        emails = [row["email"] for row in search.json()["items"]]
        assert test_user_email in emails

    def test_users_me_includes_is_site_admin(self, test_client: TestClient, monkeypatch):
        from classquiz.config import settings
        from classquiz.tests import test_user_email, test_user_password
        from classquiz.tests.test_server import TestUsers

        TestUsers.log_in(test_client, test_user_email, test_user_password)
        resp = test_client.get("/api/v1/users/me")
        assert resp.status_code == 200
        body = resp.json()
        assert "is_site_admin" in body
        assert body["is_site_admin"] is False

        monkeypatch.setattr(auth_module.settings, "admin_emails", test_user_email)
        resp2 = test_client.get("/api/v1/users/me")
        assert resp2.json()["is_site_admin"] is True

    @pytest.mark.asyncio
    async def test_admin_delete_user_by_id_minimal_user(self, test_client: TestClient, monkeypatch):
        from classquiz.config import settings
        from classquiz.db.models import User

        victim_email = f"del-id-{uuid.uuid4().hex[:8]}@example.com"
        victim_username = f"delid{uuid.uuid4().hex[:6]}"
        test_client.post(
            "/api/v1/users/create",
            json={
                "email": victim_email,
                "username": victim_username,
                "password": "delete-me-12",
            },
        )
        victim = test_client.get(
            f"/api/v1/internal/testing/user/{victim_email}?secret_key={settings().secret_key}"
        ).json()
        victim_id = victim["id"]

        admin_email = f"del-admin-{uuid.uuid4().hex[:8]}@example.com"
        test_client.post(
            "/api/v1/users/create",
            json={
                "email": admin_email,
                "username": f"deladmin{uuid.uuid4().hex[:6]}",
                "password": "admin-pass-123",
            },
        )
        test_client.get(f"/api/v1/internal/testing/user/{admin_email}?secret_key={settings().secret_key}")
        monkeypatch.setattr(auth_module.settings, "admin_emails", admin_email)
        _log_in_admin(test_client, admin_email, "admin-pass-123")

        resp = test_client.delete(f"/api/v1/admin/user/id?user_id={victim_id}")
        assert resp.status_code == 200
        assert resp.json()["deleted"] == 1
        assert await User.objects.get_or_none(id=uuid.UUID(victim_id)) is None
