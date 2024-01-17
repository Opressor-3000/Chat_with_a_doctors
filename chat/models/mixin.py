from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

from account.models import UserRelationMixin
from core.models import RelationMixin
from .chat import Chat


class ChatRelationMixin:
    _chat_back_populate: str = 'chat'
    _nullable: bool = False
    _unique: bool = False

    @declared_attr
    def chat_id(cls):
        return mapped_column(ForeignKey('chat.id'), nullable=cls._nullable, unique=cls._unique)
    
    @declared_attr
    def chat(cls) -> Mapped['Chat']:
        return relationship('User', back_populates=cls._chat_back_populate)

    


