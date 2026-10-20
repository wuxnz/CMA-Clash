# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0

from classquiz.config import settings


def test_meilisearch_api_key_setting():
    s = settings()
    assert hasattr(s, "meilisearch_api_key")
