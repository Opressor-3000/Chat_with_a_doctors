from typing import List

from sqlalchemy import Result, select, join, label
from sqlalchemy.ext.asyncio import AsyncSession

from account.models import User, Account, Disease

from doctors.models import Speciality, Doctor, Certificate
from chat.models import Chat, Message
from admin.models import Access, QR
from admin.schemes import CreateQR
from chat.schemes import ChatId, MessageID
from doctors.schemes import (
    DoctorId,
    CertificateID,
    SpecialityId,
    SpecialityUpdate,
    CreateSpeciality,
)
from account.schemes import (
    UserID,
    AccountID,
    AccountUpdate,
)


async def get_user_online(
    session: AsyncSession,
) -> list[User]:
    ###  NEED WEBSOCKET
    return


async def get_chat_messages(session: AsyncSession, chat: ChatId) -> list[Message]:
    return


async def get_online_doctors(
    session: AsyncSession,
    speciality: Speciality,
) -> list[Doctor]:
    ###   NEED WEBSOCKET
    return


async def get_users(
    session: AsyncSession,
) -> List[User]:
    # ADMINS
    stmt = select(User).offset(100)
    user: Result = await session.scalars(stmt)
    return list(user.all())


async def get_user(
    session: AsyncSession,
    user_id: UserID,
) -> User:
    #  ADMINS
    subquery = select(Disease.title).where()
    stmt = (
        select(
            User,
            User.avatar,
            Account,
            list(Disease),
            Chat,
            Doctor,
            Account.speciality,
        )
        .where(User=user_id)
        .join(Account)
        .where(Account.users == user_id)
        .join(Disease)
        .where()
        .join(User)
    )

    return


async def get_chat_message(
    session: AsyncSession,
    message_id: MessageID,
) -> Message:
    return


async def get_delete_message(
    session: AsyncSession,
    message_id: MessageID,
) -> Message:
    return


async def get_account(
    session: AsyncSession,
    account: AccountID,
) -> Account:
    return


async def get_accounts(
    session: AsyncSession,
) -> list[Account]:
    return


async def account_update(
    session: AsyncSession,
    account_id: AccountUpdate,
) -> Account:
    return


async def get_doctor(
    session: AsyncSession,
    doctor_id: DoctorId,
) -> Doctor:
    return


async def get_certificate(
    session: AsyncSession,
    certificate: CertificateID,
) -> Certificate:
    return


async def get_speciality(
    session: AsyncSession,
) -> Speciality:
    return


async def get_specialities(
    session: AsyncSession,
) -> list[SpecialityId]:
    return


##############    admins     ##############


async def create_speciality(
    session: AsyncSession, speciality: CreateSpeciality
) -> Speciality:
    new_spec = Speciality(**speciality.model_dump())
    session.add(new_spec)
    await session.commit()
    return await session.refresh(new_spec)


async def speciality_update(
    session: AsyncSession,
    speciality_id: SpecialityUpdate,
) -> Speciality:
    return


async def create_employee(
    session: AsyncSession,
    account_update: AccountID,
    partial: bool = False,
) -> Account:
    account = Account()
    for name, value in Account(**account_update.model_dump().item()):
        setattr(account, name, value)
    await session.commit()
    return


async def get_employees(
    session: AsyncSession,
) -> list[Account]:
    return


async def employee_update(
    session: AsyncSession,
    account_update: AccountID,
) -> Account:
    account = Account(**account_update.model_dump())
    return


async def create_qr(
    session: AsyncSession,
    qr: CreateQR,
) -> QR:
    qr = select(QR)
    result: Result = await session.scalars(qr)
    return result.all()


accesses = (
    "user activation",
    "account activation",
    "message activation",
    "chat activation",
    "doctor activation",
    "create doctor",
    "create certificate",
    "create sertificate",
    "create agency",
    "edit doctor",
    "edit certificate",
    "edit speciality",
    "edit agency",
    "assing access",
    "revoke access",
    "create desease",
    "edit desease",
    "insert QR",
    "singular",
    
    "statistic",
    'doctorinfo',
    'userinfo',
    'accountstat',
    'userstate',
)
