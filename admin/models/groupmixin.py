from sqlalchemy.orm import declared_attr, Mapped, relationship


from .group import Group


class GroupRelationMixin:
    _group_foreignkey_name: str
    _group_nullable = False
    _group_unique = False
    _group_onupdate = 'CASCADE'
    _group_ondelete = 'CASCADE'
    _group_back_populate:str
    _group_lazy:str
    _group_uselist:bool

    @declared_attr
    def group(cls) -> Mapped[Group]:
        return relationship(
            'Group',
            back_populates=cls._group_back_populate, 
            lazy=cls._group_lazy, 
            uselist=cls._group_uselist,
        )