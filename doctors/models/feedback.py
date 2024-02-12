from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from .doc_chatuser_mxn import DocChatUserRelationMixin
from .cucr_mixin import DocChatUserCreaterMixin


class Feedback(DocChatUserCreaterMixin, Base):
    _creater_back_populates = 'feedback'
    _creater_foreignkey_name = 'feedback_creater_fk'

    _chatuser_back_populate = 'feedback'
    _chatuser_lazy = 'joined'
    _chatuser_foreignkey_name = 'feedback_chatuser_fk'
    _chatuser_uselist = False

    _doc_back_populate = 'feedback'   # unique together for doc & user
    _doc_lazy = 'joined'
    _doc_foreignkey_name = 'feedback_doctor_fk'
    _doc_uselist = False

    text:Mapped[str] = mapped_column(String(500))
    delete:Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at:Mapped[datetime] = mapped_column(DateTime)


class Rating(DocChatUserRelationMixin, Base):
    _user_back_populates = 'rating'
    _user_foreignkey_name = 'rating_user_fk'
    _user_lazy = 'joined'
    _user_uselist = False

    _chat_back_populate = 'rating'
    _chat_foreignkey_name = 'rating_chat_fk'
    _chat_lazy = 'joined'
    _chat_uselist = False

    _doc_back_populate = 'rating'
    _doc_foreignkey_name = 'rating_doctor_fk'
    _doc_uselist = False
    _doc_lazy = 'joined'
    
    point:Mapped[int] = mapped_column(Integer)
