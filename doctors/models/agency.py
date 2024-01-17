from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from account.models import CreaterRelationMixin


class Agency(CreaterRelationMixin, Base):
    id:Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
