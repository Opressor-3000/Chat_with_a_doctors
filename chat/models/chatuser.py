from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .chat import Chat
from core.models.base import Base
from account.models.mixin import UserRelationMixin


class ChatUser(UserRelationMixin, Base):
    _user_back_populates = 'chatuser'

    chat_id:Mapped[int] = mapped_column(ForeignKey('chat.id'), nullable=False)

    chat:Mapped['Chat'] = relationship('Chat', back_populates='chatuser')
