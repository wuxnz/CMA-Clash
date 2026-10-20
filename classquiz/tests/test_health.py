# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

from classquiz.tests import test_client  # noqa: F401


def test_health_endpoint(test_client):  # noqa: F811
    resp = test_client.get("/api/v1/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
