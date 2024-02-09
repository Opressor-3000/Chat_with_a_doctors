from datetime import datetime
from typing import List

from pydantic import BaseModel
from .account import AccountId
from .gender import GenderID


class UserBase(BaseModel):  # поля по умолчанию
    username: str
    avatar: str | None = None
    birthday: datetime | None = None
    gender_id: GenderID | None = None

    class Config:
        orm_mode = True


class UserID(UserBase):  # присваивается при входе
    id: int


class UserCreate(UserID):
    account_id: AccountId | None = None
    qr_id: int | None = None


class AccountUsers(UserID):
    account_id: List[AccountId] | None = None


# class UserUpdate(UserBase):
#    username: str | None = None
