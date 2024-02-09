from sqlalchemy.orm import declared_attr, Mapped, relationship

from .chat import Chat


class ChatListRelationMixin:
    _chats_back_populate: str
    _chats_lazy:str
    _chats_uselist:bool
    _chats_secondary: str | None = None

    @declared_attr
    def chats(cls) -> Mapped[list[Chat]]:
        return relationship(
            'Chat',
            back_populates=cls._chats_back_populate,
            lazy=cls._chats_lazy,
            uselist=cls._chats_uselist,
            secondary=cls._chats_secondary,
        )
    