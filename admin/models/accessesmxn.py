from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, relationship


from .access import Access


class AccessListRelationMixin:
    _accesses_lazy:str | None = None
    _accesses_back_populate:str
    _accesses_uselist:bool
    _accesses_secondary: str | None = None

    @declared_attr
    def access(cls) -> Mapped[list['Access']]:
        return relationship(
            'Access',
            back_populates=cls._accesses_back_populate,
            lazy=cls._accesses_lazy,
            secondary=cls._accesses_secondary,
            uselist=cls._accesses_uselist,
        )
