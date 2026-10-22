# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


import pydantic
from fastapi import APIRouter

from classquiz.config import settings, meilisearch
from uuid import UUID
from typing import Optional, List, Any
import logging

from meilisearch.errors import MeilisearchApiError
from classquiz.db.models import Quiz
from classquiz.helpers import meilisearch_init, get_meili_data

settings = settings()
LOGGER = logging.getLogger(__name__)

router = APIRouter()


class Hit(pydantic.BaseModel):
    id: UUID
    title: str
    description: str
    user: str
    imported_from_kahoot: Optional[bool]
    formatted: Optional["Hit"] = pydantic.Field(None, alias="_formatted")


class SearchResponse(pydantic.BaseModel):
    hits: List[Hit] | list[None]
    query: str
    limit: int
    offset: int
    processingTimeMs: int


class SearchData(pydantic.BaseModel):
    q: str
    offset: Optional[int] = 0
    limit: Optional[int] = 20
    filter: Optional[str] = None
    facetsDistribution: Optional[list[str]] = None
    attributesToRetrieve: Optional[list[str]] = ["*"]
    attributesToCrop: Optional[list[str]] = None
    cropLength: Optional[int] = 200
    attributesToHighlight: Optional[list[str]] = None
    sort: Optional[list[str]] = None


def _empty_search_result(query: str, params: dict) -> dict[str, Any]:
    return {
        "hits": [],
        "query": query,
        "limit": params.get("limit", 20),
        "offset": params.get("offset", 0),
        "processingTimeMs": 0,
    }


def _wildcard_query(query: str) -> bool:
    return query in ("*", "")


# Upper bound for the question-text scan, so a large library cannot stall a search.
_QUESTION_SCAN_LIMIT = 2000


async def _postgres_taxonomy_matches(query: str) -> list[Quiz]:
    """Public quizzes whose certification or topic name contains the query."""
    from classquiz.db.cma_models import Certification, Topic

    certifications = await Certification.objects.filter(name__icontains=query).all()
    topics = await Topic.objects.filter(name__icontains=query).all()
    cert_ids = [cert.id for cert in certifications]
    topic_ids = [topic.id for topic in topics]
    if not cert_ids and not topic_ids:
        return []
    matches: dict[Any, Quiz] = {}
    if cert_ids:
        for quiz in await Quiz.objects.filter(public=True).filter(certification_id__in=cert_ids).all():
            matches[quiz.id] = quiz
    if topic_ids:
        for quiz in await Quiz.objects.filter(public=True).filter(topic_id__in=topic_ids).all():
            matches[quiz.id] = quiz
    return list(matches.values())


async def _postgres_question_matches(query: str) -> list[Quiz]:
    """Public quizzes whose question text contains the query."""
    from classquiz.helpers import quiz_question_text

    needle = query.lower()
    matches: list[Quiz] = []
    offset = 0
    page_size = 100
    while offset < _QUESTION_SCAN_LIMIT:
        page = (
            await Quiz.objects.filter(public=True)
            .order_by("created_at")
            .offset(offset)
            .limit(page_size)
            .all()
        )
        if not page:
            break
        for quiz in page:
            if needle in quiz_question_text(quiz).lower():
                matches.append(quiz)
        offset += page_size
    return matches


