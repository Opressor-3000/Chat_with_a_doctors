from datetime import datetime

from pydantic import BaseModel

from chat.schemes import ChatId
from doctors.schemes.doctor import DoctorId
from account.schemes.user import UserID


class BaseRating(BaseModel):
    user_id: UserID
    chat_id: ChatId
    doctor_id: DoctorId
    point: int


class RatingID(BaseRating):
    id: int
