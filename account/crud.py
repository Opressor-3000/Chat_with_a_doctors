from uuid import uuid4
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from account.models import User, Account
from doctors.models import Feedback, Doctor
from account.schemes import AccountID
from .schemes import UserID
from doctors.schemes import FeedbackID
from chat.models import Chat

async def create_user(session: AsyncSession, user: UserID) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_account(session: AsyncSession, account: int) -> Account:
    stmt = select(Account).where(Account.id == account)
    return await session.scalar(stmt)


async def get_account_id(session: AsyncSession, user: UserID) -> List[User]:
    stmt = select(Account.id, Account.users).where(Account.users == user)  # ?????????
    account_id = await session.scalars(stmt)
    return list(account_id)


async def create_issue(session: AsyncSession, user: int):
    return


async def get_user(session: AsyncSession, user_id: int) -> User:
    stmt = select(User.username, User.gender, User.birthday).where(User.id == user_id)
    return await session.scalar(stmt)


async def get_account_users(
        session: AsyncSession,
        account: AccountID
):
    stmt = select(User).where(User.account == account)
    users = await session.scalars(stmt)
    return users


async def get_account_feedback(
    session: AsyncSession,
    account: AccountID,
    feedback: FeedbackID
) -> Feedback:
    stmt = select(Feedback).where(Feedback.id == feedback).where(Account == account)
    return await session.scalar(stmt)


# async def get_account_feedbacks(
#     session: AsyncSession,
#     account_id: AccountID,
# ) -> list[Feedback]:
#     stmt = select(Feedback).where(Feedback.creater_id == account_id)
#     feedbacks = await session.scalars(stmt)
#     return {'feedbacks': list[feedbacks] }


async def get_chat_doctors(
        session: AsyncSession,
        user: UserID
) -> List[Account]:
    account = select(Account.users).where(Account.users == user)
    users = select(User).where(User.account == account).subquery()
    chats = select(Chat).where(Chat.user == users)
    stmt = select(Doctor).where(Doctor.chats == chats)
    doctors = await session.scalars(stmt)
    return doctors.unique()


