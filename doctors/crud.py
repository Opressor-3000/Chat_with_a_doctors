from typing import List

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from .models import Doctor
from .schemes import DoctorId
from chat.models import Chat
from chat.schemes import ChatId
from account.schemes import AccountID, UserID
from account.models import Account, User


async def get_doctor_profile(session: AsyncSession, doctor_id: DoctorId) -> Doctor:
    return await session.get(Doctor, doctor_id)


async def get_doctor_chats(
    session: AsyncSession,
    doctor_id: DoctorId,
) -> list[Chat]:
    stmt = (
        select(Chat, ChatId)
        .where(Chat.doctor_id == doctor_id)
        .order_by(Chat.created_at)
    )
    result: Result = session.execute(stmt)
    doctor_chat = result.scalars().all()
    return list(doctor_chat)


async def get_doctor_pasients(
    session: AsyncSession,
    doctor_id: DoctorId,
) -> list[User]:
    chat_list = get_doctor_chats(session=session, doctor_id=doctor_id)
    stmt = select(User, chat_list).where()
    return
