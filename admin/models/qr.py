from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from core.models import Base
from admin.models.mixin import CreaterRelationMixin


class QR(CreaterRelationMixin, Base):
    _creater_back_populates = 'qr'
    
    qr: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

