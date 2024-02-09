from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from .schemes.user import UserCreate
from account.schemes import  AccountId
from account.models import User, Account
from doctors.models import Feedback
from .schemes.user import UserID


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


async def create_issue(
        session: AsyncSession,
        user: UserID
):
    return 


async def get_user(
        session: AsyncSession,
        user_id: int
) -> User:
    return 


async def get_account_feedback(
        session: AsyncSession,
        user_id: UserID,
) -> Feedback:
    return 


async def get_account_feedbacks(
        session: AsyncSession,
        account_id: AccountId,
) -> list[Feedback]:
    return
