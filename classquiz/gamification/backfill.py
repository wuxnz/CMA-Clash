# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""One-time safe XP sync from historical xp_events into profiles (startup)."""

from __future__ import annotations

import logging

from classquiz.config import redis
from classquiz.db import database
from classquiz.db.cma_models import UserGamificationProfile
from classquiz.gamification.service import level_from_xp

LOGGER = logging.getLogger("uvicorn.error")

# Do not mutate these accounts during backfill (read-only for leaderboard queries).
PROTECTED_EMAILS = frozenset({"demondemands@gmail.com"})

_BACKFILL_LOCK_KEY = "gamification:backfill:profiles:v1"


async def backfill_profiles_from_xp_events() -> int:
    """Raise profile.total_xp to match summed xp_events when lower. Returns users updated."""
    if await redis.get(_BACKFILL_LOCK_KEY) is not None:
        return 0

    rows = await database.fetch_all(
        """
        SELECT e.user_id, SUM(e.amount) AS xp, u.email
        FROM xp_events e
        INNER JOIN users u ON u.id = e.user_id
        GROUP BY e.user_id, u.email
        HAVING SUM(e.amount) > 0
        """
    )
    updated = 0
    for row in rows:
        email = (row["email"] or "").lower()
        if email in PROTECTED_EMAILS:
            continue
        user_id = row["user_id"]
        target_xp = int(row["xp"] or 0)
        if target_xp <= 0:
            continue
        profile = await UserGamificationProfile.objects.get_or_none(user_id=user_id)
        if profile is None:
            await UserGamificationProfile(
                user_id=user_id,
                total_xp=target_xp,
                level=level_from_xp(target_xp),
            ).save()
            updated += 1
            continue
        if profile.total_xp >= target_xp:
            continue
        profile.total_xp = target_xp
        profile.level = level_from_xp(target_xp)
        await profile.update()
        updated += 1

    await redis.set(_BACKFILL_LOCK_KEY, "1", ex=86400 * 30)
    if updated:
        LOGGER.info("Gamification backfill updated %s user profile(s) from xp_events.", updated)
    return updated
