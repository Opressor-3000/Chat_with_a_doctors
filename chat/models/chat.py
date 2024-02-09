from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean

from core.models.base import Base
from doctors.models.mixin import UserDocRelationMixin
from doctors.models.speclistmxn import SpecialityListRelationMixin


class Chat(
    UserDocRelationMixin, 
    SpecialityListRelationMixin,
    Base,
):
    _doc_back_populate = 'chat'
    _doc_lazy = 'joined'

    _user_back_populates = 'chat'
    _user_lazy = 'joined'

    _spec_back_populate = 'chat'
    _spec_lazy = 'selectin'
    _spec_uselist = False
    _spec_secondary = 'doctor'

    active:Mapped[bool] =mapped_column(Boolean, default=True, index=True)
    previous_chat_id:Mapped[int] = mapped_column(
        Integer, 
        ForeignKey(
            'chat.id', 
            name='previous_chat_id', 
            ondelete='RESTRICT', 
            onupdate='RESTRICT'
            ), 
        unique=True)
    
    previous_chat:Mapped['Chat'] = relationship('Chat', back_populates='chat', remote_side=[id], uselist=False, lazy='joined')

    def __repr__(self) -> str:
        return 

