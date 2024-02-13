from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer

if TYPE_CHECKING:
    from .chat import Chat
    from .chatuser import ChatUser
from admin.models.mixin import CreaterRelationMixin


class ChatRelationMixin:
    _chat_back_populate: str | None = None
    _chat_nullable: bool = False
    _chat_unique: bool = False
    _chat_uselist: bool
    _chat_lazy:str | None = None
    _chat_ondelete: str = 'RESTRICT'
    _chat_onupdate: str = 'CASCADE'
    _chat_foreignkey_name: str | None

    @declared_attr
    def chat_id(cls):
        return mapped_column(
            Integer, 
            ForeignKey(
                'chat.id', 
                name=cls._chat_foreignkey_name,
                ondelete=cls._chat_ondelete, 
                onupdate=cls._chat_onupdate,
            ), 
            nullable=cls._chat_nullable, 
            unique=cls._chat_unique,
        )

    @declared_attr
    def chat(cls) -> Mapped['Chat']:
        return relationship(
            'Chat', 
            back_populates=cls._chat_back_populate, 
            uselist=cls._chat_uselist, 
            lazy=cls._chat_lazy
        )


class ChatUserRelationMixin:
    _chatuser_back_populate: str | None = None
    _chatuser_nullable: bool = False
    _chatuser_unique: bool = False
    _chatuser_lazy: str | None = None
    _chatuser_uselist: bool
    _chatuser_ondelete: str = 'RESTRICT'
    _chatuser_onupdate: str = 'CASCADE'
    _chatuser_foreignkey_name: str

    @declared_attr
    def chatuser_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, 
            ForeignKey(
                'chatuser.id', 
                ondelete=cls._chatuser_ondelete, 
                onupdate=cls._chatuser_onupdate
            ), 
            unique=cls._chatuser_unique, 
            nullable=cls._chatuser_nullable
        )
    
    @declared_attr
    def chatuser(cls)-> Mapped['ChatUser']:
        return relationship(
            'ChatUser', 
            back_populates=cls._chatuser_back_populate, 
            lazy=cls._chatuser_lazy, 
            uselist=cls._chatuser_uselist
        )

    

class ChatCreaterRelationMixin(ChatRelationMixin, CreaterRelationMixin):
    pass

