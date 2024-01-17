from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship

from core.models.base import Base



class RelationMixin:
    _back_populate: str = ''
    _unique: bool = False
    _nullable: bool = False
    _table: str = ''

    @declared_attr
    def get_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(cls._back_populate + '.id'),
            nullable=cls._nullable,
            unique=cls._unique
            )
    
    @declared_attr
    def backtable(cls) -> Mapped[object]:
      return relationship(cls._table, back_populates=cls._user_back_populates)