# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import random

from classquiz.helpers.team_mode import (
    STREAK_MULTIPLIER_CAP,
    TeamVote,
    assign_teams_randomly,
    clamp_team_count,
    advance_streak,
    resolve_team_answer,
    score_with_streak,
    streak_multiplier,
)


def test_clamp_team_count_bounds():
    assert clamp_team_count(1, 10) == 2
    assert clamp_team_count(99, 10) == 8
    assert clamp_team_count(4, 3) == 3
    assert clamp_team_count(4, 1) == 2


def test_random_assignment_is_balanced_and_complete():
    names = [f"p{i}" for i in range(7)]
    teams = assign_teams_randomly(names, 3, random.Random(1))
    assert set(teams) == set(names)
    sizes = [list(teams.values()).count(t) for t in range(3)]
    assert sorted(sizes) == [2, 2, 3]


def test_random_assignment_uses_clamped_team_count():
    teams = assign_teams_randomly(["a", "b", "c"], 8, random.Random(2))
    assert set(teams.values()) == {0, 1, 2}


def test_majority_answer_wins():
    votes = [
        TeamVote("a", "B", 100),
        TeamVote("b", "B", 300),
        TeamVote("c", "C", 50),
    ]
    assert resolve_team_answer(votes) == ("B", "majority")


def test_tie_goes_to_answer_submitted_first():
    votes = [
        TeamVote("a", "A", 900),
        TeamVote("b", "C", 200),
        TeamVote("c", "A", 1200),
        TeamVote("d", "C", 1500),
    ]
    assert resolve_team_answer(votes) == ("C", "tie_first_submitted")


def test_no_votes_has_no_answer():
    assert resolve_team_answer([]) == (None, "no_votes")


def test_streak_multiplier_steps_and_cap():
    assert streak_multiplier(0) == 1.0
    assert streak_multiplier(1) == 1.0
    assert streak_multiplier(2) == 1.1
    assert streak_multiplier(5) == 1.4
    assert streak_multiplier(50) == STREAK_MULTIPLIER_CAP


def test_higher_streak_gives_more_points():
    points = [score_with_streak(500, 300, s) for s in range(1, 12)]
    assert points == sorted(points)
    assert points[0] == 800
    assert score_with_streak(500, 300, 11) == 1600


def test_streak_resets_on_wrong_answer():
    assert advance_streak(4, 3, 4, True) == 5
    assert advance_streak(5, 4, 5, False) == 0


def test_streak_breaks_on_skipped_question():
    assert advance_streak(4, 2, 4, True) == 1
    assert advance_streak(0, None, 0, True) == 1
