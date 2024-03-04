from datetime import datetime

from pydantic import BaseModel

from chat.schemes import ChatId
from doctors.schemes.doctor import DoctorId
from account.schemes import UserID


class BaseRating(BaseModel):
    point: int


class RatingID(BaseRating):
    id: int


class CreateRating(BaseModel):
    user_id: UserID
    chat_id: ChatId
    doctor_id: DoctorId


class Ratingnfo(CreateRating):
    id:int