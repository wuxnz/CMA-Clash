# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""CMA Clash certifications, gamification, and quiz metadata

Revision ID: a1b2c3d4e5f6
Revises: 9d7fa2e6b24c
Create Date: 2026-10-20 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa
import ormar

revision = "a1b2c3d4e5f6"
down_revision = "9d7fa2e6b24c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "certifications",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("slug", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_table(
        "topics",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("slug", sa.String(length=96), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("certification", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["certification"], ["certifications.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_table(
        "user_gamification_profiles",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("user_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("total_xp", sa.Integer(), nullable=True),
        sa.Column("level", sa.Integer(), nullable=True),
        sa.Column("current_streak_days", sa.Integer(), nullable=True),
        sa.Column("longest_streak_days", sa.Integer(), nullable=True),
        sa.Column("last_activity_date", sa.Date(), nullable=True),
        sa.Column("battles_won", sa.Integer(), nullable=True),
        sa.Column("battles_played", sa.Integer(), nullable=True),
        sa.Column("questions_answered", sa.Integer(), nullable=True),
        sa.Column("questions_correct", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "user_topic_stats",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("user_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("topic_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("questions_answered", sa.Integer(), nullable=True),
        sa.Column("questions_correct", sa.Integer(), nullable=True),
        sa.Column("xp_earned", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "xp_events",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("user_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("source", sa.String(length=32), nullable=False),
        sa.Column("certification_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.Column("topic_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "leaderboard_scores",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("user_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("period", sa.String(length=16), nullable=False),
        sa.Column("period_key", sa.String(length=32), nullable=False),
        sa.Column("certification_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.Column("xp", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "battle_results",
        sa.Column("id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("quiz_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("game_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.Column("winner_user_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
        sa.Column("player_scores", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("quiz", sa.Column("certification_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True))
    op.add_column("quiz", sa.Column("topic_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True))
    op.add_column("quiz", sa.Column("difficulty", sa.String(length=32), nullable=True))
    op.add_column("quiz", sa.Column("seed_slug", sa.String(length=128), nullable=True))
    op.create_unique_constraint("uq_quiz_seed_slug", "quiz", ["seed_slug"])


def downgrade() -> None:
    op.drop_constraint("uq_quiz_seed_slug", "quiz", type_="unique")
    op.drop_column("quiz", "seed_slug")
    op.drop_column("quiz", "difficulty")
    op.drop_column("quiz", "topic_id")
    op.drop_column("quiz", "certification_id")
    op.drop_table("battle_results")
    op.drop_table("leaderboard_scores")
    op.drop_table("xp_events")
    op.drop_table("user_topic_stats")
    op.drop_table("user_gamification_profiles")
    op.drop_table("topics")
    op.drop_table("certifications")
