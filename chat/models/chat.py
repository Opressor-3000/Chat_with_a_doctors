from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean

from core.models.base import Base
from doctors.models.mixin import UserDocRelationMixin


class Chat(UserDocRelationMixin, Base):
    _doc_back_populate = 'chat'
    _user_back_populates = 'chat'

    active:Mapped[bool] =mapped_column(Boolean, default=True)
    previous_chat_id:Mapped[int] = mapped_column(Integer, ForeignKey('chat.id'), unique=True)
    
    previous_chat:Mapped['Chat'] = relationship('Chat', back_populates='chat', remote_side=[id])


