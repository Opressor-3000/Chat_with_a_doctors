from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

from chat.models import Chat
from core.models.base import Base
from account.models.user_mixin import UserRelationMixin


class ChatUser(UserRelationMixin, Base):
    _user_back_populates = 'chatuser'
    _user_lazy = 'joined'
    _user_uselist = False
    _user_unique = True

    chat_id:Mapped[int] = mapped_column(
        Integer, 
        ForeignKey(
            'chat.id', 
            name='chatuser_chat_id', 
            ondelete='RESTRICT', 
            onupdate='RESTRICT'
            ), 
        nullable=False,
        )

    chat:Mapped['Chat'] = relationship('Chat', back_populates='chatuser', uselist=False, lazy='joined')
