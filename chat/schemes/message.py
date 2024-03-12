from datetime import datetime
from typing import TYPE_CHECKING

from typing import Optional


from pydantic import BaseModel

if TYPE_CHECKING:
    from account.schemes import AccountID
    from .chatuser import ChatUserID
    from .messagestatus import MessageStatusID
from .chatuser import ChatUserID


class BaseMessage(BaseModel):
    text: str
    messagestatus: 'MessageStatusID'
    created_at: datetime


class MessageID(BaseMessage):
    id: int


class MessageUserChat(BaseMessage):
    chatuser_id: 'ChatUserID'


class MessageInfo(MessageUserChat):
    id: int


class BanMessage(BaseMessage):
    creater_id: 'AccountID'
    delete: bool
    deleted_at: datetime


class CurrentMessageStatus(MessageID):
    messagestatus: 'MessageStatusID'


class MessageList(ChatUserID):  #   1
    id: int
    text: str
