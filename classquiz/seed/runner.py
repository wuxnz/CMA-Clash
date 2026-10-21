# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import logging
import os
import uuid
from collections import defaultdict
from datetime import datetime

from classquiz.config import settings, meilisearch
from classquiz.db import database
from classquiz.db.cma_models import Certification, Topic
from classquiz.db.models import ABCDQuizAnswer, Quiz, QuizQuestion, QuizQuestionType, User
from classquiz.auth import get_password_hash
from classquiz.helpers import get_meili_data, meilisearch_init
from classquiz.helpers.avatar import gzipped_user_avatar
from classquiz.seed.banks import load_all_facts
from classquiz.seed.catalog import CERTIFICATIONS, TOPIC_QUESTIONS_PER_QUIZ, study_content_for_topic

LOGGER = logging.getLogger(__name__)

SEED_USER_EMAIL = "content@cmaclash.local"
SEED_USER_USERNAME = "cmaclash_content"
DEMO_USER_EMAIL = "demo@cmaclash.local"
DEMO_USER_USERNAME = "demo"
DEMO_USER_PASSWORD = "CMA-Clash-Demo1!"
QUESTIONS_PER_QUIZ = 8


def _certification_uuid(topic: Topic) -> uuid.UUID | None:
    cert = topic.certification
    if cert is None:
        return None
    if isinstance(cert, uuid.UUID):
        return cert
    return cert.id


def _fact_to_question(fact: dict) -> QuizQuestion:
    answers = [ABCDQuizAnswer(right=True, answer=fact["correct"])]
    for d in fact["distractors"]:
        answers.append(ABCDQuizAnswer(right=False, answer=d))
    difficulty = fact.get("difficulty", "intermediate")
    time_secs = "45" if difficulty == "advanced" else "30"
    return QuizQuestion(
        question=fact["stem"],
        time=time_secs,
        type=QuizQuestionType.ABCD,
        answers=answers,
        explanation=fact.get("explanation"),
        references=fact.get("references"),
    )


async def _ensure_demo_user() -> User:
    user = await User.objects.get_or_none(email=DEMO_USER_EMAIL)
    if user is not None:
        return user
    return await User(
        email=DEMO_USER_EMAIL,
        username=DEMO_USER_USERNAME,
        password=get_password_hash(DEMO_USER_PASSWORD),
        verified=True,
        verify_key=None,
        require_password=True,
        avatar=gzipped_user_avatar(),
    ).save()


async def _ensure_seed_user() -> User:
    user = await User.objects.get_or_none(email=SEED_USER_EMAIL)
    if user is not None:
        return user
    return await User(
        email=SEED_USER_EMAIL,
        username=SEED_USER_USERNAME,
        password=None,
        verified=True,
        verify_key=None,
        require_password=False,
        avatar=gzipped_user_avatar(),
    ).save()


async def _ensure_certifications_and_topics() -> dict[str, Topic]:
    topic_by_slug: dict[str, Topic] = {}
    for cert_def in CERTIFICATIONS:
        cert = await Certification.objects.get_or_none(slug=cert_def["slug"])
        if cert is None:
            cert = await Certification(
                slug=cert_def["slug"],
                name=cert_def["name"],
                description=cert_def["description"],
                sort_order=cert_def["sort_order"],
            ).save()
        for slug, name, order in cert_def["topics"]:
            study = study_content_for_topic(slug)
            topic = await Topic.objects.get_or_none(slug=slug)
            if topic is None:
                topic = await Topic(
                    slug=slug,
                    name=name,
                    certification=cert,
                    sort_order=order,
                    study_content=study,
                ).save()
            else:
                updates: dict = {}
                if topic.name != name:
                    updates["name"] = name
                if topic.sort_order != order:
                    updates["sort_order"] = order
                if study is not None and topic.study_content != study:
                    updates["study_content"] = study
                if updates:
                    await topic.update(**updates)
            topic_by_slug[slug] = topic
    return topic_by_slug


