# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0


from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from classquiz.auth import get_admin_user
from classquiz.db.models import User
from classquiz.services.user_deletion import (
    delete_user_by_email as delete_user_by_email_service,
    delete_user_by_id as delete_user_by_id_service,
    delete_user_by_username as delete_user_by_username_service,
)

router = APIRouter()


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
