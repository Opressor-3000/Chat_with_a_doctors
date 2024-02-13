from datetime import datetime


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean, DateTime, String


from core.models.base import Base
from .mixin import ChatUserRelationMixin
from doctors.models.cucr_mixin import ChatUserCreaterRelationMixin


class Message(
    ChatUserCreaterRelationMixin, 
    Base
):
    _creater_back_populates = 'message'
    _creater_foreignkey_name = 'message_creater_id' 

    _chatuser_back_populate = 'message'
    _chatuser_lazy = 'joined'
    _chatuser_uselist = False
    _chatuser_foreignkey_name = 'message_chatuser_id'
    
    text:Mapped[str] = mapped_column(String(512),index=True)
    delete:Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at:Mapped[datetime] = mapped_column(DateTime)


class MessageStatus(
    ChatUserRelationMixin, 
    Base
):
    _chatuser_back_populate = 'messagestatus'
    _chatuser_foreignkey_name = 'MessageStetus_chatuser_id'
    _chatuser_lazy = 'joined'
    _chatuser_uselist = False

    message_id:Mapped[int] = mapped_column(
        Integer, 
        ForeignKey(
            'message.id', 
            name='message_status', 
            ondelete='CASCADE', 
            onupdate='CASCADE',
        ), 
        unique=True,
    )
    received:Mapped[datetime] = mapped_column(DateTime)
    read:Mapped[datetime] = mapped_column(DateTime)



