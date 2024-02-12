from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from .account import AccountId
from .gender import GenderID
from chat.schemes.chat import ChatId


class UserBase(BaseModel):  # поля по умолчанию
    username: str
    avatar: Optional[str] = None


    class Config:
        orm_mode = True

class UserData(UserBase):
    birthday: Optional[datetime] = None
    gender_id: Optional[GenderID] = None


class UserAccount(UserBase):
    account: Optional[AccountId]


class UserID(UserAccount):  # присваивается при входе
    id: int


class UserCreate(UserID):
    account_id: Optional[AccountId] = None
    qr_id: Optional[int] = None


class AccountUsers(UserID):
    account_id: Optional[AccountId] = None


class UserChat(UserID):
    chats:Optional[List[ChatId]]
