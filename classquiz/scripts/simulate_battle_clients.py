#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Simulate a 2-player battle against a running API (Socket.IO + REST).

Usage (local API on :8000):
  python3 classquiz/scripts/simulate_battle_clients.py --base http://127.0.0.1:8000
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys

import httpx
import socketio


async def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="http://127.0.0.1:8000")
    args = parser.parse_args()
    base = args.base.rstrip("/")

    async with httpx.AsyncClient(base_url=base, timeout=60.0) as client:
        quizzes = (await client.get("/api/v1/clash/quizzes", params={"page_size": 1})).json()
        if not quizzes:
            print("No quizzes", file=sys.stderr)
            return 1
        quiz_id = quizzes[0]["id"]
        create = await client.post(
            "/api/v1/clash/battles",
            json={"quiz_id": quiz_id, "max_players": 2, "display_name": "SimHost"},
        )
        create.raise_for_status()
        lobby = create.json()
        code = lobby["battle_code"]
        secret = lobby["host_secret"]
        await client.post(f"/api/v1/clash/battles/{code}/join", json={"display_name": "SimGuest"})
        start = await client.post(f"/api/v1/clash/battles/{code}/start", json={"host_secret": secret})
        start.raise_for_status()
        game_pin = start.json()["game_pin"]

    events: list[str] = []

    async def player(name: str) -> None:
        sio = socketio.AsyncClient()
        @sio.event
        async def connect():
            events.append(f"{name}:connect")

        @sio.event
        async def start_game():
            events.append(f"{name}:start_game")

        @sio.event
        async def set_question_number(data):
            events.append(f"{name}:q{data.get('question_index')}")

        await sio.connect(base, socketio_path="/socket.io", transports=["websocket", "polling"])
        await sio.emit(
            "join_game",
            {"game_pin": game_pin, "username": name, "captcha": "", "custom_field": ""},
        )
        await asyncio.sleep(2)
        await sio.disconnect()

    await asyncio.gather(player("SimHost"), player("SimGuest"))
    print(json.dumps({"game_pin": game_pin, "events": events}, indent=2))
    ok = any("start_game" in e for e in events) and any(":q0" in e for e in events)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
