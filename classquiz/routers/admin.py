# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from ormar import or_
from pydantic import BaseModel

from classquiz.auth import get_admin_user, get_site_admin_user
from classquiz.db.models import Quiz, User
from classquiz.services.user_deletion import (
    delete_user_by_email as delete_user_by_email_service,
    delete_user_by_id as delete_user_by_id_service,
    delete_user_by_username as delete_user_by_username_service,
)

router = APIRouter()

MAX_ADMIN_USER_PAGE_SIZE = 50


class AdminMeResponse(BaseModel):
    id: UUID
    email: str
    username: str


class AdminUserListItem(BaseModel):
    id: UUID
    username: str
    email: str
    verified: bool
    created_at: datetime
    quiz_count: int


class AdminUserListResponse(BaseModel):
    items: list[AdminUserListItem]
    page: int
    page_size: int
    total: int


@router.get("/me", response_model=AdminMeResponse)
async def admin_me(user: User = Depends(get_site_admin_user)) -> AdminMeResponse:
    return AdminMeResponse(id=user.id, email=user.email, username=user.username)


@router.get("/users", response_model=AdminUserListResponse)
async def list_admin_users(
    q: str = "",
    page: int = 1,
    page_size: int = MAX_ADMIN_USER_PAGE_SIZE,
    _: User = Depends(get_site_admin_user),
) -> AdminUserListResponse:
    page = max(1, page)
    page_size = min(max(1, page_size), MAX_ADMIN_USER_PAGE_SIZE)
    queryset = User.objects
    term = q.strip()
    if term:
        queryset = queryset.filter(or_(username__icontains=term, email__icontains=term))
    total = await queryset.count()
    users = (
        await queryset.order_by(User.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    items: list[AdminUserListItem] = []
    for row in users:
        quiz_count = await Quiz.objects.filter(user_id=row.id).count()
        items.append(
            AdminUserListItem(
                id=row.id,
                username=row.username,
                email=row.email,
                verified=row.verified,
                created_at=row.created_at,
                quiz_count=quiz_count,
            )
        )
    return AdminUserListResponse(items=items, page=page, page_size=page_size, total=total)


@router.delete("/user/id")
async def delete_user_by_id(user_id: UUID, _: User = Depends(get_admin_user)):
    result = await delete_user_by_id_service(user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@router.delete("/user/username")
async def delete_user_by_username(username: str, _: User = Depends(get_admin_user)):
    result = await delete_user_by_username_service(username)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@router.delete("/user/email")
async def delete_user_by_email(email: str, _: User = Depends(get_admin_user)):
    result = await delete_user_by_email_service(email)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result
