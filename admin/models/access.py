from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UniqueConstraint, ForeignKey

from core.models import Base
from admin.models.mixin import CreaterRelationMixin
from account.models.accounts_mixin import AccountListRelationMixin
from account.models.accounts_mixin import AccountListRelationMixin


class Access(
    AccountListRelationMixin, 
    Base
):
    _accounts_back_populate = 'access'
    _accounts_secondary = 'accessaccount'
    _accounts_uselist = True
    _accounts_lazy = 'joined'
    
    title: Mapped[str] = mapped_column(String(32), unique=True)

    def __repr__(self) -> str:
        return f"{self.title}"


class AccessAccount(
    CreaterRelationMixin, 
    Base
):
    _creater_back_populates = "accessgroup"
    _creater_foreignkey_name = 'accessgroup_creater_fk'

    account_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "account.id",
            name="accessaccount_account_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )

    access_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "access.id",
            name="accessaccount_access_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
    )

    __table_args__ = (
        UniqueConstraint(
            "account_id",
            "access_id",
            name="access_account_uc",
        ),
    )


