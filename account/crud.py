from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from account.models import User, Account
from doctors.models import Feedback
from account.schemes import AccountID
from .schemes import UserID


async def create_user(session: AsyncSession, user: int) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_account_data(session: AsyncSession, account: int) -> Account:
    stmt = select(list(Account)).where(Account.id == account)
    return session.scalar(stmt)


async def get_account_id(session: AsyncSession, user: UserID) -> list[User]:
    stmt = select(Account.id, Account.users).where(Account.users == user)  # ?????????
    return session.scalar(stmt)


async def create_issue(session: AsyncSession, user: int):
    return


async def get_user(session: AsyncSession, user_id: int) -> User:
    return


async def get_account_feedback(
    session: AsyncSession,
    user_id: int,
) -> Feedback:
    return


async def get_account_feedbacks(
    session: AsyncSession,
    account_id: AccountID,
) -> list[Feedback]:
    return
