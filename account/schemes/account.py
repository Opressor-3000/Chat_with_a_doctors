from datetime import datetime

from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .user import User

from doctors.schemes.doctor import DoctorId
from .disease import DiseaseID
from admin.schemes import Accessid
from chat.schemes.chat import ChatId
from .user import User


class AccountIDforUpdate(BaseModel):
    id: int


class AccountBase(BaseModel):  #  1
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


"""
   ##############    ACCOUNT  MENU    ###############
"""


class AccountId(AccountBase):  #  1     id, first_name, last_name,
    id: int
    last_enter: datetime
    btk_db_id: int | None
    phone: int 
    email: EmailStr | None
    password: bytes
    is_active: bool
    is_staff:  bool


class AccountUserChatList(AccountId):  #
    messages: Optional[List[ChatId]]


class CreateAccount(AccountBase):
    phone: int
    email: Optional[str] = None
    password: bytes


class AccountUpdate(AccountBase):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class ChangePassword(BaseModel):
    phone: int | None = None
    password: bytes


class AccountUsers(AccountBase):
    users: List[User]


class AccountDoctor(AccountBase):
    doctor_id: Optional[DoctorId]


class AccountDisease(AccountBase):
    diseases: Optional[List[DiseaseID]]


class AccountAccesses(AccountBase):
    accesses: Optional[List[Accessid]]


class AccountBTKID(AccountBase):
    btk_db: Optional[int]


class AccountActiveStatus(AccountBase):
    is_active: bool


class AccountStaffStaus(AccountBase):
    is_staff: bool


class AccountFullData(AccountId):
    doctor_id: Optional[DoctorId]
    accesses: Optional[List[Accessid]]
    btk_db: Optional[int]
    is_active: bool
    is_staff: bool


class AccountDoctorChat(AccountDoctor):
    chats: Optional[List[ChatId]]
