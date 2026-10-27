# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Team mode and streak bonus rules for live games.

Pure functions, no I/O, so the rules can be tested without Redis or sockets.

- Teams: the host picks a team count. Players are assigned at random (balanced) or
  pick their own team in the lobby.
- Team answer: the answer most team members chose. A tie goes to the tied answer
  that was submitted first by any member of the team.
- Streak: score = (base + speed bonus) x multiplier, where the multiplier is
  1 + 0.1 x (streak - 1) for a streak of 1 or more, capped at 2x.
"""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass

MIN_TEAMS = 2
MAX_TEAMS = 8
STREAK_STEP = 0.1
STREAK_MULTIPLIER_CAP = 2.0


def clamp_team_count(team_count: int, player_count: int) -> int:
    """A team count the host can use: at least 2, at most 8 and at most one team per player."""
    return max(MIN_TEAMS, min(team_count, MAX_TEAMS, max(player_count, MIN_TEAMS)))


def assign_teams_randomly(usernames: list[str], team_count: int, rng: random.Random | None = None) -> dict[str, int]:
    """Return {username: team_index}, shuffled and split into teams that differ by at most one player."""
    rng = rng or random.Random()
    team_count = clamp_team_count(team_count, len(usernames))
    shuffled = list(usernames)
    rng.shuffle(shuffled)
    return {name: i % team_count for i, name in enumerate(shuffled)}


@dataclass(frozen=True)
class TeamVote:
    username: str
    answer: str
    submitted_ms: int


def resolve_team_answer(votes: list[TeamVote]) -> tuple[str | None, str]:
    """Pick the team's answer from its members' votes.

    Returns (answer, reason). reason is "majority", "tie_first_submitted", or "no_votes".
    """
    if not votes:
        return None, "no_votes"
    counts = Counter(v.answer for v in votes)
    top = max(counts.values())
    tied = [a for a, n in counts.items() if n == top]
    if len(tied) == 1:
        return tied[0], "majority"
    # Tie: the tied answer whose earliest submission came first.
    earliest = {a: min(v.submitted_ms for v in votes if v.answer == a) for a in tied}
    winner = min(tied, key=lambda a: (earliest[a], a))
    return winner, "tie_first_submitted"


def streak_multiplier(streak: int) -> float:
    """Multiplier for a correct answer on a streak. 1st correct = 1.0x, rising 0.1x per step, capped at 2.0x."""
    if streak <= 1:
        return 1.0
    return min(STREAK_MULTIPLIER_CAP, round(1.0 + STREAK_STEP * (streak - 1), 4))


def score_with_streak(base_points: int, speed_bonus: int, streak: int) -> int:
    """Total points for a correct answer, including the streak multiplier."""
    return int(round((base_points + speed_bonus) * streak_multiplier(streak)))


def advance_streak(
    prev_streak: int,
    prev_question: int | None,
    question_index: int,
    correct: bool,
) -> int:
    """New streak after answering question_index.

    A correct answer extends the streak only if the player's previous recorded answer was on the
    question right before this one. A wrong answer, or a skipped question, starts over.
    """
    if not correct:
        return 0
    consecutive = prev_question is not None and prev_question == question_index - 1
    return (prev_streak if consecutive else 0) + 1
