# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Live kahoot-style scoring: base points, speed bonus, standings helpers."""

from __future__ import annotations

from typing import Any

LIVE_CORRECT_BASE_POINTS = 500
LIVE_SPEED_BONUS_MAX = 500


def compute_speed_bonus_ms(
    answer_submitted_ms: int,
    answer_phase_start_ms: int,
    answer_deadline_ms: int,
) -> int:
    """Bonus for a correct answer; 0 at deadline, capped at LIVE_SPEED_BONUS_MAX."""
    window_ms = max(1, answer_deadline_ms - answer_phase_start_ms)
    elapsed_ms = answer_submitted_ms - answer_phase_start_ms
    if elapsed_ms < 0:
        elapsed_ms = 0
    if elapsed_ms > window_ms:
        elapsed_ms = window_ms
    frac = 1.0 - (elapsed_ms / window_ms)
    return int(round(frac * LIVE_SPEED_BONUS_MAX))


def score_correct_answer(
    answer_submitted_ms: int,
    answer_phase_start_ms: int,
    answer_deadline_ms: int,
) -> tuple[int, int, int]:
    """Return (base_score, speed_bonus, total_score) for a correct answer."""
    bonus = compute_speed_bonus_ms(answer_submitted_ms, answer_phase_start_ms, answer_deadline_ms)
    base = LIVE_CORRECT_BASE_POINTS
    return base, bonus, base + bonus


def ordinal_word(n: int) -> str:
    if n < 1:
        return str(n)
    words = {
        1: "1st",
        2: "2nd",
        3: "3rd",
    }
    return words.get(n, f"{n}th")


def assign_speed_ranks(rows: list[dict[str, Any]]) -> None:
    correct = [r for r in rows if r.get("right")]
    correct.sort(key=lambda r: float(r.get("time_taken") or 0))
    for rank, row in enumerate(correct, start=1):
        row["speed_rank"] = rank


def build_standings(player_scores: dict[str, int]) -> list[dict[str, Any]]:
    ordered = sorted(player_scores.items(), key=lambda item: (-item[1], item[0]))
    standings: list[dict[str, Any]] = []
    for idx, (username, total) in enumerate(ordered):
        entry: dict[str, Any] = {
            "username": username,
            "score": int(total),
            "overall_rank": idx + 1,
        }
        if idx == 0 and len(ordered) > 1:
            entry["points_ahead_of_next"] = int(ordered[0][1]) - int(ordered[1][1])
        elif idx > 0:
            above_name, above_score = ordered[idx - 1]
            entry["player_above"] = above_name
            entry["points_behind_above"] = int(above_score) - int(total)
        standings.append(entry)
    return standings


def standings_top_n(standings: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    return standings[:limit]


def merge_standings_into_results(
    results: list[dict[str, Any]],
    standings: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_user = {s["username"]: s for s in standings}
    merged: list[dict[str, Any]] = []
    for row in results:
        out = dict(row)
        extra = by_user.get(row.get("username", ""))
        if extra:
            out.update(
                {
                    k: extra[k]
                    for k in (
                        "overall_rank",
                        "points_behind_above",
                        "player_above",
                        "points_ahead_of_next",
                    )
                    if k in extra
                }
            )
        merged.append(out)
    return merged
