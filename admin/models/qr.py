from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String

from core.models import Base
if TYPE_CHECKING:
    from .group import CreaterRelationMixin
from account.models import User

class QR(CreaterRelationMixin, Base):
    _creater_back_populates = 'qr'
    _creater_lazy = 'joined'
    
    qr: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    users:Mapped[list[User]] = relationship(
        'User', 
        back_populates='qr',
        lazy='joined',
        uselist=False,
        )

    def __repr__(self) -> str:
        return f'{self.qr}'