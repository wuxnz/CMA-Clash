# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Server-authoritative live question timing (epoch ms)."""

from __future__ import annotations

import json
import time
from typing import Any

from classquiz.config import redis
from classquiz.db.models import PlayGame

INTRO_MS = 3500
TIMING_KEY = "game:{game_pin}:timing"


def server_now_ms() -> int:
    return int(time.time() * 1000)


def is_kahoot_style(game_mode: str | None) -> bool:
    return game_mode in ("kahoot", "battle", None)


def build_question_timing(game_data: PlayGame, question_index: int, now_ms: int | None = None) -> dict[str, Any]:
    now_ms = now_ms if now_ms is not None else server_now_ms()
    q_secs = int(float(game_data.questions[question_index].time))
    answer_duration_ms = max(1000, q_secs * 1000)
    intro_ms = 0 if is_kahoot_style(game_data.game_mode) else INTRO_MS
    question_start_ms = now_ms
    intro_deadline_ms = question_start_ms + intro_ms
    answer_phase_start_ms = intro_deadline_ms
    answer_deadline_ms = answer_phase_start_ms + answer_duration_ms
    return {
        "question_index": question_index,
        "question_start_ms": question_start_ms,
        "intro_deadline_ms": intro_deadline_ms,
        "answer_phase_start_ms": answer_phase_start_ms,
        "answer_deadline_ms": answer_deadline_ms,
        "server_time_ms": now_ms,
    }


async def save_question_timing(game_pin: str, timing: dict[str, Any]) -> None:
    await redis.set(TIMING_KEY.format(game_pin=game_pin), json.dumps(timing), ex=7200)


async def load_question_timing(game_pin: str) -> dict[str, Any] | None:
    raw = await redis.get(TIMING_KEY.format(game_pin=game_pin))
    if not raw:
        return None
    return json.loads(raw)
