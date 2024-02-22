
from account.schemes.user import User
from pydantic import BaseModel
from chat.schemes import ChatId
from account.schemes import UserAccount


class BaseChatUser(BaseModel):  #  1
   user_id: User


class ChatUserChatId(BaseChatUser):
   chat_id:ChatId


class ChatUserId(BaseChatUser): #  1
   id: int


class CreateChatUser(BaseChatUser):
   pass


class ChatUserList():
   pass

