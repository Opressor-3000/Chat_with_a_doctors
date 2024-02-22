from datetime import datetime

from pydantic import BaseModel

from chat.schemes import ChatId
from doctors.schemes.doctor import DoctorId
from account.schemes.user import User


class BaseRating(BaseModel):
    user_id: User
    chat_id: ChatId
    doctor_id: DoctorId
    point: int


class RatingID(BaseRating):
    id: int
