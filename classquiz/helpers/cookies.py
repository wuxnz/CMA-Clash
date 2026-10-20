# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.config import settings


def auth_cookie_kwargs() -> dict:
    s = settings()
    if s.cookie_cross_site:
        return {"httponly": True, "samesite": "none", "secure": True}
    return {"httponly": True, "samesite": "lax", "secure": s.cookie_secure}
