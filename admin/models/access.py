from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UniqueConstraint, ForeignKey

from core.models import Base
from admin.models.mixin import CreaterRelationMixin
from account.models.accounts_mixin import AccountListRelationMixin
# from account.models.accounts_mixin import AccountListRelationMixin


class Access(AccountListRelationMixin, Base):
    _accounts_back_populate = 'access'
    _accounts_secondary = 'accessaccount'
    _accounts_uselist = True
    _accounts_lazy = 'joined'
    
    title: Mapped[str] = mapped_column(String(32), unique=True)

    def __repr__(self) -> str:
        return f"{self.title}"


class AccessAccount(CreaterRelationMixin, Base):
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


# class Group(
#     CreaterRelationMixin,
#     AccountListRelationMixin,
#     Base,
# ):
#     _accounts_back_populate = 'group'
#     _accounts_lazy = 'joined'
#     _accounts_uselist = True
#     _accounts_secondary = 'permission'

#     _creater_back_populates = "group"
#     _creater_foreignkey_name = 'group_creater_fk'

#     title: Mapped[str] = mapped_column(String(60), unique=True)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

#     accesses: Mapped[list["Access"]] = relationship(
#         "Access",
#         back_populates="group",
#         secondary="accessgroup",
#         uselist=True,
#         lazy="joined",
#     )

#     def __repr__(self) -> str:
#         return f"{self.title}"




    # добавить constrian что не может быть циклов
