from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean, DateTime, String


from core.models.base import Base
from .mixin import ChatUserRelationMixin
from doctors.models.cucr_mixin import ChatUserCreaterRelationMixin


class Message(ChatUserCreaterRelationMixin, Base):
    _chatuser_back_populate = 'message'
    _creater_back_populates = 'message'
    
    text:Mapped[str] = mapped_column(String(512),)
    delete:Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at:Mapped[datetime] = mapped_column(DateTime)


class MessageStatus(ChatUserRelationMixin, Base):
    _chatuser_back_populate = 'messagestatus'

    message_id:Mapped[int] = mapped_column(Integer, ForeignKey('message.id', name='message_status'), unique=True)
    received:Mapped[datetime] = mapped_column(DateTime)
    read:Mapped[datetime] = mapped_column(DateTime)

    message:Mapped['Message'] = relationship('Message', back_populates='messagestatus')


