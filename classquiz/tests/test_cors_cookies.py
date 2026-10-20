# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.helpers.cookies import auth_cookie_kwargs


def test_auth_cookie_kwargs_default():
    flags = auth_cookie_kwargs()
    assert flags["httponly"] is True
    assert flags["samesite"] == "lax"


def test_auth_cookie_kwargs_cross_site(monkeypatch):
    from classquiz.config import settings as settings_factory

    class _Settings:
        cookie_cross_site = True
        cookie_secure = False

    monkeypatch.setattr("classquiz.helpers.cookies.settings", lambda: _Settings())
    flags = auth_cookie_kwargs()
    assert flags["samesite"] == "none"
    assert flags["secure"] is True
