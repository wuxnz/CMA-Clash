# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta
from typing import Literal

from classquiz.db import database
from classquiz.db.cma_models import LeaderboardScore, UserGamificationProfile
from classquiz.db.models import User
from classquiz.gamification.service import level_from_xp


def _iso_week_key(d: date | None = None) -> str:
    d = d or date.today()
    year, week, _ = d.isocalendar()
    return f"{year}-W{week:02d}"


def _week_start_dt(d: date | None = None) -> datetime:
    d = d or date.today()
    monday = d - timedelta(days=d.weekday())
    return datetime.combine(monday, datetime.min.time())


async def _ranked_from_profiles(
    limit: int,
    certification_id: uuid.UUID | None,
) -> list[tuple[uuid.UUID, int, int]]:
    """Return (user_id, xp, level) rows ordered by xp desc."""
    if certification_id is None:
        rows = await database.fetch_all(
            """
            SELECT p.user_id, p.total_xp AS xp, p.level
            FROM user_gamification_profiles p
            INNER JOIN users u ON u.id = p.user_id
            WHERE p.total_xp > 0
            ORDER BY p.total_xp DESC, p.user_id
            LIMIT :limit
            """,
            {"limit": limit},
        )
    else:
        rows = await database.fetch_all(
            """
            SELECT e.user_id, SUM(e.amount) AS xp, MAX(p.level) AS level
            FROM xp_events e
            INNER JOIN users u ON u.id = e.user_id
            LEFT JOIN user_gamification_profiles p ON p.user_id = e.user_id
            WHERE e.certification_id = :cert_id
            GROUP BY e.user_id
            HAVING SUM(e.amount) > 0
            ORDER BY xp DESC, e.user_id
            LIMIT :limit
            """,
            {"cert_id": certification_id, "limit": limit},
        )
    out: list[tuple[uuid.UUID, int, int]] = []
    for row in rows:
        xp = int(row["xp"] or 0)
        level = int(row["level"] or level_from_xp(xp))
        out.append((uuid.UUID(str(row["user_id"])), xp, level))
    return out


async def _ranked_from_weekly_events(
    limit: int,
    certification_id: uuid.UUID | None,
    week_start: datetime,
) -> list[tuple[uuid.UUID, int, int]]:
    cert_clause = ""
    params: dict = {"week_start": week_start, "limit": limit}
    if certification_id is not None:
        cert_clause = "AND e.certification_id = :cert_id"
        params["cert_id"] = certification_id
    rows = await database.fetch_all(
        f"""
        SELECT e.user_id, SUM(e.amount) AS xp, MAX(p.level) AS level
        FROM xp_events e
        INNER JOIN users u ON u.id = e.user_id
        LEFT JOIN user_gamification_profiles p ON p.user_id = e.user_id
        WHERE e.created_at >= :week_start
        {cert_clause}
        GROUP BY e.user_id
        HAVING SUM(e.amount) > 0
        ORDER BY xp DESC, e.user_id
        LIMIT :limit
        """,
        params,
    )
    out: list[tuple[uuid.UUID, int, int]] = []
    for row in rows:
        xp = int(row["xp"] or 0)
        level = int(row["level"] or level_from_xp(xp))
        out.append((uuid.UUID(str(row["user_id"])), xp, level))
    return out


async def _ranked_from_all_time_events(
    limit: int,
    certification_id: uuid.UUID | None,
) -> list[tuple[uuid.UUID, int, int]]:
    cert_clause = ""
    params: dict = {"limit": limit}
    if certification_id is not None:
        cert_clause = "AND e.certification_id = :cert_id"
        params["cert_id"] = certification_id
    rows = await database.fetch_all(
        f"""
        SELECT e.user_id, SUM(e.amount) AS xp, MAX(p.level) AS level
        FROM xp_events e
        INNER JOIN users u ON u.id = e.user_id
        LEFT JOIN user_gamification_profiles p ON p.user_id = e.user_id
        WHERE 1=1
        {cert_clause}
        GROUP BY e.user_id
        HAVING SUM(e.amount) > 0
        ORDER BY xp DESC, e.user_id
        LIMIT :limit
        """,
        params,
    )
    out: list[tuple[uuid.UUID, int, int]] = []
    for row in rows:
        xp = int(row["xp"] or 0)
        level = int(row["level"] or level_from_xp(xp))
        out.append((uuid.UUID(str(row["user_id"])), xp, level))
    return out


async def _ranked_from_leaderboard_scores_aggregate(
    limit: int,
    certification_id: uuid.UUID | None,
) -> list[tuple[uuid.UUID, int, int]]:
    cert_clause = ""
    params: dict = {"limit": limit}
    if certification_id is not None:
        cert_clause = "AND ls.certification_id = :cert_id"
        params["cert_id"] = certification_id
    rows = await database.fetch_all(
        f"""
        SELECT ls.user_id, SUM(ls.xp) AS xp, MAX(p.level) AS level
        FROM leaderboard_scores ls
        INNER JOIN users u ON u.id = ls.user_id
        LEFT JOIN user_gamification_profiles p ON p.user_id = ls.user_id
        WHERE ls.period = 'all_time'
        {cert_clause}
        GROUP BY ls.user_id
        HAVING SUM(ls.xp) > 0
        ORDER BY xp DESC, ls.user_id
        LIMIT :limit
        """,
        params,
    )
    out: list[tuple[uuid.UUID, int, int]] = []
    for row in rows:
        xp = int(row["xp"] or 0)
        level = int(row["level"] or level_from_xp(xp))
        out.append((uuid.UUID(str(row["user_id"])), xp, level))
    return out


