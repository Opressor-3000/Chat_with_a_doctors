from datetime import datetime

from typing import Optional, List, Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr
from .user import User

from doctors.schemes import DoctorId
from .disease import DiseaseID
from admin.schemes import Accessid
from chat.schemes import ChatId
from .user import User


class AccountBase(BaseModel):  #  1
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class CreateAccount(AccountBase):
    phone: int
    email: EmailStr
    password: bytes


class AccountID(AccountBase):
    btk_db_id: int | None = None
    phone: int
    email: EmailStr
    password: bytes
    is_active: bool
    is_staff: bool
    

class AccountLogin(BaseModel):
    phone: Annotated[int, MaxLen(10), MinLen(10)]
    password: str


class AccountAddBTKID(AccountID):
    btk_db_id: int


class SetAccountActive(AccountID):
    is_active: bool


class SetAccountIsStaff(AccountID):
    is_staff: bool