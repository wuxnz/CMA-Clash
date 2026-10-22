# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from pydantic import BaseModel, Field

from classquiz.auth import get_current_user, get_current_user_optional
from classquiz.battle.service import (
    create_battle_lobby,
    create_battle_lobby_guest,
    enqueue_matchmaking,
    get_battle_lobby,
    join_battle_lobby,
    join_battle_lobby_guest,
    start_battle_game,
)
from classquiz.rate_limit import rate_limit_request
from classquiz.db.cma_models import Certification, Topic, UserTopicStat
from classquiz.db.models import Quiz, User
from classquiz.gamification.leaderboard import build_leaderboard_entries
from classquiz.gamification.service import accuracy_percent, get_or_create_profile, level_from_xp, xp_for_level

router = APIRouter()


class CertificationOut(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    description: str | None
    sort_order: int


class StudyBlockOut(BaseModel):
    """A single study-guide section with its authoritative source."""

    title: str
    summary: str
    url: str
    source: str | None = None
    bullets: list[str] | None = None


class TopicOut(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    description: str | None
    study_content: list[StudyBlockOut] | None = None
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
    questions_per_game: int | None = None
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
    is_you: bool = False


class CreateBattleBody(BaseModel):
    quiz_id: uuid.UUID
    max_players: int = Field(default=4, ge=2, le=8)
    certification_slug: str | None = None
    display_name: str | None = Field(default=None, max_length=32)


class JoinBattleBody(BaseModel):
    display_name: str | None = Field(default=None, max_length=32)
    guest_player_id: str | None = None


class StartBattleBody(BaseModel):
    host_secret: str | None = None


class BattleLobbyOut(BaseModel):
    battle_code: str
    quiz_id: str
    host_user_id: str
    max_players: int
    player_slots: list[dict]
    status: str
    game_pin: str | None = None
    game_id: str | None = None
    host_secret: str | None = None
    guest_player_id: str | None = None


@router.get("/certifications", response_model=list[CertificationOut])
async def list_certifications():
    return await Certification.objects.order_by("sort_order").all()


def _certification_id(topic: Topic) -> uuid.UUID | None:
    """Read the certification primary key from an ormar relation.

    `Topic.certification` is a ForeignKey, so ormar exposes the related model
    (lazily loaded, primary key only) instead of a `certification_id` attribute.
    """
    cert = getattr(topic, "certification", None)
    if cert is None:
        return None
    if isinstance(cert, uuid.UUID):
        return cert
    return getattr(cert, "id", None)


_UNSET = object()


def _topic_out(topic: Topic, certification_id: object = _UNSET) -> TopicOut:
    """Build the topic payload explicitly.

    Returning the ormar model directly makes FastAPI validate against the
    response model, which fails for the `certification` relation because the
    model has no `certification_id` attribute.
    """
    cert_id = _certification_id(topic) if certification_id is _UNSET else certification_id
    return TopicOut(
        id=topic.id,
        slug=topic.slug,
        name=topic.name,
        description=topic.description,
        study_content=topic.study_content,
        certification_id=cert_id,
        sort_order=topic.sort_order,
    )


@router.get("/topics/{topic_slug}", response_model=TopicOut)
async def get_topic(topic_slug: str):
    topic = await Topic.objects.get_or_none(slug=topic_slug)
    if topic is None:
        raise HTTPException(status_code=404, detail="topic not found")
    return _topic_out(topic)


@router.get("/topics", response_model=list[TopicOut])
async def list_topics(certification_slug: str | None = None):
    if certification_slug:
        cert = await Certification.objects.get_or_none(slug=certification_slug)
        if cert is None:
            raise HTTPException(status_code=404, detail="certification not found")
        topics = await Topic.objects.filter(certification=cert.id).order_by("sort_order").all()
        return [_topic_out(topic, certification_id=cert.id) for topic in topics]
    return [_topic_out(topic) for topic in await Topic.objects.order_by("sort_order").all()]


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
            questions_per_game=q.questions_per_game,
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
    user: User | None = Depends(get_current_user_optional),
):
    cert_id = None
    if certification_slug:
        cert = await Certification.objects.get_or_none(slug=certification_slug)
        if cert is None:
            raise HTTPException(status_code=404, detail="certification not found")
        cert_id = cert.id
    viewer_id = user.id if user is not None else None
    raw = await build_leaderboard_entries(period, cert_id, limit, viewer_id=viewer_id)
    return [LeaderboardEntryOut(**row) for row in raw]


class PracticeXpBody(BaseModel):
    quiz_id: uuid.UUID
    correct: bool


@router.post("/me/practice/answer")
async def practice_answer_xp(body: PracticeXpBody, user: User = Depends(get_current_user)):
    from classquiz.gamification.service import record_answer_stats

    quiz = await Quiz.objects.get_or_none(id=body.quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="quiz not found")
    await record_answer_stats(
        user.id,
        quiz.topic_id,
        body.correct,
        certification_id=quiz.certification_id,
    )
    return {"ok": True}


def _lobby_out(lobby, guest_player_id: str | None = None, include_host_secret: bool = False) -> BattleLobbyOut:
    data = lobby.model_dump()
    if not include_host_secret:
        data["host_secret"] = None
    return BattleLobbyOut(**data, guest_player_id=guest_player_id)


@router.post("/battles", response_model=BattleLobbyOut)
async def api_create_battle(
    request: Request,
    body: CreateBattleBody,
    user: User | None = Depends(get_current_user_optional),
):
    quiz = await Quiz.objects.get_or_none(id=body.quiz_id, public=True)
    if quiz is None:
        if user is None:
            raise HTTPException(status_code=404, detail="quiz not found")
        quiz = await Quiz.objects.get_or_none(id=body.quiz_id, user_id=user.id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="quiz not found")
    if user is None:
        await rate_limit_request(request, "battle_create_anon", limit=20, window_sec=3600)
        try:
            lobby = await create_battle_lobby_guest(quiz.id, body.max_players, body.certification_slug)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return _lobby_out(lobby, include_host_secret=True)
    lobby = await create_battle_lobby(user, quiz.id, body.max_players, body.certification_slug)
    return _lobby_out(lobby)


@router.post("/battles/{battle_code}/join", response_model=BattleLobbyOut)
async def api_join_battle(
    battle_code: str,
    body: JoinBattleBody | None = None,
    user: User | None = Depends(get_current_user_optional),
):
    if user is not None:
        try:
            lobby = await join_battle_lobby(battle_code, user)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return _lobby_out(lobby)
    if body is None or not body.display_name or len(body.display_name.strip()) < 2:
        raise HTTPException(status_code=400, detail="display_name required for guest join")
    try:
        lobby, guest_id = await join_battle_lobby_guest(
            battle_code, body.display_name, body.guest_player_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return _lobby_out(lobby, guest_player_id=guest_id)


@router.get("/battles/{battle_code}", response_model=BattleLobbyOut)
async def api_get_battle(battle_code: str):
    lobby = await get_battle_lobby(battle_code)
    if lobby is None:
        raise HTTPException(status_code=404, detail="battle not found")
    return _lobby_out(lobby)


@router.post("/battles/{battle_code}/start", response_model=BattleLobbyOut)
async def api_start_battle(
    battle_code: str,
    body: StartBattleBody | None = None,
    user: User | None = Depends(get_current_user_optional),
):
    host_secret = body.host_secret if body else None
    user_id = user.id if user is not None else None
    try:
        lobby = await start_battle_game(battle_code, user_id, host_secret=host_secret)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return _lobby_out(lobby)


@router.post("/matchmaking/queue")
async def api_matchmaking_queue(certification_slug: str, user: User = Depends(get_current_user)):
    game_pin = await enqueue_matchmaking(user, certification_slug)
    return {"status": "queued" if game_pin is None else "matched", "game_pin": game_pin}
