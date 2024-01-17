from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from core.models.base import Base
from doctors.models import UserDocSpecMixin
from account.models import CreaterRelationMixin


class Chat(UserDocSpecMixin, Base):
    active:Mapped[bool]
    previous_chat:Mapped[int] = mapped_column(ForeignKey('chat.id'), unique=True)


class ChatUser(Base):
    chat_id:Mapped[int]
    user_id:Mapped[int]


class Status(CreaterRelationMixin, Base):
    title: Mapped[str] = mapped_column(String(50))



