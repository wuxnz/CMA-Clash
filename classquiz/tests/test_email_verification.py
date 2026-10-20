# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import uuid
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from classquiz.emails.verification import create_email_verify_token
from classquiz.routers import users as users_router
from classquiz.tests import test_client, test_user_password  # noqa: F401

pytestmark = pytest.mark.order("last")


@pytest.fixture
def unverified_user(test_client: TestClient):
    email = f"unverified-{uuid.uuid4().hex[:8]}@example.com"
    with patch.object(users_router.settings, "skip_email_verification", False):
        resp = test_client.post(
            "/api/v1/users/create",
            json={"email": email, "password": test_user_password, "username": f"u{uuid.uuid4().hex[:8]}"},
        )
    assert resp.status_code == 200
    data = resp.json()
    assert data["verified"] is False
    return {"email": email, "id": data["id"]}


def test_verify_token_roundtrip():
    from classquiz.emails.verification import decode_email_verify_token

    user_id = uuid.uuid4()
    token = create_email_verify_token(user_id)
    decoded, err = decode_email_verify_token(token)
    assert err is None
    assert decoded == user_id


def test_login_blocked_until_verified(test_client: TestClient, unverified_user: dict):
    resp = test_client.post("/api/v1/login/start", json={"email": unverified_user["email"]})
    assert resp.status_code == 403
    assert resp.json()["detail"]["code"] == "email_not_verified"


def test_verify_email_endpoint(test_client: TestClient, unverified_user: dict):
    token = create_email_verify_token(uuid.UUID(unverified_user["id"]))
    resp = test_client.post("/api/v1/users/verify-email", json={"token": token})
    assert resp.status_code == 200
    assert resp.json()["status"] == "verified"

    resp2 = test_client.post("/api/v1/users/verify-email", json={"token": token})
    assert resp2.status_code == 200
    assert resp2.json()["status"] == "already_verified"


def test_verify_email_invalid_token(test_client: TestClient):
    resp = test_client.post("/api/v1/users/verify-email", json={"token": "not-a-jwt"})
    assert resp.status_code == 400
    assert resp.json()["detail"]["code"] == "invalid_token"


def test_resend_verification_rate_limit(test_client: TestClient, unverified_user: dict):
    for _ in range(3):
        resp = test_client.post(
            "/api/v1/users/resend-verification", json={"email": unverified_user["email"]}
        )
        assert resp.status_code == 200
    resp = test_client.post("/api/v1/users/resend-verification", json={"email": unverified_user["email"]})
    assert resp.status_code == 429
    assert resp.json()["detail"]["code"] == "resend_rate_limited"
