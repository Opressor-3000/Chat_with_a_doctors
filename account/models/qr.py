from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base
from .mixin import UserRelationMixin


class QR(UserRelationMixin, Base):
    qr: Mapped[str] = mapped_column(unique=True, nullable=False)

