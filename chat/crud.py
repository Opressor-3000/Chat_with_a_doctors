from sqlalchemy import Result, select, Subquery, join, desc, label
from sqlalchemy.ext.asyncio import AsyncSession


from chat.models import Chat, Message, MessageStatus
from chat.schemes import MessageStatusID, ChatId, CurrenChatId
from account.schemes import UserID, AccountID
from doctors.models import Doctor
from account.models import Account, User


async def get_current_chat(
    session: AsyncSession,
    user_id: UserID,
):
    stmt = select(Chat.id).where(Chat.active == True).where(Chat.user == user_id)
    return session.scalar(stmt)


async def get_user_chat_list(
    session: AsyncSession,
    user_id: UserID,
) -> list[Chat]:
    stmt = (
        select(Chat.id, Chat.created_at, Chat.speciality, Chat.doctor_account)
        .where(Chat.user == user_id)
        .order_by(desc(Chat.created_at))
    )
    return session.scalars(stmt)


async def get_doctor_current_chat(
    session: AsyncSession, account_id: AccountID
) -> list[Chat]:
    # получаем account, проверяем doctor_id -> account
    # проверяем chat(active, doctor_id) -> result
    return


async def get_user_doctors(
    session: AsyncSession,
    user: UserID,
) -> list[Doctor]:
    subquery = select(Chat.id).where(Chat.id == User.chats)
    stmt = select(Doctor).where(Doctor.chats == subquery.label("user"))
    return


async def get_chat_doctor(
    session: AsyncSession,
    user_id: UserID,
) -> Doctor:
    stmt = select(Chat).where(Chat.user == user_id)
    return session.scalar(stmt)


async def get_messages_all_chats(session: AsyncSession, user: UserID):
    subquery1 = select(Account.users).where(Account.user == user.id)
    subquery = (
        select(Chat.id).where(Chat.user == subquery1).order_by(desc(Chat.created_at))
    )
    stmt = (
        select(Message.text, Message.user, Message.created_at)
        .where(Message.chat == subquery)
        .order_by(Message.created_at)
        .offset(50)
    )
    result: Result = session.execute(stmt)
    messages = result.scalars().all()
    result[messages]


async def get_chat(
    session: AsyncSession,
    chat_id: ChatId,
):
    stmt = select(Chat, list(Message)).where(Chat.id == chat_id)
    return list(session.scalars(stmt))


##################   ADMIN  ###############


async def get_all_current_chat_list(
    session: AsyncSession,
):
    stmt = (
        select(Chat.created_at, Account, User)
        .where(Chat.active == True)
        .join(Account)
        .where(Account.id == Chat.doctor_account)
        .join(User)
        .where(User == Chat.user_id)
        .order_by(desc(Chat.created_at))
        .offset(30)
    )
    result: Result = session.execute(stmt)
    return result.scalars().all()


async def get_all_current_chat_count(session: AsyncSession):
    stmt = select(Chat).where(Chat.active == True).count()
    session.execute()
