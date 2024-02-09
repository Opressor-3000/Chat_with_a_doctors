from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

from chat.models.mixin import ChatRelationMixin
from core.models.base import Base
from account.models.user_mixin import UserRelationMixin


class ChatUser(
    UserRelationMixin, 
    ChatRelationMixin,
    Base,
):
    _user_back_populates = 'chatuser'
    _user_foreignkey_name = 'chatuser_user_fk'
    _user_lazy = 'joined'
    _user_uselist = False
    _user_unique = True

    _chat_back_populate = 'chatuser'
    _chat_foreignkey_name = 'chatuser_chat_fk'
    _chat_lazy = 'joined'
    _chat_uselist = True

