# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from classquiz.auth import get_current_user
from classquiz.battle.service import (
    create_battle_lobby,
    enqueue_matchmaking,
    get_battle_lobby,
    join_battle_lobby,
    start_battle_game,
)
from classquiz.db.cma_models import Certification, LeaderboardScore, Topic, UserGamificationProfile, UserTopicStat
from classquiz.db.models import Quiz, User
from classquiz.gamification.service import accuracy_percent, get_or_create_profile, level_from_xp, xp_for_level

router = APIRouter()


class CertificationOut(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    description: str | None
    sort_order: int


class TopicOut(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    description: str | None
    certification_id: uuid.UUID | None
    sort_order: int


class QuizBrowseItem(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None
    difficulty: str | None
    topic_id: uuid.UUID | None
    certification_id: uuid.UUID | None
    question_count: int
    plays: int


class GamificationProfileOut(BaseModel):
    total_xp: int
    level: int
    xp_to_next_level: int
    current_streak_days: int
    longest_streak_days: int
    battles_won: int
    battles_played: int
    questions_answered: int
    questions_correct: int
    accuracy_percent: float


class LeaderboardEntryOut(BaseModel):
    rank: int
    user_id: uuid.UUID
    username: str
    xp: int
    level: int


class CreateBattleBody(BaseModel):
    quiz_id: uuid.UUID
    max_players: int = Field(default=4, ge=2, le=8)
    certification_slug: str | None = None


class BattleLobbyOut(BaseModel):
    battle_code: str
    quiz_id: str
    host_user_id: str
    max_players: int
    player_slots: list[dict]
    status: str
    game_pin: str | None = None
    game_id: str | None = None


@router.get("/certifications", response_model=list[CertificationOut])
async def list_certifications():
    return await Certification.objects.order_by("sort_order").all()


@router.get("/topics", response_model=list[TopicOut])
async def list_topics(certification_slug: str | None = None):
    if certification_slug:
        cert = await Certification.objects.get_or_none(slug=certification_slug)
        if cert is None:
            raise HTTPException(status_code=404, detail="certification not found")
        return await Topic.objects.filter(certification=cert.id).order_by("sort_order").all()
    return await Topic.objects.order_by("sort_order").all()


@router.get("/quizzes", response_model=list[QuizBrowseItem])
async def browse_quizzes(
    certification_slug: str | None = None,
    topic_slug: str | None = None,
    difficulty: str | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    qs = Quiz.objects.filter(public=True)
    if certification_slug:
        cert = await Certification.objects.get_or_none(slug=certification_slug)
        if cert is None:
            raise HTTPException(status_code=404, detail="certification not found")
        qs = qs.filter(certification_id=cert.id)
    if topic_slug:
        topic = await Topic.objects.get_or_none(slug=topic_slug)
        if topic is None:
            raise HTTPException(status_code=404, detail="topic not found")
        qs = qs.filter(topic_id=topic.id)
    if difficulty:
        qs = qs.filter(difficulty=difficulty)
    quizzes = await qs.order_by(Quiz.updated_at.desc()).paginate(page, page_size=page_size).all()
    return [
        QuizBrowseItem(
            id=q.id,
            title=q.title,
            description=q.description,
            difficulty=q.difficulty,
            topic_id=q.topic_id,
            certification_id=q.certification_id,
            question_count=len(q.questions),
            plays=q.plays,
        )
        for q in quizzes
    ]


@router.get("/me/gamification", response_model=GamificationProfileOut)
async def my_gamification(user: User = Depends(get_current_user)):
    profile = await get_or_create_profile(user.id)
    next_level_xp = xp_for_level(profile.level + 1)
    return GamificationProfileOut(
        total_xp=profile.total_xp,
        level=profile.level,
        xp_to_next_level=max(0, next_level_xp - profile.total_xp),
        current_streak_days=profile.current_streak_days,
        longest_streak_days=profile.longest_streak_days,
        battles_won=profile.battles_won,
        battles_played=profile.battles_played,
        questions_answered=profile.questions_answered,
        questions_correct=profile.questions_correct,
        accuracy_percent=accuracy_percent(profile.questions_correct, profile.questions_answered),
    )


@router.get("/me/stats/by-topic")
async def my_topic_stats(user: User = Depends(get_current_user)):
    stats = await UserTopicStat.objects.filter(user_id=user.id).all()
    result = []
    for s in stats:
        topic = await Topic.objects.get_or_none(id=s.topic_id)
        result.append(
            {
                "topic_slug": topic.slug if topic else None,
                "topic_name": topic.name if topic else None,
                "questions_answered": s.questions_answered,
                "questions_correct": s.questions_correct,
                "accuracy_percent": accuracy_percent(s.questions_correct, s.questions_answered),
                "xp_earned": s.xp_earned,
            }
        )
    return result


@router.get("/leaderboards", response_model=list[LeaderboardEntryOut])
async def get_leaderboard(
    period: Literal["all_time", "weekly"] = "all_time",
    certification_slug: str | None = None,
    limit: int = Query(50, ge=1, le=100),
):
    from datetime import date

    cert_id = None
    if certification_slug:
        cert = await Certification.objects.get_or_none(slug=certification_slug)
        if cert is None:
            raise HTTPException(status_code=404, detail="certification not found")
        cert_id = cert.id
    if period == "weekly":
        year, week, _ = date.today().isocalendar()
        period_key = f"{year}-W{week:02d}"
    else:
        period_key = "global"
    scores = (
        await LeaderboardScore.objects.filter(
            period=period,
            period_key=period_key,
            certification_id=cert_id,
        )
        .order_by("-xp")
        .limit(limit)
        .all()
    )
    entries: list[LeaderboardEntryOut] = []
    for rank, row in enumerate(scores, start=1):
        u = await User.objects.get_or_none(id=row.user_id)
        if u is None:
            continue
        profile = await UserGamificationProfile.objects.get_or_none(user_id=row.user_id)
        level = profile.level if profile else level_from_xp(row.xp)
        entries.append(
            LeaderboardEntryOut(rank=rank, user_id=row.user_id, username=u.username, xp=row.xp, level=level)
        )
    return entries


@router.post("/battles", response_model=BattleLobbyOut)
async def api_create_battle(body: CreateBattleBody, user: User = Depends(get_current_user)):
    quiz = await Quiz.objects.get_or_none(id=body.quiz_id, public=True)
    if quiz is None:
        quiz = await Quiz.objects.get_or_none(id=body.quiz_id, user_id=user.id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="quiz not found")
    lobby = await create_battle_lobby(user, quiz.id, body.max_players, body.certification_slug)
    return BattleLobbyOut(**lobby.model_dump())


@router.post("/battles/{battle_code}/join", response_model=BattleLobbyOut)
async def api_join_battle(battle_code: str, user: User = Depends(get_current_user)):
    try:
        lobby = await join_battle_lobby(battle_code, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return BattleLobbyOut(**lobby.model_dump())


@router.get("/battles/{battle_code}", response_model=BattleLobbyOut)
async def api_get_battle(battle_code: str):
    lobby = await get_battle_lobby(battle_code)
    if lobby is None:
        raise HTTPException(status_code=404, detail="battle not found")
    return BattleLobbyOut(**lobby.model_dump())


@router.post("/battles/{battle_code}/start", response_model=BattleLobbyOut)
async def api_start_battle(battle_code: str, user: User = Depends(get_current_user)):
    try:
        lobby = await start_battle_game(battle_code, user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return BattleLobbyOut(**lobby.model_dump())


@router.post("/matchmaking/queue")
async def api_matchmaking_queue(certification_slug: str, user: User = Depends(get_current_user)):
    game_pin = await enqueue_matchmaking(user, certification_slug)
    return {"status": "queued" if game_pin is None else "matched", "game_pin": game_pin}
