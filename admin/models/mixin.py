from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from account.models import Account


class CreaterRelationMixin:
    _creater_unique: bool = False
    _creater_back_populates: str
    _creater_id_nullable: bool = False
    _creater_ondelete: str = "RESTRICT"
    _creater_onupdate: str = "RESTRICT"
    _creater_foreignkey_name: str

    @declared_attr
    def creater_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey(
                "account.id",
                name=cls._creater_foreignkey_name,
                ondelete=cls._creater_ondelete,
                onupdate=cls._creater_onupdate,
            ),
            nullable=cls._creater_id_nullable,
            unique=cls._creater_unique,
        )

    @declared_attr
    def creater(cls) -> Mapped["Account"]:
        return relationship(
            "Account",
            back_populates=cls._creater_back_populates,
        )


