# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import uuid
from datetime import date, datetime
from enum import Enum

import ormar
from ormar import ReferentialAction
from pydantic import BaseModel

from . import database, metadata


class DifficultyLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class LeaderboardPeriod(str, Enum):
    ALL_TIME = "all_time"
    WEEKLY = "weekly"


class XpSource(str, Enum):
    QUIZ_PLAY = "quiz_play"
    BATTLE_WIN = "battle_win"
    BATTLE_PLAY = "battle_play"
    DAILY_STREAK = "daily_streak"
    CORRECT_ANSWER = "correct_answer"


class Certification(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    slug: str = ormar.String(max_length=64, unique=True)
    name: str = ormar.String(max_length=200)
    description: str = ormar.Text(nullable=True)
    sort_order: int = ormar.Integer(default=0)

    ormar_config = ormar.OrmarConfig(
        tablename="certifications",
        metadata=metadata,
        database=database,
    )


class Topic(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    slug: str = ormar.String(max_length=96, unique=True)
    name: str = ormar.String(max_length=200)
    description: str | None = ormar.Text(nullable=True)
    study_content: list | None = ormar.JSON(nullable=True, default=None)
    certification: Certification | None = ormar.ForeignKey(
        Certification, nullable=True, ondelete=ReferentialAction.CASCADE
    )
    sort_order: int = ormar.Integer(default=0)

    ormar_config = ormar.OrmarConfig(
        tablename="topics",
        metadata=metadata,
        database=database,
    )


class UserGamificationProfile(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = ormar.UUID(unique=True)
    total_xp: int = ormar.Integer(default=0, minimum=0)
    level: int = ormar.Integer(default=1, minimum=1)
    current_streak_days: int = ormar.Integer(default=0, minimum=0)
    longest_streak_days: int = ormar.Integer(default=0, minimum=0)
    last_activity_date: date | None = ormar.Date(nullable=True, default=None)
    battles_won: int = ormar.Integer(default=0, minimum=0)
    battles_played: int = ormar.Integer(default=0, minimum=0)
    questions_answered: int = ormar.Integer(default=0, minimum=0)
    questions_correct: int = ormar.Integer(default=0, minimum=0)

    ormar_config = ormar.OrmarConfig(
        tablename="user_gamification_profiles",
        metadata=metadata,
        database=database,
    )


class UserTopicStat(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = ormar.UUID()
    topic_id: uuid.UUID = ormar.UUID()
    questions_answered: int = ormar.Integer(default=0, minimum=0)
    questions_correct: int = ormar.Integer(default=0, minimum=0)
    xp_earned: int = ormar.Integer(default=0, minimum=0)

    ormar_config = ormar.OrmarConfig(
        tablename="user_topic_stats",
        metadata=metadata,
        database=database,
    )


class XpEvent(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = ormar.UUID()
    amount: int = ormar.Integer()
    source: str = ormar.String(max_length=32)
    certification_id: uuid.UUID | None = ormar.UUID(nullable=True, default=None)
    topic_id: uuid.UUID | None = ormar.UUID(nullable=True, default=None)
    note: str | None = ormar.Text(nullable=True, default=None)
    created_at: datetime = ormar.DateTime(default=datetime.now())

    ormar_config = ormar.OrmarConfig(
        tablename="xp_events",
        metadata=metadata,
        database=database,
    )


class LeaderboardScore(ormar.Model):
    """Aggregated XP for leaderboard windows (updated when XP is awarded)."""

    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = ormar.UUID()
    period: str = ormar.String(max_length=16)
    period_key: str = ormar.String(max_length=32)
    certification_id: uuid.UUID | None = ormar.UUID(nullable=True, default=None)
    xp: int = ormar.Integer(default=0, minimum=0)

    ormar_config = ormar.OrmarConfig(
        tablename="leaderboard_scores",
        metadata=metadata,
        database=database,
    )


class BattleResult(ormar.Model):
    id: uuid.UUID = ormar.UUID(primary_key=True, default=uuid.uuid4)
    quiz_id: uuid.UUID = ormar.UUID()
    game_id: uuid.UUID = ormar.UUID()
    winner_user_id: uuid.UUID | None = ormar.UUID(nullable=True, default=None)
    player_scores: dict = ormar.JSON(nullable=False)
    created_at: datetime = ormar.DateTime(default=datetime.now())

    ormar_config = ormar.OrmarConfig(
        tablename="battle_results",
        metadata=metadata,
        database=database,
    )


class BattleLobbyState(BaseModel):
    battle_code: str
    quiz_id: str
    host_user_id: str
    max_players: int = 4
    player_slots: list[dict]
    status: str = "waiting"
    game_pin: str | None = None
    game_id: str | None = None
    certification_slug: str | None = None
