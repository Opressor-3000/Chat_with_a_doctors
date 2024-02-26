from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from .account import AccountID
from .gender import GenderID
from chat.schemes.chat import ChatId
from doctors.schemes.doctor import AccountDoctorData
from chat.schemes.chat import UserChats
from chat.schemes.chat import ChatUserMessageList


#  only 
class UserUpdateID(BaseModel):
    id: int


class UserIDAccount(UserUpdateID): # id
    account: Optional[AccountID]


class UserBase(BaseModel):   # 1, 2 
    username: str


    class Config:
        orm_mode = True


class UserAvatar(UserBase):
    avatar: Optional[str] = None


class User(UserBase):  #  1     username, avatar
    id: int


class UserBaseAccount(UserBase):
    account: Optional[AccountID]


'''
   ###########      USER MENU         ############
'''


class UserInfo(User): #  2   username, avatar, id
    birthday: Optional[datetime] = None
    gender_id: Optional[GenderID] = None


class UserAccountInfo(UserInfo):
    account: AccountID


class CreateUserModel(UserBase):  # username, avatar
    qr_id: Optional[int] = None


class UserAccountData(User):
    account:AccountDoctorData


class AccountUsersAdd(User): # username, avatar, id
    account_id: Optional[AccountID] = None


class CreateAccountGender(UserUpdateID): # id 
    gender:Optional[GenderID]


class UserChat(UserUpdateID): 
    chats:Optional[List[ChatId]]


class UserDoctors(UserUpdateID):
    doctors:Optional[List[AccountDoctorData]]


class UserChatListList(UserUpdateID):
    chats:Optional[List[UserChats]]


class UserChatMessagesList(UserUpdateID):
    messages:List[ChatUserMessageList]


class UserDashboardInfo(UserUpdateID):
    pass