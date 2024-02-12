from datetime import datetime

from typing import Optional

from pydantic import BaseModel
from chat.schemes import ChatUserId, MessageID


class MessageStatusBase(BaseModel):
   chatuser_id: ChatUserId
   message_id: MessageID
   received: Optional[datetime]
   read: Optional[datetime]
   

class MessageStatusID(BaseModel):
   id: int

