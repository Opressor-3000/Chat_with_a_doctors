from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from admin.models.mixin import CreaterRelationMixin


class Agency(CreaterRelationMixin, Base):
    _creater_back_populates = 'agency'
    _creater_foreignkey_name = 'creater_agency_id'
    
    title: Mapped[str] = mapped_column(String(150))

