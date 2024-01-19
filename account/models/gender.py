
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from account.models.mixin import CreaterRelationMixin


class Gender(CreaterRelationMixin, Base):
   _creater_back_populates = 'gender'
   _creater_unique = True
   
   title:Mapped[str] = mapped_column(String(30), unique=True)