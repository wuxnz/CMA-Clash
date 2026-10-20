# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def _mock_outbound_email():
    """Tests run without a real SMTP server; mail is exercised via API status codes only."""
    with patch("classquiz.emails.transport.send_email"):
        yield
