
from typing import Optional

from pydantic import BaseModel


class BaseChat(BaseModel):
   user_id: int
   previous_chat_id: Optional[int] = None


class CreateChat(BaseChat):
   pass


class ChatId(BaseChat):
   id: int


class CurrenChatId(ChatId):
   active: bool