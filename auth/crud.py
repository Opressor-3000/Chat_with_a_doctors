from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Cookie


from .schemes import AuthJWTScheme
from core.models.db_connector import db_connect
from account.schemes import UserID
from auth.utils import COOKIE_SESSION_ID
from account.models import Account
from account.models import User


async def create_account(
        session: AsyncSession,
        first_name: str,
        last_name: str,
        phone: int,
        email: str | None = None
        ) -> Account:
    account = Account(**create_account.model_dump())
    session.add(account)
    await session.commit()
    return account


async def create_user(
        session: AsyncSession, 
        user: UserID,
        ) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user
