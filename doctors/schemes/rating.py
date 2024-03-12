from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from chat.schemes import ChatId
    from doctors.schemes import DoctorId
    from account.schemes import UserID


class BaseRating(BaseModel):
    point: int


class RatingID(BaseRating):
    id: int


class CreateRating(BaseModel):
    user_id: 'UserID'
    chat_id: 'ChatId'
    doctor_id: 'DoctorId'


class Ratingnfo(CreateRating):
    id:int