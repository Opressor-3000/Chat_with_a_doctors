from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from core.models.base import Base
from doctors.models.mixin import UserDocSpecMixin


class Chat(UserDocSpecMixin, Base):
    _doc_back_populate = 'chat'
    _user_back_populates = 'chat'
    _spec_back_populate = 'chat'
    _spec_nullable = True

    active:Mapped[bool]
    previous_chat:Mapped[int] = mapped_column(ForeignKey('chat.id'), unique=True)



