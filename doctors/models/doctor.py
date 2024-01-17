from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from account.models import CreaterRelationMixin, Account
from chat.models import Chat
from .speciality import Speciality


class Doctor(CreaterRelationMixin, Base):
    account_id:Mapped[int] = mapped_column(ForeignKey('account.id')) # create if exist current sertificate CHECH
    speciality:Mapped[int] 

    account:Mapped['Account'] = relationship(back_populates='account.id')


class Feedback(Base):
    chat_id: Mapped[int]
    doctor_id:Mapped[int]
    user_id:Mapped[int]


class Rating(Base):
    chat_id:Mapped[int]
    point:Mapped[int]
