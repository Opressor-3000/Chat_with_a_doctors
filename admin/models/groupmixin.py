from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey

if TYPE_CHECKING:
    from admin.models.access import Group


class GroupForeignkeyRelationMixin:
    _group_foreignkey_name: str
    _group_nullable = False
    _group_unique = False
    _group_onupdate = 'CASCADE'
    _group_ondelete = 'RESTRICT'
    _group_back_populate:str
    _group_lazy:str
    _group_uselist:bool
 
    @declared_attr
    def group_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey(
                "group.id",
                ondelete=cls._group_ondelete,
                onupdate=cls._group_onupdate,
                name=cls._group_foreignkey_name,
            ),
            unique=cls._group_unique,
            nullable=cls._group_nullable,
        )
    
    @declared_attr
    def group(cls) -> Mapped['Group']:
        return relationship(
            'Group',
            back_populates=cls._group_back_populate, 
            lazy=cls._group_lazy, 
            uselist=cls._group_uselist,
        )
    

class GroupRelationMixin:
    _group_back_populate:str
    _group_lazy:str
    _group_uselist:bool
    _group_secondary: str | None = None
    
    @declared_attr
    def group(cls) -> Mapped['Group']:
        return relationship(
            'Group',
            back_populates=cls._group_back_populate, 
            lazy=cls._group_lazy, 
            uselist=cls._group_uselist,
            secondary=cls._group_secondary,
        )
    