from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .chat import Chat
    from .chatuser import ChatUser
from account.models.mixin import CreaterRelationMixin

class ChatRelationMixin:
    _chat_back_populate: str | None = None
    _chat_nullable: bool = False
    _chat_unique: bool = False

    @declared_attr
    def chat_id(cls):
        return mapped_column(ForeignKey('chat.id'), nullable=cls._chat_nullable, unique=cls._chat_unique)

    @declared_attr
    def chat(cls) -> Mapped['Chat']:
        return relationship('Chat', back_populates=cls._chat_back_populate)
    

class ChatUserRelationMixin:
    _chatuser_back_populate: str | None = None
    _chatuser_nullable: bool = False
    _chatuser_unique: bool = False

    @declared_attr
    def chatuserr_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('chatuser.id'), unique=cls._chatuser_unique, nullable=cls._chatuser_nullable)
    
    @declared_attr
    def chatuser(cls)-> Mapped['ChatUser']:
        return relationship('ChatUser', back_populates=cls._chatuser_back_populate)

    

class ChatCreaterRelationMixin(ChatRelationMixin, CreaterRelationMixin):
    pass

