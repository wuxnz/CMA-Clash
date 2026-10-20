# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.config import settings


def auth_cookie_kwargs() -> dict:
    """
    Cookie flags for auth tokens.

    Use cross-site cookies when the browser talks to the API on a different origin
    (no reverse proxy). Same-origin setups (Caddy or Vercel rewrites) should keep
    the default lax cookies.
    """
    s = settings()
    if s.cookie_cross_site:
        return {"httponly": True, "samesite": "none", "secure": True}
    return {"httponly": True, "samesite": "lax", "secure": s.cookie_secure}
