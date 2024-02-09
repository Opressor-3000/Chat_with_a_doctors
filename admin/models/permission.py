from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UniqueConstraint, Boolean, Integer
from core.models import Base

if TYPE_CHECKING:
    from account.models.accounts_mixin import AccountRelationMixin
    from .group import Group
from .groupmixin import GroupRelationMixin
from .mixin import CreaterRelationMixin


class Permission(
    CreaterRelationMixin, # <--
    GroupRelationMixin,
    AccountRelationMixin,
    Base,
):
    _account_foreignkey_name = 'permission_account_fk'
    _account_nullable = False
    _account_unique = False
    _account_onupdate = 'CASCADE'
    _account_ondelete = 'CASCADE'
    _account_back_populate = 'permission'
    _account_lazy = 'selectin'
    _account_uselist = True

    _creater_unique = False
    _creater_back_populates = 'permission'
    _creater_id_nullable: bool = False
    _creater_lazy: str | None = None
    _creater_uselist: bool
    _creater_ondelete: str = "RESTRICT"
    _creater_onupdate: str = "RESTRICT"
    _creater_foreignkey_name: str | None

    _group_foreignkey_name = 'permission_group_fk'
    _group_nullable = False
    _group_unique = False
    _group_onupdate = 'CASCADE'
    _group_ondelete = 'CASCADE'
    _group_back_populate = 'permission'
    _group_lazy = 'selectin'
    _group_uselist = True

    group_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "group.id",
            name="permission_group_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )
    creater_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "permission.id",
            name="permission_creater_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

    group: Mapped["Group"] = relationship(
        "Group", back_populates="permission", lazy="joined", uselist=True
    )
    creater: Mapped["Permission"] = relationship(
        "Permission",
        back_populates="permission",
        remote_side=[id],
    )

    __table_args__ = (
        UniqueConstraint("account_id", "group_id", name="account_of_group_uc"),
    )

    def __repr__(self) -> str:
        return f"{self.account.last_name} {self.account.first_name} {self.group.title}"
