
from typing import Optional, List

from pydantic import BaseModel
from doctors.schemes.doctor import DoctorId
from doctors.schemes.speciality import SpecialityId
from account.schemes.account import AccountId
from account.schemes.user import UserID
from .message import MessageID


class BaseChat(BaseModel):
   user_id: UserID
   doctor_id: Optional[DoctorId]
   speciality_id: Optional[SpecialityId]
   previous_chat_id: Optional[int] = None


class CreateChat(BaseChat):
   pass


class ChatId(BaseChat):
   id: int


class ChatMessage(BaseModel):
   messages:List[MessageID]


class CurrenChatId(ChatId):
   active: bool