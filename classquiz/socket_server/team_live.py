# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Team mode for live matches: team setup, team answers, and team scoring.

A team answers as one. The answer most members chose becomes the answer for every member.
Streaks and points are tracked per team. Each member's personal score also receives the team's
points, so the normal standings keep working.
"""

from __future__ import annotations

import json
import random

from classquiz.config import redis
from classquiz.db.models import AnswerData, AnswerDataList, GamePlayer, PlayGame
from classquiz.helpers.team_mode import (
    MIN_TEAMS,
    TeamVote,
    advance_streak,
    assign_teams_randomly,
    clamp_team_count,
    resolve_team_answer,
    score_with_streak,
)

ASSIGN_MODES = ("random", "choose")
TTL = 7200


def _teams_key(game_pin: str) -> str:
    return f"game:{game_pin}:teams"


def _team_scores_key(game_pin: str) -> str:
    return f"game_session:{game_pin}:team_scores"


def _team_answers_key(game_pin: str) -> str:
    return f"game_session:{game_pin}:team_answers"


def _team_streak_key(game_pin: str, team: int) -> str:
    return f"game_session:{game_pin}:streak:team:{team}"


def _player_scores_key(game_pin: str) -> str:
    return f"game_session:{game_pin}:player_scores"


async def roster_usernames(game_pin: str) -> list[str]:
    names = set()
    for raw in await redis.smembers(f"game_session:{game_pin}:players"):
        player = GamePlayer.model_validate_json(raw)
        if player.username:
            names.add(player.username)
    return sorted(names)


async def get_team_map(game_pin: str) -> dict[str, int]:
    raw = await redis.hgetall(_teams_key(game_pin))
    return {name: int(team) for name, team in raw.items()}


async def set_team_mode(game_pin: str, count: int, assign: str) -> PlayGame:
    """Host setup. Only allowed before the game starts, and not for battles."""
    if assign not in ASSIGN_MODES:
        raise ValueError("invalid_assign")
    game = await PlayGame.get_from_redis(game_pin)
    if game.game_mode == "battle":
        raise ValueError("battle_not_supported")
    if game.started:
        raise ValueError("already_started")
    players = await roster_usernames(game_pin)
    game.team_mode = {
        "count": clamp_team_count(int(count), max(len(players), MIN_TEAMS)),
        "assign": assign,
    }
    await game.save(game_pin)
    return game


async def choose_team(game_pin: str, username: str, team: int) -> None:
    game = await PlayGame.get_from_redis(game_pin)
    cfg = game.team_mode
    if not cfg:
        raise ValueError("no_team_mode")
    if cfg["assign"] != "choose":
        raise ValueError("teams_are_random")
    if game.started:
        raise ValueError("already_started")
    if not 0 <= team < cfg["count"]:
        raise ValueError("invalid_team")
    await redis.hset(_teams_key(game_pin), username, str(team))
    await redis.expire(_teams_key(game_pin), TTL)


async def place_unassigned(game_pin: str, game: PlayGame, at_start: bool = False) -> None:
    """Put every player without a team on the smallest team.

    In choose mode, players pick their own team before the game starts, so nothing is placed
    until start (at_start=True).
    """
    cfg = game.team_mode
    if not cfg:
        return
    if cfg["assign"] == "choose" and not game.started and not at_start:
        return
    count = cfg["count"]
    teams = await get_team_map(game_pin)
    pending = [u for u in await roster_usernames(game_pin) if u not in teams]
    random.shuffle(pending)
    sizes = [0] * count
    for team in teams.values():
        if team < count:
            sizes[team] += 1
    new = {}
    for name in pending:
        team = min(range(count), key=lambda i: (sizes[i], i))
        sizes[team] += 1
        new[name] = str(team)
    if new:
        await redis.hset(_teams_key(game_pin), mapping=new)
        await redis.expire(_teams_key(game_pin), TTL)


async def reshuffle_random_teams(game_pin: str, game: PlayGame) -> None:
    """Random mode at start: a fresh balanced shuffle of everyone in the lobby."""
    count = int((game.team_mode or {}).get("count", MIN_TEAMS))
    mapping = assign_teams_randomly(await roster_usernames(game_pin), count)
    await redis.delete(_teams_key(game_pin))
    if mapping:
        await redis.hset(_teams_key(game_pin), mapping={u: str(t) for u, t in mapping.items()})
        await redis.expire(_teams_key(game_pin), TTL)


async def roster_payload(game_pin: str) -> dict:
    game = await PlayGame.get_from_redis(game_pin)
    cfg = game.team_mode or {}
    count = cfg.get("count", 0)
    teams = await get_team_map(game_pin)
    names = await roster_usernames(game_pin)
    return {
        "count": count,
        "assign": cfg.get("assign"),
        "started": game.started,
        "teams": {str(i): sorted(u for u in names if teams.get(u) == i) for i in range(count)},
        "unassigned": sorted(u for u in names if u not in teams),
    }


async def emit_team_roster(sio, game_pin: str) -> None:
    payload = await roster_payload(game_pin)
    await sio.emit("team_roster", payload, room=game_pin)
    await sio.emit("team_roster", payload, room=f"admin:{game_pin}")


async def _advance_team_streak(game_pin: str, team: int, question_index: int, correct: bool) -> int:
    key = _team_streak_key(game_pin, team)
    prev, prev_question = 0, None
    raw = await redis.get(key)
    if raw:
        stored = json.loads(raw)
        prev, prev_question = int(stored["n"]), int(stored["q"])
    streak = advance_streak(prev, prev_question, question_index, correct)
    await redis.set(key, json.dumps({"n": streak, "q": question_index}), ex=TTL)
    return streak


async def resolve_team_round(game_pin: str, question_index: int) -> None:
    """Replace each member's vote with the team's answer, then score the team.

    Runs when a question closes, before non-answers are recorded. Teams with no votes are left
    alone, so their members are recorded as wrong like everyone else who didn't answer.
    """
    game = await PlayGame.get_from_redis(game_pin)
    if not game.team_mode:
        return
    await place_unassigned(game_pin, game)
    count = game.team_mode["count"]
    teams = await get_team_map(game_pin)
    votes = {a.username: a for a in (await AnswerDataList.get_redis_or_empty(game_pin, question_index)).root}

    summary: dict[str, dict] = {}
    records: list[AnswerData] = []
    for team in range(count):
        members = sorted(u for u, t in teams.items() if t == team)
        voted = [votes[u] for u in members if u in votes]
        if not voted:
            continue
        answer, reason = resolve_team_answer(
            [TeamVote(a.username, a.answer, int(a.time_taken)) for a in voted]
        )
        if answer is None:
            continue
        rep = min((a for a in voted if a.answer == answer), key=lambda a: a.time_taken)
        right = rep.right
        streak = await _advance_team_streak(game_pin, team, question_index, right)
        base, speed = (rep.base_score, rep.speed_bonus) if right else (0, 0)
        points = score_with_streak(base, speed, streak) if right else 0
        bonus = points - (base + speed) if right else 0
        if points:
            await redis.hincrby(_team_scores_key(game_pin), str(team), points)
        summary[str(team)] = {
            "answer": answer,
            "right": right,
            "reason": reason,
            "streak": streak,
            "points": points,
        }
        for name in members:
            await redis.hincrby(_player_scores_key(game_pin), name, points)
            records.append(
                AnswerData(
                    username=name,
                    answer=answer,
                    right=right,
                    time_taken=rep.time_taken,
                    score=points,
                    base_score=base,
                    speed_bonus=speed,
                    streak=streak if right else 0,
                    streak_bonus=bonus,
                )
            )

    key = f"game_session:{game_pin}:{question_index}"
    await redis.delete(key)
    if records:
        await redis.rpush(key, *[r.model_dump_json() for r in records])
        await redis.expire(key, TTL)
    if summary:
        await redis.hset(_team_answers_key(game_pin), str(question_index), json.dumps(summary))
        await redis.expire(_team_answers_key(game_pin), TTL)


async def team_standings(game_pin: str) -> list[dict]:
    """Scoreboard rows for team games: one row per team, labeled "Team N". No player names."""
    from classquiz.helpers.live_scoring import build_standings

    game = await PlayGame.get_from_redis(game_pin)
    count = int((game.team_mode or {}).get("count", 0))
    totals = await redis.hgetall(_team_scores_key(game_pin))
    return build_standings({f"Team {t + 1}": int(totals.get(str(t), 0)) for t in range(count)})


async def team_results_summary(game_pin: str, question_index: int) -> dict | None:
    """Per-team block for the question_results payload."""
    game = await PlayGame.get_from_redis(game_pin)
    if not game.team_mode:
        return None
    raw = await redis.hget(_team_answers_key(game_pin), str(question_index))
    answers = json.loads(raw) if raw else {}
    totals = await redis.hgetall(_team_scores_key(game_pin))
    teams = await get_team_map(game_pin)
    names = await roster_usernames(game_pin)
    out = []
    for team in range(game.team_mode["count"]):
        result = answers.get(str(team), {})
        out.append(
            {
                "index": team,
                "name": f"Team {team + 1}",
                "members": sorted(u for u in names if teams.get(u) == team),
                "answer": result.get("answer"),
                "right": result.get("right"),
                "reason": result.get("reason"),
                "streak": result.get("streak", 0),
                "points": result.get("points", 0),
                "total": int(totals.get(str(team), 0)),
            }
        )
    return {"count": game.team_mode["count"], "assign": game.team_mode["assign"], "teams": out}
