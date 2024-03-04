from typing import Annotated, List


from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession


from .schemes import TokenInfo
from core.models.db_connector import db_connect
from account.schemes import AccountID, CreateAccount, AccountLogin
from account.crud import create_user
from .utils import encode_jwt, validation_auth_jwt
from .crud import get_account


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/account_auth/")
async def main_auth():
    pass


# @router.post('/add_cookie/', response_model=None, status_code=status.HTTP_201_CREATED)
# async def cookie_auth(session: AsyncSession, user_data: UserCreate):
#     await create_user(session=session, user=user_data)
#     return RedirectResponse(url='api/v1/chat/', status_code=status.HTTP_302_FOUND)


@router.get("/")  # страница для отправки сообщения и регистрации
async def create_user(
    token: str | None = None, cookie: str | None = None, username=None
):
    """
    возвращает all chats user order_by(created_at)
     all message chats order_by(created_at) если есть:
        1. Bearer token -> account with DB, а иначе
        2. user в DB с таким cookie, а иначе
        3. create cookie and create new User and redirect
        4. для отправки сообщения просит ввести имя
    """
    pass


@router.post("/jwt_singin/")
async def account_singin(
    session: AsyncSession = Depends(db_connect.scope_session_dependency),
    account: CreateAccount = Depends(validation_auth_jwt),
):
    unregister_exc = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Register Except Message"
    )


@router.post("/jwt_login/")
async def auth_account_jwt(
    session: AsyncSession = Depends(db_connect.scope_session_dependency),
    login_data: AccountLogin = Depends(validation_auth_jwt()),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="incorrectly entered phone number and/or password",
    )
    validate_data = validation_auth_jwt(session=session, login_data=login_data)
    if not validate_data:
        raise unauthed_exc
    jwt_payload = {
        "account": login_data.first_name,
    }
    token = encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )
