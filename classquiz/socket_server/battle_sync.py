# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Battle lobby roster, synchronized kickoff, and answer quorum."""

from __future__ import annotations

import asyncio
import json

from classquiz.battle.service import BATTLE_REDIS_PREFIX
from classquiz.config import redis

BATTLE_KICKOFF_MAX_WAIT_SEC = 15


async def battle_roster_usernames(game_pin: str) -> list[str] | None:
    meta_raw = await redis.get(f"{BATTLE_REDIS_PREFIX}:meta:{game_pin}")
    if meta_raw is None:
        return None
    meta = json.loads(meta_raw)
    return list(meta.get("player_user_ids", {}).keys())


async def battle_roster_size(game_pin: str) -> int:
    names = await battle_roster_usernames(game_pin)
    if names is not None:
        return len(names)
    return await redis.scard(f"game_session:{game_pin}:players")


async def is_username_in_battle_roster(game_pin: str, username: str) -> bool:
    names = await battle_roster_usernames(game_pin)
    if names is None:
        return True
    return username in names


async def is_battle_finished(game_pin: str) -> bool:
    return await redis.get(f"{BATTLE_REDIS_PREFIX}:done:{game_pin}") is not None


async def schedule_battle_kickoff(sio, game_pin: str) -> None:
    """Wait for all lobby players to join_game, or max wait, then start question 0."""
    from classquiz.socket_server.game_sync import try_kickoff_battle

    usernames = await battle_roster_usernames(game_pin)
    if not usernames:
        await try_kickoff_battle(sio, game_pin)
        return
    await redis.set(
        f"{BATTLE_REDIS_PREFIX}:kickoff:{game_pin}",
        json.dumps({"usernames": usernames, "kicked_off": False}),
        ex=18000,
    )
    await redis.delete(f"{BATTLE_REDIS_PREFIX}:joined:{game_pin}")

    async def _deadline() -> None:
        try:
            await asyncio.sleep(BATTLE_KICKOFF_MAX_WAIT_SEC)
            await try_kickoff_battle(sio, game_pin)
        except asyncio.CancelledError:
            return

    asyncio.create_task(_deadline())


async def battle_player_joined_socket(sio, game_pin: str, username: str) -> None:
    from classquiz.socket_server.game_sync import try_kickoff_battle

    kickoff_raw = await redis.get(f"{BATTLE_REDIS_PREFIX}:kickoff:{game_pin}")
    if kickoff_raw is None:
        return
    kickoff = json.loads(kickoff_raw)
    if kickoff.get("kicked_off"):
        return
    expected = kickoff.get("usernames") or []
    if username not in expected:
        return
    await redis.sadd(f"{BATTLE_REDIS_PREFIX}:joined:{game_pin}", username)
    joined = await redis.smembers(f"{BATTLE_REDIS_PREFIX}:joined:{game_pin}")
    if set(expected).issubset(set(joined)):
        await try_kickoff_battle(sio, game_pin)
