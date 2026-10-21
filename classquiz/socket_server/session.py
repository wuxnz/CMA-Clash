# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.config import redis
import json
from typing import Any
from socketio import AsyncServer
from socketio.exceptions import ConnectionRefusedError


async def get_session(sid: str, sio: AsyncServer, disconnect_on_error: bool = True) -> dict:
    session_id = (await sio.get_session(sid)).get("session_id")
    if session_id is None:
        raise ConnectionRefusedError("Session not configured")
    val = await redis.get(f"socket_io_session:{session_id}")
    if val is None:
        if disconnect_on_error:
            raise ConnectionRefusedError("session not available")
        return {}
    return json.loads(val)


async def save_session(sid: str, sio: AsyncServer, data: Any, disconnect_on_error: bool = True) -> None:
    session_id = (await sio.get_session(sid)).get("session_id")
    if session_id is None:
        raise ConnectionRefusedError("Session not configured")
    await redis.set(f"socket_io_session:{session_id}", json.dumps(data), ex=3600)


async def leave_game_rooms(sio: AsyncServer, sid: str, game_pin: str | None) -> None:
    if not game_pin:
        return
    await sio.leave_room(sid, game_pin)
    await sio.leave_room(sid, f"admin:{game_pin}")


async def detach_socket_from_prior_game(sio: AsyncServer, sid: str) -> None:
    try:
        prior = await get_session(sid, sio, disconnect_on_error=False)
    except ConnectionRefusedError:
        return
    await leave_game_rooms(sio, sid, prior.get("game_pin"))
