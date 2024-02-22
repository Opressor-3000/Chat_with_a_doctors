from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel
from doctors.schemes.doctor import DoctorId
from doctors.schemes.speciality import SpecialityId
from account.schemes.account import AccountId
from account.schemes.user import UserInfo
from .message import MessageList, MessageInfo, MessageUserChat
from .message import CurrentMessageStatus
from .chatuser import ChatUserId



class ChatId(BaseModel):  # chat_id
    id: int


class BaseChat(BaseModel):  # doctor_id, list[speciality_id]
    doctor_id: Optional[DoctorId]
    

class ChatSpeciality(BaseChat):
    speciality_id: Optional[SpecialityId]


class ChatInfo(BaseChat):  # id, doctor_id, list[speciality_id]
    id: int


class DoctorChatList(ChatId):
    chatusers: List[ChatUserId]


class CreateChat(BaseChat):  # doctor_id, list[speciality_id]
    pass


class ChatUsers(ChatId):
    user: List[ChatUserId]


class CurrenChatId(ChatId):
    active: bool


class UserChats(ChatId):
    """ """

    created_at: datetime


class UserChat(ChatId):
    chatuser: list[ChatUserId]


class ChatIdForDoctor(ChatId):
    chatuser: List


class ChatUserMessageList(CurrentMessageStatus):
    text: str


#################################################################################################################


#    Содержание одного чата


class UserChatMessageDoctor(BaseModel):    #  1 
    doctor: Optional[DoctorId]
    message: MessageList


#    Список чатов с содержанием (сообщения в хронологическом порядке, имя доктора)


class AllMessagesFromAllUserChats(BaseModel):   #  1
    chats: Optional[List[UserChatMessageDoctor]]


#  -------------------------------------------------------------------------------------------------
    

class ChatUsernameMessage(ChatId):
    user: UserInfo
    message: List[MessageInfo]


class DoctorCurrentChatList(BaseModel):
    chats: Optional[List[ChatUsernameMessage]]