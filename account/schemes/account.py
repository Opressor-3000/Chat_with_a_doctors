from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .user import UserID

from doctors.schemes.doctor import DoctorId
from .disease import DiseaseID
from admin.schemes import Accessid
from chat.schemes.chat import ChatId


class AccountBase(BaseModel):
   first_name: str
   last_name: str
   phone: int
   email: EmailStr | None = None

   class Config:
      orm_mode = True


class AccountId(AccountBase):
   id: int


class AccountMessages(AccountId):
   messages:Optional[List[ChatId]]


class CreateAccount(AccountBase):
   password: bytes


class AccountUpdate(AccountBase):
   first_name: str | None = None
   last_name: str | None = None
   email: EmailStr | None = None


class ChangePassword(BaseModel):
   phone: int | None = None
   password: bytes


class AccountUsers(AccountBase):
   users: Optional[List[UserID]]


class AccountDoctor(AccountBase):
   doctor_id:Optional[DoctorId]


class AccountDisease(AccountBase):
   diseases:Optional[List[DiseaseID]]


class AccountAccesses(AccountBase):
   accesses:Optional[List[Accessid]]


class AccountBTKID(AccountBase):
   btk_db:Optional[int]


class AccountActiveStatus(AccountBase):
   is_active:bool


class AccountStaffStaus(AccountBase):
   is_staff:bool


class AccountFullData(AccountId):
   doctor_id:Optional[DoctorId]
   accesses:Optional[List[Accessid]]
   btk_db:Optional[int]
   is_active:bool
   is_staff:bool