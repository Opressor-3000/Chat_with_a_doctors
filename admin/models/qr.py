from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String

from mixin import CreaterRelationMixin
from account.models.user_mixin import UserListRelationMixin
from core.models import Base
if TYPE_CHECKING:
    from .permission import Permission
from account.models import User

class QR(
    CreaterRelationMixin, 
    UserListRelationMixin,
    Base
):
    _creater_unique = False
    _creater_back_populates = 'qr'
    _creater_lazy = 'joined'
    _creater_uselist = False
    _creater_foreignkey_name = 'qr_creater_fk'

    _users_back_populates = 'qr'
    _users_lazy = 'joined'
    _users_uselist = True
    
    qr: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)    

    def __repr__(self) -> str:
        return f'{self.qr}'