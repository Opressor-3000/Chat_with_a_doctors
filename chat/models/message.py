from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean, DateTime


from core.models.base import Base
from .mixin import ChatUserRelationMixin
from .chatuser import ChatUser
from doctors.models.mixin_1 import ChatUserCreaterRelationMixin


class Message(ChatUserCreaterRelationMixin, Base):
    _chatuser_back_populate = 'message'
    _creater_back_populates = 'message'
    
    text:Mapped[int] = mapped_column(Integer)
    delete:Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at:Mapped[datetime] = mapped_column(DateTime)


class MessageStatus(ChatUserRelationMixin, Base):
    _chatuser_back_populate = 'messagestatus'

    message_id:Mapped[int] = mapped_column(ForeignKey('message.id'), unique=True)
    received:Mapped[datetime] = mapped_column()
    read:Mapped[datetime] = mapped_column()

    message:Mapped['Message'] = relationship('Message', back_populates='messagestatus')


