from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from account.models.mixin import CreaterRelationMixin


class Agency(CreaterRelationMixin, Base):
    _creater_back_populates = 'agency'
    
    title: Mapped[str] = mapped_column(String(150))
