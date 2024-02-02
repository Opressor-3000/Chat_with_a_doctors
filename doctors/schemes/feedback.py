from datetime import datetime

from pydantic import BaseModel

from chat.schemes import ChatId
from account.schemes import UserID
from admin.schemes import PermissionId
from .doctor import DoctorId


class BaseFeedback(BaseModel):
    chat_id: ChatId
    dcotor_id: DoctorId
    user_id: UserID
    text: str


class FeedbackID(BaseFeedback):
    id: int


class BanFeedback(FeedbackID):
    creater_id: PermissionId
    delete: bool
    deleted_at: datetime
