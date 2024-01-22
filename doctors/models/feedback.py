from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from .mixin_1 import DocChatUserCreaterMixin, DocChatUserRelationMixin


class Feedback(DocChatUserCreaterMixin, Base):
    _creater_back_populates = 'feedback'
    _chat_back_populate = 'feedback'   
    _doc_back_populate = 'feedback'   # unique together for doc & user
    _user_back_populates = 'feedback'  

    text:Mapped[str] = mapped_column(String(500))
    delete:Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at:Mapped[datetime] = mapped_column(DateTime)


class Rating(DocChatUserRelationMixin, Base):
    _user_back_populates = 'rating'
    _chat_back_populate = 'rating'
    _doc_back_populate = 'rating'
    
    point:Mapped[int] = mapped_column(Integer)
