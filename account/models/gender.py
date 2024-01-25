
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from admin.models.mixin import CreaterRelationMixin


class Gender(CreaterRelationMixin, Base):
   _creater_back_populates = 'gender'
   
   title:Mapped[str] = mapped_column(String(30), unique=True)