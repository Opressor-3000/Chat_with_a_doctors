from typing import Annotated, List

from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from account.schemes.user import UserCreate
from account.crud import create_user
from account.models import User
from chat.schemes.schemes import ChatId


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/account_auth/')
async def set_auth(phone):
    pass


@router.get('/comfirmation_phone/')
async def get_phone():
    pass


@router.post('/comfirmation_phone/')
async def comfirmation_phone():
    pass


# @router.post('/add_cookie/', response_model=None, status_code=status.HTTP_201_CREATED)
# async def cookie_auth(session: AsyncSession, user_data: UserCreate):
#     await create_user(session=session, user=user_data)
#     return RedirectResponse(url='api/v1/chat', status_code=status.HTTP_302_FOUND)


@router.post('/autorization/')
async def autorization():
    pass


