from datetime import datetime

from typing import Optional, List, Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr
from .user import User

from doctors.schemes import DoctorId, CertificateID
from .disease import DiseaseID
from admin.schemes import AccessID
from doctors.schemes import SpecialityId
from .user import UserID


class AccountBase(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class AccountID(AccountBase):  #   1
    id: int
    

class CreateAccount(AccountBase):
    phone: int
    email: EmailStr | None = None
    password: bytes


class AccountInfo(AccountID):
    btk_db_id: int | None = None
    phone: int
    email: EmailStr
    password: bytes
    is_active: bool
    is_staff: bool
    certificate: List[CertificateID]
    users: List[UserID]
    diseases: List[DiseaseID]
    accesses: List[AccessID]
    specialities: List[SpecialityId]


class AccountLogin(BaseModel):
    phone: Annotated[int, MaxLen(10), MinLen(10)]
    password: str


class AccountUpdate(AccountInfo):
    btk_db_id: int | None = None
    is_active: bool | None = None
    is_staff: bool | None = None


class AccountUsers(AccessID):
    users: List[UserID]


