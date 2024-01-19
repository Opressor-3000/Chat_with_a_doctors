from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from .mixin import CreaterRelationMixin


class Group(CreaterRelationMixin, Base):
    _account_back_populates = 'account'
    
    title:Mapped[str] = mapped_column(String(60), unique=True)
