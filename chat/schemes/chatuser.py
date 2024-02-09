
from account.schemes.user import UserID
from pydantic import BaseModel
from chat.schemes import ChatId


class BaseChatUser(BaseModel):
   user_id: UserID
   chat_id: ChatId


class ChatUserId(BaseChatUser):
   id: int


class CreateChatUser(BaseChatUser):
   pass


