#!/usr/bin/env python3
"""Copy a handful of public seed quizzes onto the demo user for dashboard captures."""
from __future__ import annotations

import asyncio
import os
import sys
import uuid
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from classquiz.db import database
from classquiz.db.models import Quiz, User

DEMO_EMAIL = os.environ.get("DEMO_EMAIL", "demo@cmaclash.local")


async def main() -> int:
    await database.connect()
    demo = await User.objects.get_or_none(email=DEMO_EMAIL)
    if demo is None:
        print("demo user missing")
        await database.disconnect()
        return 1
    owned = await Quiz.objects.filter(user_id=demo.id).all()
    if len(owned) >= 6:
        print(f"demo already owns {len(owned)} quizzes")
        await database.disconnect()
        return 0
    seeds = await Quiz.objects.filter(public=True).limit(40).all()
    copied = 0
    for q in seeds:
        if str(q.user_id) == str(demo.id):
            continue
        await Quiz(
            id=uuid.uuid4(),
            public=True,
            title=q.title,
            description=q.description,
            user_id=demo.id,
            questions=q.questions,
            cover_image=q.cover_image,
            certification_id=q.certification_id,
            topic_id=q.topic_id,
            difficulty=q.difficulty,
            seed_slug=None,
            updated_at=datetime.now(),
        ).save()
        copied += 1
        if copied >= 8:
            break
    print(f"copied {copied} quizzes to {DEMO_EMAIL}")
    await database.disconnect()
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