async def migrate_seed_quiz_titles() -> int:
    """Rename legacy em-dash quiz titles to colon style (idempotent)."""
    updated = 0
    quizzes = await Quiz.objects.filter(public=True).all()
    for quiz in quizzes:
        if " — Set " not in quiz.title:
            continue
        new_title = quiz.title.replace(" — Set ", ": Set ")
        if new_title == quiz.title:
            continue
        quiz.title = new_title
        await quiz.update()
        updated += 1
        try:
            meilisearch.index(settings().meilisearch_index).add_documents([await get_meili_data(quiz)])
        except Exception as exc:
            LOGGER.warning("Meilisearch title migrate failed for %s: %s", quiz.id, exc)
    return updated


async def run_seed(force: bool = False) -> dict:
    """Idempotent seed: certifications, topics, and public quizzes from question banks."""
    if not force and os.environ.get("CMA_CLASH_SKIP_SEED", "").lower() in ("1", "true", "yes"):
        LOGGER.info("CMA Clash seed skipped (CMA_CLASH_SKIP_SEED)")
        return {"skipped": True}
    owned_connection = False
    if not database.is_connected:
        await database.connect()
        owned_connection = True
    user = await _ensure_seed_user()
    await _ensure_demo_user()
    titles_migrated = await migrate_seed_quiz_titles()
    topic_by_slug = await _ensure_certifications_and_topics()
    facts = load_all_facts()
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for fact in facts:
        by_topic[fact["topic"]].append(fact)
    quizzes_created = 0
    questions_seeded = 0
    for topic_slug, topic_facts in sorted(by_topic.items()):
        topic = topic_by_slug.get(topic_slug)
        if topic is None:
            LOGGER.warning("Unknown topic slug in bank: %s", topic_slug)
            continue
        cert_id = _certification_uuid(topic)
        chunk_size = TOPIC_QUESTIONS_PER_QUIZ.get(topic_slug, QUESTIONS_PER_QUIZ)
        chunks = [topic_facts[i : i + chunk_size] for i in range(0, len(topic_facts), chunk_size)]
        for idx, chunk in enumerate(chunks):
            seed_slug = f"quiz:{topic_slug}:{idx + 1}"
            existing = await Quiz.objects.get_or_none(seed_slug=seed_slug)
            if existing is not None:
                questions_seeded += len(chunk)
                continue
            questions = [_fact_to_question(f) for f in chunk]
            difficulty = chunk[0].get("difficulty", "intermediate")
            title = f"{topic.name}: Set {idx + 1}"
            quiz = await Quiz(
                id=uuid.uuid4(),
                public=True,
                title=title,
                description=f"CMA Clash practice: {topic.name}. Exam-style multiple-choice questions with rationales.",
                user_id=user.id,
                questions=[q.model_dump() for q in questions],
                certification_id=cert_id,
                topic_id=topic.id,
                difficulty=difficulty,
                seed_slug=seed_slug,
                updated_at=datetime.now(),
            ).save()
            quizzes_created += 1
            questions_seeded += len(chunk)
            try:
                meilisearch.index(settings().meilisearch_index).add_documents([await get_meili_data(quiz)])
            except Exception as exc:
                LOGGER.warning("Meilisearch index update failed for %s: %s", seed_slug, exc)
    summary = {
        "quizzes_created": quizzes_created,
        "questions_in_bank": len(facts),
        "questions_accounted": questions_seeded,
        "topics": len(by_topic),
        "titles_migrated": titles_migrated,
    }
    LOGGER.info("CMA Clash seed complete: %s", summary)
    try:
        await meilisearch_init()
    except Exception as exc:
        LOGGER.warning("Meilisearch re-sync after seed failed: %s", exc)
    if owned_connection and database.is_connected:
        await database.disconnect()
    return summary


def main() -> None:
    import asyncio

    asyncio.run(run_seed())


if __name__ == "__main__":
    main()


async def seed_counts() -> dict:
    owned_connection = False
    if not database.is_connected:
        await database.connect()
        owned_connection = True
    facts = load_all_facts()
    by_topic: dict[str, int] = defaultdict(int)
    for f in facts:
        by_topic[f["topic"]] += 1
    return {"total_questions": len(facts), "per_topic": dict(by_topic)}
