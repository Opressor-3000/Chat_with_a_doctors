from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from admin.models.mixin import CreaterRelationMixin
from .doctor import Doctor
from account.models import Account
from chat.models import Chat


class Speciality(CreaterRelationMixin, Base):
    _creater_back_populates = 'speciality'
    _creater_lazy = 'joined'


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)

    doctors: Mapped[list[Doctor]] = relationship('Doctor', back_populates='speciality', uselist=True, lazy='joined')
    chats:Mapped[list[Chat]] = relationship('Chat', back_populates='speciality', uselist=True, secondary='doctor', lazy='joined')

    def __repr__(self) -> str:
        return f'{self.title}'