async def _ranked_from_leaderboard_scores(
    period: Literal["all_time", "weekly"],
    period_key: str,
    certification_id: uuid.UUID | None,
    limit: int,
) -> list[tuple[uuid.UUID, int, int]]:
    qs = LeaderboardScore.objects.filter(period=period, period_key=period_key)
    if certification_id is None:
        qs = qs.filter(certification_id__isnull=True)
    else:
        qs = qs.filter(certification_id=certification_id)
    scores = await qs.order_by("-xp").limit(limit).all()
    out: list[tuple[uuid.UUID, int, int]] = []
    for row in scores:
        profile = await UserGamificationProfile.objects.get_or_none(user_id=row.user_id)
        level = profile.level if profile else level_from_xp(row.xp)
        out.append((row.user_id, row.xp, level))
    return out


async def fetch_leaderboard_rows(
    period: Literal["all_time", "weekly"],
    certification_id: uuid.UUID | None,
    limit: int,
) -> list[tuple[uuid.UUID, int, int]]:
    if period == "weekly":
        rows = await _ranked_from_weekly_events(limit, certification_id, _week_start_dt())
        if rows:
            return rows
        period_key = _iso_week_key()
        return await _ranked_from_leaderboard_scores(period, period_key, certification_id, limit)

    for loader in (
        lambda: _ranked_from_profiles(limit, certification_id),
        lambda: _ranked_from_all_time_events(limit, certification_id),
        lambda: _ranked_from_leaderboard_scores_aggregate(limit, certification_id),
        lambda: _ranked_from_leaderboard_scores(period, "global", certification_id, limit),
    ):
        rows = await loader()
        if rows:
            return rows
    return []


async def viewer_rank_row(
    viewer_id: uuid.UUID,
    period: Literal["all_time", "weekly"],
    certification_id: uuid.UUID | None,
) -> tuple[int, int, int] | None:
    """Return (rank, xp, level) for viewer, or None if they have no XP in this board."""
    if period == "all_time" and certification_id is None:
        row = await database.fetch_one(
            """
            SELECT p.total_xp AS xp, p.level
            FROM user_gamification_profiles p
            INNER JOIN users u ON u.id = p.user_id
            WHERE p.user_id = :user_id AND p.total_xp > 0
            """,
            {"user_id": viewer_id},
        )
        if row is None:
            return None
        xp = int(row["xp"])
        level = int(row["level"])
        higher = await database.fetch_val(
            """
            SELECT COUNT(*) FROM user_gamification_profiles p
            INNER JOIN users u ON u.id = p.user_id
            WHERE p.total_xp > :xp
            """,
            {"xp": xp},
        )
        return int(higher or 0) + 1, xp, level

    if period == "weekly":
        week_start = _week_start_dt()
        cert_clause = ""
        params: dict = {"user_id": viewer_id, "week_start": week_start}
        if certification_id is not None:
            cert_clause = "AND e.certification_id = :cert_id"
            params["cert_id"] = certification_id
        row = await database.fetch_one(
            f"""
            SELECT SUM(e.amount) AS xp, MAX(p.level) AS level
            FROM xp_events e
            LEFT JOIN user_gamification_profiles p ON p.user_id = e.user_id
            WHERE e.user_id = :user_id AND e.created_at >= :week_start
            {cert_clause}
            """,
            params,
        )
        if row is None or int(row["xp"] or 0) <= 0:
            return None
        xp = int(row["xp"])
        level = int(row["level"] or level_from_xp(xp))
        higher = await database.fetch_val(
            f"""
            SELECT COUNT(*) FROM (
                SELECT e.user_id, SUM(e.amount) AS xp
                FROM xp_events e
                INNER JOIN users u ON u.id = e.user_id
                WHERE e.created_at >= :week_start
                {cert_clause}
                GROUP BY e.user_id
                HAVING SUM(e.amount) > :xp
            ) sub
            """,
            {**params, "xp": xp},
        )
        return int(higher or 0) + 1, xp, level

    return None


async def build_leaderboard_entries(
    period: Literal["all_time", "weekly"],
    certification_id: uuid.UUID | None,
    limit: int,
    viewer_id: uuid.UUID | None = None,
) -> list[dict]:
    rows = await fetch_leaderboard_rows(period, certification_id, limit)
    entries: list[dict] = []
    seen: set[uuid.UUID] = set()
    for rank, (user_id, xp, level) in enumerate(rows, start=1):
        u = await User.objects.get_or_none(id=user_id)
        if u is None:
            continue
        seen.add(user_id)
        entries.append(
            {
                "rank": rank,
                "user_id": user_id,
                "username": u.username,
                "xp": xp,
                "level": level,
                "is_you": viewer_id == user_id,
            }
        )

    if viewer_id is not None and viewer_id not in seen:
        viewer = await viewer_rank_row(viewer_id, period, certification_id)
        if viewer is not None:
            rank, xp, level = viewer
            u = await User.objects.get_or_none(id=viewer_id)
            if u is not None:
                entries.append(
                    {
                        "rank": rank,
                        "user_id": viewer_id,
                        "username": u.username,
                        "xp": xp,
                        "level": level,
                        "is_you": True,
                    }
                )
    return entries
