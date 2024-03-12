from typing import TYPE_CHECKING
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Cookie, HTTPException, status


from core.models.db_connector import db_connect
from account.schemes import (
    UserID as UserSchemas,
    CreateAccount,
    AccountID,
)
from auth.utils import COOKIE_SESSION_ID
if TYPE_CHECKING:
    from account.models import Account, User as UserModel


async def get_account(
    session: AsyncSession,
    account: AccountID,
) -> 'Account':
    stmt = select(Account).where(Account.phone == account.phone)
    return await session.execute(stmt)


#    >>>>>>>>>>>>>>>>     CREATE    ACCOUNT    <<<<<<<<<<<<<<<<


async def create_account(
    session: AsyncSession,
    create_account: CreateAccount,
) -> 'Account':
    account = Account(**create_account.model_dump())
    if await get_account(session, create_account):
        session.add(account)
        await session.commit()
        return account
    else:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ian account with this number has already been registered",
        )


async def create_user(
    session: AsyncSession,
    user: UserSchemas,
) -> 'UserModel':
    user = UserModel(**user.model_dump())
    session.add(user)
    await session.commit()
    return user
