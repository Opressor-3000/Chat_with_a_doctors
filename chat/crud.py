from sqlalchemy.ext.asyncio import AsyncSession

from chat.models import Chat, Message, MessageStatus
from chat.schemes import MessageStatusID, ChatId, CurrenChatId
from account.schemes import UserID, AccountId
from doctors.models import Doctor


async def get_chat_id(
        session: AsyncSession, 
        user_id: UserID,
        chat_id: ChatId,
        ):
    return


async def get_current_chat(
        session: AsyncSession,
        user_id: UserID,
        current_chat_id: CurrenChatId,
        ):
    return


async def get_user_chats(
        session: AsyncSession,
        user_id: UserID,
        ) -> list[Chat]:
    return


async def get_doctor_current_chat(
        session: AsyncSession,
        account_id: AccountId,
        ) -> list[Chat]:
    # получаем account, проверяем doctor_id -> account 
    # проверяем chat(active, doctor_id) -> result
    return 


async def get_user_doctors(
        session: AsyncSession,
        user: UserID,
) -> list[Doctor]:
    return 


async def get_account_doctors(
        session: AsyncSession,
        account_id: AccountId,
) -> list[Doctor]:
    return


async def get_chat_doctor(
        session: AsyncSession,
        chat_id: ChatId,
) -> Doctor:
    return


