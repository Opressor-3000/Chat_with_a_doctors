from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint, ForeignKey

from core.models import Base
from admin.models.mixin import CreaterRelationMixin

from account.models.accounts_mixin import AccountListRelationMixin


class Group(
    CreaterRelationMixin,
    AccountListRelationMixin,
    Base,
):
    _account_foreignkey_name = 'group_account_fk'
    _account_nullable = False
    _account_unique = True
    _account_onupdate = 'CASCADE'
    _account_ondelete = 'CASCADE'
    _account_back_populate = 'group'
    _account_lazy = 'joined'
    _account_uselist = True
    _accounts_secondary = 'permission'

    _creater_back_populates = "group"
    _creater_lazy = "joined"

    title: Mapped[str] = mapped_column(String(60), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

    accesses: Mapped[list["Access"]] = relationship(
        "Access",
        back_populates="group",
        secondary="accessgroup",
        uselist=True,
        lazy="joined",
    )

    def __repr__(self) -> str:
        return f"{self.title}"


class AccessGroup(CreaterRelationMixin, Base):
    _creater_back_populates = "accessgroup"
    _creater_lazy = "joined"

    group_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "group.id",
            name="accessgroup_group_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )

    access_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "access.id",
            name="accessgroup_access_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )

    access: Mapped["Access"] = relationship(
        "Access",
        back_populates="accessgroup",
        uselist=True,
        lazy="selectin",
    )

    __table_args__ = (
        UniqueConstraint(
            "group_id",
            "access_id",
            name="access_group_uc",
        ),
    )


class Access(Base):
    title: Mapped[str] = mapped_column(String(32), unique=True)
    parent_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "access.id",
            name="access_parent_fk",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
        nullable=True,
    )

    parent: Mapped["Access"] = relationship(
        "Access",
        back_populates="access",
        remote_side=[id],
        uselist=False,
        lazy="joined",
    )

    groups: Mapped[list[Group]] = relationship(
        "Group",
        back_populates="access",
        secondary="accessgroup",
        uselist=True,
        lazy="joined",
    )

    def __repr__(self) -> str:
        return f"{self.title}"

    # добавить constrian что не может быть циклов