async def _postgres_search(query: str, params: dict) -> dict[str, Any]:
    offset = int(params.get("offset") or 0)
    limit = int(params.get("limit") or 20)
    sort = params.get("sort") or []
    desc = any(str(s).startswith("created_at:desc") for s in sort)

    if _wildcard_query(query):
        quizzes = (
            await Quiz.objects.filter(public=True)
            .order_by("-created_at" if desc else "created_at")
            .offset(offset)
            .limit(limit)
            .all()
        )
    else:
        quizzes = (
            await Quiz.objects.filter(public=True)
            .filter(title__icontains=query)
            .offset(offset)
            .limit(limit)
            .all()
        )
        if not quizzes:
            quizzes = (
                await Quiz.objects.filter(public=True)
                .filter(description__icontains=query)
                .offset(offset)
                .limit(limit)
                .all()
            )
        if not quizzes:
            # The topic lives in the certification/topic names or in the question
            # text, so a title/description miss must not end the search.
            matches = await _postgres_taxonomy_matches(query)
            if not matches:
                matches = await _postgres_question_matches(query)
            matches.sort(key=lambda quiz: quiz.created_at, reverse=desc)
            quizzes = matches[offset : offset + limit]

    hits: list[dict[str, Any]] = []
    for quiz in quizzes:
        doc = await get_meili_data(quiz)
        hit = {
            "id": doc["id"],
            "title": doc["title"],
            "description": doc["description"] or "",
            "user": doc["user"],
            "imported_from_kahoot": doc.get("imported_from_kahoot"),
        }
        highlight = params.get("attributesToHighlight")
        if highlight and not _wildcard_query(query):
            em = f"<mark>{query}</mark>"
            hit["_formatted"] = {
                **hit,
                "title": doc["title"].replace(query, em) if query.lower() in doc["title"].lower() else doc["title"],
                "description": doc["description"] or "",
            }
        hits.append(hit)

    return {
        "hits": hits,
        "query": query,
        "limit": limit,
        "offset": offset,
        "processingTimeMs": 0,
    }


async def _meili_search(query: str, params: dict) -> dict[str, Any] | None:
    try:
        index = meilisearch.get_index(settings.meilisearch_index)
        return index.search(query, params)
    except MeilisearchApiError:
        try:
            await meilisearch_init()
            index = meilisearch.get_index(settings.meilisearch_index)
            return index.search(query, params)
        except Exception as exc:
            LOGGER.warning("Search unavailable (Meilisearch): %s", exc)
            return None
    except Exception as exc:
        LOGGER.warning("Search unavailable (Meilisearch): %s", exc)
        return None


async def _perform_search(query: str, params: dict) -> dict[str, Any]:
    meili_params = {k: v for k, v in params.items() if v is not None}
    meili_result = await _meili_search(query, meili_params)
    if meili_result is None:
        return await _postgres_search(query, params)

    hits = meili_result.get("hits") or []
    if len(hits) == 0:
        try:
            public_count = await Quiz.objects.filter(public=True).count()
        except Exception:
            public_count = 0
        if public_count > 0:
            LOGGER.info("Meilisearch returned no hits; falling back to Postgres for q=%r", query)
            return await _postgres_search(query, params)
    return meili_result


async def _search_handler(data: SearchData):
    query = await _perform_search(
        data.q,
        {
            "offset": data.offset,
            "limit": data.limit,
            "filter": data.filter,
            "cropLength": data.cropLength,
            "attributesToRetrieve": data.attributesToRetrieve,
            "attributesToCrop": data.attributesToCrop,
            "sort": data.sort,
            "attributesToHighlight": data.attributesToHighlight,
        },
    )
    return SearchResponse(**query)


@router.post("/", response_model=SearchResponse)
@router.post("", response_model=SearchResponse, include_in_schema=False)
async def search(data: SearchData):
    return await _search_handler(data)


@router.get("/", response_model=SearchResponse)
@router.get("", response_model=SearchResponse, include_in_schema=False)
async def search_get(
    q: str,
    offset: int = 0,
    limit: int = 20,
    filter: str | None = None,  # skipcq: PYL-W0622
    cropLength: int = 200,
    attributesToHighlight: Optional[str] = "*",
):
    query = await _perform_search(
        q,
        {
            "offset": offset,
            "limit": limit,
            "filter": filter,  # skipcq: PYL-W0622
            "cropLength": cropLength,
            "attributesToHighlight": [attributesToHighlight],
        },
    )
    return SearchResponse(**query)
