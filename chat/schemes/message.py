from datetime import datetime


from typing import Optional


from pydantic import BaseModel
from admin.schemes import PermissionId
from chat.schemes.chatuser import ChatUserId
from .chatuser import ChatUserAccount
from .messagestatus import MessageStatusID


class BaseMessage(BaseModel):
    text: str
    messagestatus: MessageStatusID


class MessageID(BaseMessage):
    id: int


class MessageUserChat(BaseMessage):
    chatuser_id: ChatUserId


class MessageInfo(MessageUserChat):
    id: int

class BanMessage(BaseMessage):
    creater_id: PermissionId
    delete: bool
    deleted_at: datetime


class CurrentMessageStatus(MessageID):
    messagestatus: MessageStatusID


class MessageList(ChatUserId):  #   1
    id: int
    text: str
