#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0
"""Reproduce live multi-question flow against production (or any API) via socket.io."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from typing import Any

import aiohttp
import socketio

API_DEFAULT = "https://cmaclash-api.onrender.com"


def ts() -> str:
    return f"{time.time():.3f}"


def summarize(event: str, data: Any) -> str:
    if event == "set_question_number" and isinstance(data, dict):
        return json.dumps(
            {
                "question_index": data.get("question_index"),
                "has_question": bool(data.get("question")),
                "answer_deadline_ms": data.get("answer_deadline_ms"),
            },
            sort_keys=True,
        )
    if event == "question_results":
        if isinstance(data, dict):
            rows = data.get("results")
            return json.dumps(
                {
                    "shape": "wrapped",
                    "question_index": data.get("question_index"),
                    "results_len": len(rows) if isinstance(rows, list) else type(rows).__name__,
                },
                sort_keys=True,
            )
        if isinstance(data, list):
            return json.dumps({"shape": "bare_array", "len": len(data)}, sort_keys=True)
        return repr(data)[:200]
    if isinstance(data, (dict, list)):
        s = json.dumps(data, default=str)
        return s[:300] + ("..." if len(s) > 300 else "")
    return repr(data)[:200]


class ClientLog:
    def __init__(self, name: str, sio: socketio.AsyncClient):
        self.name = name
        self.sio = sio
        self.events: list[tuple[str, str, Any]] = []

    def attach(self) -> None:
        @self.sio.on("*")
        async def catch_all(event, *args):
            data = args[0] if args else None
            self.events.append((ts(), event, data))
            print(f"[{ts()}] {self.name:8} {event:22} {summarize(event, data)}")

        @self.sio.event
        async def connect():
            print(f"[{ts()}] {self.name:8} connect                sid={self.sio.sid}")

        @self.sio.event
        async def disconnect():
            print(f"[{ts()}] {self.name:8} disconnect")


async def fetch_quiz_id(session: aiohttp.ClientSession, api: str) -> str:
    url = f"{api}/api/v1/clash/quizzes?page_size=5"
    async with session.get(url) as resp:
        resp.raise_for_status()
        quizzes = await resp.json()
    if not quizzes:
        raise RuntimeError("no public quizzes")
    # Prefer a quiz with several questions
    for q in quizzes:
        if q.get("question_count", 0) >= 3:
            return q["id"]
    return quizzes[0]["id"]


async def start_game(session: aiohttp.ClientSession, api: str, quiz_id: str, game_mode: str) -> dict:
    params = {
        "captcha_enabled": "False",
        "game_mode": game_mode,
        "custom_field": "",
        "cqcs_enabled": "False",
        "randomize_answers": "False",
    }
    url = f"{api}/api/v1/quiz/start/{quiz_id}"
    async with session.post(url, params=params) as resp:
        text = await resp.text()
        if resp.status != 200:
            raise RuntimeError(f"start failed {resp.status}: {text[:500]}")
        return json.loads(text)


async def run_flow(
    api: str,
    game_mode: str,
    wait_reveal_sec: float,
    manual_advance_sec: float | None,
) -> int:
    quiz_id = None
    async with aiohttp.ClientSession() as http:
        quiz_id = await fetch_quiz_id(http, api)
        print(f"[{ts()}] quiz_id={quiz_id} game_mode={game_mode}")
        start_body = await start_game(http, api, quiz_id, game_mode)
    game_pin = start_body["game_pin"]
    game_id = start_body["game_id"]
    print(f"[{ts()}] game_pin={game_pin} game_id={game_id}")

    admin = socketio.AsyncClient(logger=False, engineio_logger=False)
    p1 = socketio.AsyncClient(logger=False, engineio_logger=False)
    p2 = socketio.AsyncClient(logger=False, engineio_logger=False)
    admin_log = ClientLog("admin", admin)
    p1_log = ClientLog("player1", p1)
    p2_log = ClientLog("player2", p2)
    admin_log.attach()
    p1_log.attach()
    p2_log.attach()

    socket_url = api.rstrip("/")
    await admin.connect(socket_url, transports=["websocket", "polling"])
    await p1.connect(socket_url, transports=["websocket", "polling"])
    await p2.connect(socket_url, transports=["websocket", "polling"])

    await admin.emit("register_as_admin", {"game_pin": game_pin, "game_id": game_id})
    await asyncio.sleep(0.3)
    await p1.emit(
        "join_game",
        {"game_pin": game_pin, "username": "ReproP1", "captcha": "", "custom_field": ""},
    )
    await p2.emit(
        "join_game",
        {"game_pin": game_pin, "username": "ReproP2", "captcha": "", "custom_field": ""},
    )
    await asyncio.sleep(0.5)
    if game_mode == "normal":
        await admin.emit("start_game", {})
        await asyncio.sleep(0.5)
        await admin.emit("set_question_number", "0")
        await asyncio.sleep(0.5)
    else:
        await admin.emit("start_game", {})
        await asyncio.sleep(1.0)

    q0_payload = None
    for _, ev, data in admin_log.events:
        if ev == "set_question_number" and isinstance(data, dict) and data.get("question_index") == 0:
            q0_payload = data
            break
    if not q0_payload or not q0_payload.get("question"):
        print("ERROR: admin never received set_question_number for Q0 with question payload")
        await admin.disconnect()
        await p1.disconnect()
        await p2.disconnect()
        return 1

    answers = q0_payload["question"].get("answers") or []
    pick = answers[0]["answer"] if answers else "Yes"
    await p1.emit("submit_answer", {"question_index": 0, "answer": pick})
    await p2.emit("submit_answer", {"question_index": 0, "answer": pick})
    print(f"[{ts()}] both players answered Q1 with {pick!r}")

    if manual_advance_sec is not None:
        await asyncio.sleep(manual_advance_sec)
        await admin.emit("set_question_number", "1")
        print(f"[{ts()}] host manual set_question_number(1)")
        await asyncio.sleep(max(0.0, wait_reveal_sec - manual_advance_sec))
    else:
        await asyncio.sleep(wait_reveal_sec)

    def last_q_index(log: ClientLog) -> int | None:
        idx = None
        for _, ev, data in log.events:
            if ev == "set_question_number" and isinstance(data, dict):
                idx = data.get("question_index")
        return idx

    def got_q(log: ClientLog, n: int) -> bool:
        return any(
            ev == "set_question_number" and isinstance(data, dict) and data.get("question_index") == n
            for _, ev, data in log.events
        )

    a1, a2 = last_q_index(p1_log), last_q_index(p2_log)
    print(f"[{ts()}] SUMMARY pin={game_pin} p1_last_q={a1} p2_last_q={a2} admin_last_q={last_q_index(admin_log)}")
    print(f"[{ts()}] p1 got Q2={got_q(p1_log, 1)} p2 got Q2={got_q(p2_log, 1)}")

    ok = got_q(p1_log, 1) and got_q(p2_log, 1)
    await admin.disconnect()
    await p1.disconnect()
    await p2.disconnect()
    return 0 if ok else 2


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--api", default=API_DEFAULT)
    p.add_argument("--game-mode", default="kahoot", choices=["kahoot", "normal"])
    p.add_argument("--wait", type=float, default=12.0, help="seconds after answers before summary")
    p.add_argument(
        "--manual-advance",
        type=float,
        default=None,
        help="host emits set_question_number(1) after N seconds (before auto-advance)",
    )
    args = p.parse_args()
    code = asyncio.run(run_flow(args.api, args.game_mode, args.wait, args.manual_advance))
    sys.exit(code)


if __name__ == "__main__":
    main()
