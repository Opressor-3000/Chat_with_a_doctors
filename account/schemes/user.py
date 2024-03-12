from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from pydantic import BaseModel
if TYPE_CHECKING:
    from .account import AccountID
    from .gender import GenderID
    from chat.schemes import UserChats, ChatUserMessageList, ChatId


class UserBase(BaseModel):  # 1, 2
    username: str

    class Config:
        orm_mode = True


class UserIDAccount(UserBase):  # id
    account: Optional['AccountID']


class UserAvatar(UserBase):
    avatar: Optional[str] = None


class UserID(UserBase):  #  1     username, avatar
    id: int


class UserBaseAccount(UserID):  # 2
    account: Optional["AccountID"]


"""
   ###########      USER MENU         ############
"""


class UserInfo(UserID):  #  2   username, avatar, id
    birthday: Optional[datetime] = None
    gender_id: Optional["GenderID"] = None


class UserAccountInfo(UserInfo):
    account: 'AccountID'


class CreateUser(UserBase):  # username, avatar
    qr_id: Optional[int] = None


class UserAccountData(UserID):
    account: 'AccountID'


class AccountUsersAdd(UserID):  # username, avatar, id
    account_id: Optional['AccountID'] = None


class CreateAccountGender(UserID):  # id
    gender: Optional['GenderID']


class UserChat(UserID):
    chats: Optional[List['ChatId']]


class UserDoctors(UserID):
    doctors: Optional[List['AccountID']]


class UserChatListList(UserID):
    chats: Optional[List['UserChats']]


class UserChatMessagesList(UserID):
    messages: List['ChatUserMessageList']


class UserDashboardInfo(UserID):
    pass
