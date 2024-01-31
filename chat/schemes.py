from datetime import datetime

from pydantic import BaseModel
from account.crud import User
from admin.schemes import PermissionId


#  -------------------   CHAT    ---------------------

class BaseChat(BaseModel):
   user_id: User
   previous_chat_id: 'BaseChat' | None


class CreateChat(BaseChat):
   pass


class ChatId(BaseChat):
   id: int


class CurrenChatId(ChatId):
   active: True

#  ------------------------  CHAT USER  ----------------------


class BaseChatUser(BaseModel):
   user_id: User
   chat_id: ChatId


class ChatUserId(BaseChatUser):
   id: int


class CreateChatUser(BaseChatUser):
   pass


#  ------------------   MESSAGE  --------------------


class BaseMessage(BaseModel):
   chatuser_id: ChatUserId
   text: str
   

class MessageID(BaseMessage):
   id: int


class BanMessage(BaseMessage):
   creater_id: PermissionId
   delete:bool
   deleted_at: datetime


#  -----------------------  MESSAGE STATUS   ---------------------


class MessageStatus(BaseModel):
   chatuser_id: ChatUserId
   message_id: MessageID
   received: datetime
   read: datetime
   

class MessageStatusID(BaseModel):
   id: int

