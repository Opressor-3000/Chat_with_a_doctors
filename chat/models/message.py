from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


from core.models.base import Base
from .mixin import ChatUserRelationMixin
from .chatuser import ChatUser
from doctors.models.mixin_1 import ChatUserDocRelationMixin


class Message(ChatUserDocRelationMixin, Base):
    _chatuser_back_populate = 'message'
    _creater_back_populates = 'message'

    text:Mapped[int] = mapped_column()
    delete:Mapped[bool] = mapped_column(default=False)
    deleted_at:Mapped[datetime]


class MessageStatus(ChatUserRelationMixin, Base):
    message_id:Mapped[int] = mapped_column(ForeignKey('message.id'), unique=True)
    chatuser_id:Mapped[int] = mapped_column(ForeignKey('chatuser.id'), unique=True)
    received:Mapped[datetime] = mapped_column()
    read:Mapped[datetime] = mapped_column()

    message:Mapped['Message'] = relationship('Message', back_populates='messagestatus')
    chatuser:Mapped['ChatUser'] = relationship('ChatUser', back_populates='messagestatus')

