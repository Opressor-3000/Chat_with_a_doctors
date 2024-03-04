from datetime import datetime

from pydantic import BaseModel

from account.schemes import AccountID
from .doctor import DoctorId


class BaseFeedback(BaseModel):
    text: str


class FeedbackID(BaseFeedback):
    id: int


class CreateBanFeedback(FeedbackID):
    creater_id: AccountID
    delete: bool
    deleted_at: datetime


class FeedbackInfo(CreateBanFeedback):
    id: int
    doctor: DoctorId