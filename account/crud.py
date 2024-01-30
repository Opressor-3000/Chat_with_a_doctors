from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Cookie
from main import COOKIE_SESSION_ID
from core.models.db_connector import db_connect
from .schemes import UserCreate
from .models import User


async def get_user_cookie(
        session = db_connect.get_scope_session, 
        user_cookie: str = Cookie(alias=COOKIE_SESSION_ID),
        ) -> User | None:
    stmt = select(User).filter_by(cookie = user_cookie)
    return await session.execute(stmt)


async def create_user(
        session: AsyncSession, 
        user: UserCreate
        ) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user

