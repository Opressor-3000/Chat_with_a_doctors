from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from .schemes import UserCreate, AccountUsers, AccountId
from account.models import User, Account
from doctors.models import Feedback
from doctors.models import Doctor


async def create_user(
        session: AsyncSession, 
        user: UserCreate
        ) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_account_uuid(
        session: AsyncSession, 
        uuid: uuid4
) -> Account:
    return


async def get_account_users(
        session: AsyncSession,
        account_id: AccountId,
) -> list[User]:
    return


async def get_chat_doctors(
        session: AsyncSession,
        user: User,
) -> list[Doctor]:
    return 


async def create_issue(
        session: AsyncSession,
        user: User
):
    return 


async def get_user_id(
        session: AsyncSession,
        user_id: int
) -> User:
    return 


async def get_feedback(
        session: AsyncSession,
        user_id: User,
) -> Feedback:
    return 
