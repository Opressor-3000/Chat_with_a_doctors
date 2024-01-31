from sqlalchemy.ext.asyncio import AsyncSession

from account.models import User, Account
from doctors.models import Speciality, Doctor, Certificate
from chat.models import Chat, Message
from admin.models import Permission, Group, Access, QR
from admin.schemes import PermissionId, GroupId, AccessGroupId, CreateQR
from chat.schemes import ChatId, MessageID
from doctors.schemes import DoctorId, CertificateId, SpecialityId, SpecialityUpdate
from account.schemes import UserID, AccountId, AccountUpdate


async def get_user_online(
        session: AsyncSession,
) -> list[User]:
    return


async def get_messages(
        session: AsyncSession,
        chat: ChatId
) -> list[Message]:
    return 


async def get_online_doctors(
        session: AsyncSession,
        speciality: Speciality,
) -> list[Doctor]:
    return 


async def get_user_current_chat(
        session: AsyncSession,
        user: User,
) -> Chat:
    return 


async def get_users(
        session: AsyncSession,
) -> list[User]:
    return


async def get_user(
        session: AsyncSession,
        user_id: UserID,
) -> User:
    return


async def get_chat_message(
        session: AsyncSession,
        message_id: MessageID
) -> Message:
    return


async def get_delete_message(
        session: AsyncSession,
        message_id: MessageID
) -> Message:
    return


async def get_account(
        session: AsyncSession,
        account: AccountId
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


# async def doctor_update(
#         session: AsyncSession,
#         dcotor_id: D
# ) -> Doctor:
#     return


async def get_certificate(
        session: AsyncSession,
        certificate: CertificateId,
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


#admins


async def create_speciality(
        session: AsyncSession,
        permission_id: PermissionId,
) -> Speciality:
    return


async def speciality_update(
        session: AsyncSession,
        speciality_id: SpecialityUpdate,
) -> Speciality:
    return


async def create_employee(
        session: AsyncSession,
        account_id: AccountId,
) -> Permission:
    return


async def get_employees(
        session: AsyncSession,
) -> list[Permission]:
    return


async def employee_update(
        session: AsyncSession,
        permission_id: PermissionId,
) -> Permission:
    return


async def get_groups(
        session: AsyncSession,
) -> list[Group]:
    return


async def get_group_employees(
        session: AsyncSession,
        group_id: GroupId,
) -> list[Permission]:
    return


async def create_group(
        session: AsyncSession,
        permission_id: PermissionId,
) -> Group:
    return


async def group_update(
        session: AsyncSession,
        group_id: GroupId,
        employee_id: PermissionId,
) -> list[AccessGroupId]:
    return


async def get_accessgroup(
        session: AsyncSession,
        group_id: GroupId,
) -> list[Access]:
    return


async def get_accesses(
        session: AsyncSession,
        employee_id: PermissionId,
) -> list[Access]:
    return


async def create_qr(
        session: AsyncSession,
        qr: CreateQR,
        employee_id: PermissionId,
) -> QR:
    return




