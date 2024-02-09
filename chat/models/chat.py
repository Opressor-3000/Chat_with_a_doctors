from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean

if TYPE_CHECKING:
    from account.models import User
from core.models.base import Base
from doctors.models.mixin import UserDocRelationMixin
from doctors.models import Speciality


class Chat(UserDocRelationMixin, Base):
    _doc_back_populate = 'chat'
    _doc_lazy = 'joined'
    _user_back_populates = 'chat'
    _user_lazy = 'joined'

    active:Mapped[bool] =mapped_column(Boolean, default=True)
    previous_chat_id:Mapped[int] = mapped_column(
        Integer, 
        ForeignKey(
            'chat.id', 
            name='previous_chat_id', 
            ondelete='RESTRICT', 
            onupdate='RESTRICT'
            ), 
        unique=True)
    
    previous_chat:Mapped['Chat'] = relationship('Chat', back_populates='chat', remote_side=[id], uselist=False, lazy='joined')

    specialities:Mapped[list[Speciality]] = relationship('Speciality', back_populates='chat', uselist=True, lazy='selectin', secondary='doctor')

    def __repr__(self) -> str:
        return 

