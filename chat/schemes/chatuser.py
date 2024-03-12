from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
   from chat.schemes import ChatId
   from account.schemes import UserID


class BaseChatUser(BaseModel):  #  1
   user_id: 'UserID'


class ChatUserChatId(BaseChatUser):
   chat_id:'ChatId'


class ChatUserID(BaseChatUser): #  1
   id: int


class CreateChatUser(BaseChatUser):
   pass


class ChatUserList():
   pass

