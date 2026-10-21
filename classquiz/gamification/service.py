# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta

from classquiz.db.cma_models import (
    LeaderboardPeriod,
    LeaderboardScore,
    UserGamificationProfile,
    UserTopicStat,
    XpEvent,
    XpSource,
    BattleResult,
)
from classquiz.db.models import User


def xp_for_level(level: int) -> int:
    """XP required to reach `level` (level 1 = 0)."""
    if level <= 1:
        return 0
    return sum(100 + (n - 1) * 50 for n in range(2, level + 1))


def level_from_xp(total_xp: int) -> int:
    level = 1
    while total_xp >= xp_for_level(level + 1):
        level += 1
    return level


def _iso_week_key(d: date | None = None) -> str:
    d = d or date.today()
    year, week, _ = d.isocalendar()
    return f"{year}-W{week:02d}"


async def get_or_create_profile(user_id: uuid.UUID) -> UserGamificationProfile:
    profile = await UserGamificationProfile.objects.get_or_none(user_id=user_id)
    if profile is None:
        profile = await UserGamificationProfile(user_id=user_id).save()
    return profile


async def _bump_leaderboard(
    user_id: uuid.UUID,
    amount: int,
    certification_id: uuid.UUID | None,
) -> None:
    if await User.objects.get_or_none(id=user_id) is None:
        return
    period_key = _iso_week_key()
    for period in (LeaderboardPeriod.ALL_TIME.value, LeaderboardPeriod.WEEKLY.value):
        key = "global" if period == LeaderboardPeriod.ALL_TIME.value else period_key
        for cert_filter in (certification_id, None):
            qs = LeaderboardScore.objects.filter(
                user_id=user_id,
                period=period,
                period_key=key,
            )
            if cert_filter is None:
                qs = qs.filter(certification_id__isnull=True)
            else:
                qs = qs.filter(certification_id=cert_filter)
            existing = await qs.get_or_none()
            if existing is None:
                await LeaderboardScore(
                    user_id=user_id,
                    period=period,
                    period_key=key,
                    certification_id=cert_filter,
                    xp=amount,
                ).save()
            else:
                existing.xp += amount
                await existing.update()


async def _update_streak(profile: UserGamificationProfile) -> None:
    today = date.today()
    if profile.last_activity_date is None:
        profile.current_streak_days = 1
    elif profile.last_activity_date == today:
        return
    elif profile.last_activity_date == today - timedelta(days=1):
        profile.current_streak_days += 1
    else:
        profile.current_streak_days = 1
    profile.longest_streak_days = max(profile.longest_streak_days, profile.current_streak_days)
    profile.last_activity_date = today


async def award_xp(
    user_id: uuid.UUID,
    amount: int,
    source: XpSource | str,
    certification_id: uuid.UUID | None = None,
    topic_id: uuid.UUID | None = None,
    note: str | None = None,
) -> UserGamificationProfile:
    if amount <= 0:
        return await get_or_create_profile(user_id)
    profile = await get_or_create_profile(user_id)
    await _update_streak(profile)
    profile.total_xp += amount
    profile.level = level_from_xp(profile.total_xp)
    await profile.update()
    source_val = source.value if isinstance(source, XpSource) else source
    await XpEvent(
        user_id=user_id,
        amount=amount,
        source=source_val,
        certification_id=certification_id,
        topic_id=topic_id,
        note=note,
    ).save()
    await _bump_leaderboard(user_id, amount, certification_id)
    return profile


async def record_answer_stats(
    user_id: uuid.UUID,
    topic_id: uuid.UUID | None,
    correct: bool,
    certification_id: uuid.UUID | None = None,
) -> None:
    profile = await get_or_create_profile(user_id)
    profile.questions_answered += 1
    if correct:
        profile.questions_correct += 1
    await profile.update()
    xp_amount = 15 if correct else 3
    if topic_id is not None:
        stat = await UserTopicStat.objects.get_or_none(user_id=user_id, topic_id=topic_id)
        if stat is None:
            stat = await UserTopicStat(user_id=user_id, topic_id=topic_id).save()
        stat.questions_answered += 1
        if correct:
            stat.questions_correct += 1
        stat.xp_earned += xp_amount
        await stat.update()
    await award_xp(
        user_id,
        xp_amount,
        XpSource.CORRECT_ANSWER if correct else XpSource.QUIZ_PLAY,
        certification_id=certification_id,
        topic_id=topic_id,
    )


async def record_battle_result(
    quiz_id: uuid.UUID,
    game_id: uuid.UUID,
    scores: dict[str, int],
    user_ids: dict[str, uuid.UUID],
) -> uuid.UUID | None:
    if not scores:
        return None
    winner_name = max(scores, key=scores.get)
    winner_id = user_ids.get(winner_name)
    await BattleResult(
        quiz_id=quiz_id,
        game_id=game_id,
        winner_user_id=winner_id,
        player_scores=scores,
    ).save()
    for username, score in scores.items():
        uid = user_ids.get(username)
        if uid is None:
            continue
        if await User.objects.get_or_none(id=uid) is None:
            continue
        profile = await get_or_create_profile(uid)
        profile.battles_played += 1
        await profile.update()
        await award_xp(uid, max(10, score // 10), XpSource.BATTLE_PLAY, note=f"battle:{game_id}")
    if winner_id is not None and await User.objects.get_or_none(id=winner_id) is not None:
        profile = await get_or_create_profile(winner_id)
        profile.battles_won += 1
        await profile.update()
        await award_xp(winner_id, 50, XpSource.BATTLE_WIN, note=f"battle-win:{game_id}")
    return winner_id


def accuracy_percent(correct: int, answered: int) -> float:
    if answered == 0:
        return 0.0
    return round(100.0 * correct / answered, 1)
