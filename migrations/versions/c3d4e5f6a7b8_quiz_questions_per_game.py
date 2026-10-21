# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Add questions_per_game to quiz

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-10-21 03:45:00.000000

"""

from alembic import op
import sqlalchemy as sa

revision = "c3d4e5f6a7b8"
down_revision = "b2c3d4e5f6a7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "quiz",
        sa.Column("questions_per_game", sa.Integer(), nullable=True, server_default="10"),
    )


def downgrade() -> None:
    op.drop_column("quiz", "questions_per_game")
