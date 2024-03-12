from typing import TYPE_CHECKING, List

from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .message import Message


class MessageListRelationMixin:
    _messages_back_populate: str
    _messages_lazy: str
    _messages_uselist: bool
    _messages_secondary: str | None = None

    @declared_attr
    def messages(cls) -> Mapped[List['Message']]:
        return relationship(
            back_populates=cls._messages_back_populate,
            lazy=cls._messages_lazy,
            uselist=cls._messages_uselist,
            secondary=cls._messages_secondary,
        )
