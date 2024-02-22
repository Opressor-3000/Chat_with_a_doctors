from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Cookie


from .schemes import AuthJWTScheme
from core.models.db_connector import db_connect
from account.schemes import User as UserSchemas
from auth.utils import COOKIE_SESSION_ID
from account.models import Account
from account.models import User as UserModel
from account.schemes import CreateAccount, AccountId


async def create_account(
    session: AsyncSession,
    create_account: CreateAccount,
) -> Account:
    account = Account(**create_account.model_dump())
    if await account_validate(session, account):
        session.add(account)
        await session.commit()
        return account
    else:
        return "an account with this number has already been registered"


async def create_user(
    session: AsyncSession,
    user: UserSchemas,
) -> UserModel:
    user = UserModel(**user.model_dump())
    session.add(user)
    await session.commit()
    return user


async def account_validate(
    session: AsyncSession,
    account: CreateAccount,
) -> bool:
    stmt = select(Account).where(Account.phone == account.phone)
    if await session.scalar(stmt):
        return True
    else:
        return False
