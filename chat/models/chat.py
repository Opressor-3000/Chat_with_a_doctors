from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from core.models.base import Base
from account.models import UserRelationMixin
from doctors.models import UserDocSpecMixin
from account.models import CreaterRelationMixin


class Chat(UserDocSpecMixin, Base):
    active:Mapped[bool]
    previous_chat:Mapped[int] = mapped_column(ForeignKey('chat.id'), unique=True)


class ChatUser(UserRelationMixin, Base):
    _user_back_populates = 'chatuser'

    chat_id:Mapped[int] = mapped_column(ForeignKey('chat.id'), nullable=False)

    chat:Mapped['Chat'] = relationship('Chat', back_populates='chatuser')
    


class Status(CreaterRelationMixin, Base):
    _creater_nullable = 'status'

    title: Mapped[str] = mapped_column(String(50), unique=True)



