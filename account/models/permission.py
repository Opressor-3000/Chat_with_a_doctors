from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from core.models import Base

if TYPE_CHECKING:
    from .account import Account
    from .group import Group


class Permission(Base):
    account_id:Mapped[int] = mapped_column(ForeignKey('account.id'))  #togeder_unique
    group_id:Mapped[int] = mapped_column(ForeignKey('group.id'))
    creater_id:Mapped[int] = mapped_column(ForeignKey('permission.id'))

    account:Mapped['Account'] = relationship('Account', back_populates='permission')
    group:Mapped['Group'] = relationship('Group', back_populates='permission')
    creater:Mapped['Permission'] = relationship('Permission', back_populates='permission', remote_side=[id])




