from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UniqueConstraint, Boolean, Integer
from core.models import Base
    

# if TYPE_CHECKING:
from .mixin import CreaterRelationMixin
# from .groupmixin import GroupForeignkeyRelationMixin
from account.models.accounts_mixin import AccountRelationMixin


# class Permission(
#     CreaterRelationMixin, # <--
#     AccountRelationMixin,
#     Base,
# ):
#     _account_foreignkey_name = 'permission_account_fk'
#     _account_nullable = False
#     _account_unique = False
#     _account_onupdate = 'CASCADE'
#     _account_ondelete = 'RESTRICT'
#     _account_back_populate = 'permission'
#     _account_lazy = 'selectin'
#     _account_uselist = False

#     creater_id: Mapped[int] = mapped_column(
#         Integer,
#         ForeignKey(
#             "permission.id",
#             name="permission_creater_id",
#             ondelete="RESTRICT",
#             onupdate="CASCADE",
#         ),
#     )
    
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)

#     creater: Mapped["Permission"] = relationship(
#         "Permission",
#         back_populates="permission",
#         remote_side=[id],
#     )

#     __table_args__ = (
#         UniqueConstraint("account_id", "group_id", name="account_of_group_uc"),
#     )

#     def __repr__(self) -> str:
#         return f"{self.account.last_name} {self.account.first_name} {self.group.title}"

