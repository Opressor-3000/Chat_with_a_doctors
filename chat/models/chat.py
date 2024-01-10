from datetime import datetime

from sqlalchemy.orm import Mapped


from core.models.base import Base



class Chat(Base):
    created_at: Mapped[int]
    user_created: Mapped[datetime]


class UserOfChat(Base):
    chat_id:Mapped[int]
    user_id:Mapped[int]


class Message(Base):
    chat_id:Mapped[int]
    user_chat: Mapped[int]
    text:Mapped[int]
    created_at:Mapped[datetime]
    deleted_at:Mapped[datetime]
    user_deleted:Mapped[int]


class Status(Base):
    title: Mapped[str]
    user_id: Mapped[int]
    created_at: Mapped[datetime]


class MessageStatus(Base):
    message_id:Mapped[int]
    chat_user:Mapped[int]
    status_id:Mapped[int]
    created_at:Mapped[datetime]
