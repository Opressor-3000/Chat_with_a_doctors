from sqlalchemy.orm import declared_attr, Mapped, relationship

from .group import Group


class GroupListRelationMixin:
    _groups_back_populate:str
    _groups_lazy:str
    _groups_uselist:bool
    _groups_secondary: str | None = None

    @declared_attr
    def groups(cls) -> Mapped[list[Group]]:
        return relationship(
            'Group',
            back_populates=cls._groups_back_populate,
            lazy=cls._groups_lazy,
            secondary=cls._groups_secondary,
            uselist=cls._groups_uselist,
        )
