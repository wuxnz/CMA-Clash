# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.helpers.live_scoring import (
    LIVE_CORRECT_BASE_POINTS,
    LIVE_SPEED_BONUS_MAX,
    assign_speed_ranks,
    build_standings,
    compute_speed_bonus_ms,
    merge_standings_into_results,
    score_correct_answer,
)


def test_speed_bonus_at_start_is_max() -> None:
    start = 1_000_000
    deadline = start + 30_000
    assert compute_speed_bonus_ms(start, start, deadline) == LIVE_SPEED_BONUS_MAX


def test_speed_bonus_at_deadline_is_zero() -> None:
    start = 1_000_000
    deadline = start + 30_000
    assert compute_speed_bonus_ms(deadline, start, deadline) == 0


def test_score_correct_answer_totals() -> None:
    start = 0
    deadline = 10_000
    base, bonus, total = score_correct_answer(0, start, deadline)
    assert base == LIVE_CORRECT_BASE_POINTS
    assert bonus == LIVE_SPEED_BONUS_MAX
    assert total == base + bonus


def test_speed_ranks_by_time_taken() -> None:
    rows = [
        {"username": "slow", "right": True, "time_taken": 5000},
        {"username": "fast", "right": True, "time_taken": 100},
        {"username": "wrong", "right": False, "time_taken": 50},
    ]
    assign_speed_ranks(rows)
    assert rows[1]["speed_rank"] == 1
    assert rows[0]["speed_rank"] == 2
    assert "speed_rank" not in rows[2] or rows[2].get("speed_rank") is None


def test_standings_behind_and_lead() -> None:
    standings = build_standings({"alice": 1200, "bob": 900, "cara": 900})
    assert standings[0]["username"] == "alice"
    assert standings[0]["overall_rank"] == 1
    assert standings[0]["points_ahead_of_next"] == 300
    bob = next(s for s in standings if s["username"] == "bob")
    assert bob["overall_rank"] == 2
    assert bob["points_behind_above"] == 300
    assert bob["player_above"] == "alice"


def test_merge_standings_into_results() -> None:
    results = [{"username": "bob", "right": True, "score": 900}]
    standings = build_standings({"alice": 1200, "bob": 900})
    merged = merge_standings_into_results(results, standings)
    assert merged[0]["overall_rank"] == 2
    assert merged[0]["points_behind_above"] == 300
    assert merged[0]["player_above"] == "alice"
