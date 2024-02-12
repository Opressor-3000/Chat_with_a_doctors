
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from admin.models.mixin import CreaterRelationMixin
from .user import User


class Gender(CreaterRelationMixin, Base):
   _creater_id_nullable = True 
   _creater_foreignkey_name = 'gender_creater_fk'
   _creater_back_populates = 'gender'
   
   title:Mapped[str] = mapped_column(String(30), unique=True)

   users:Mapped[list[User]] = relationship(
      'User', 
      back_populates='gender',
      uselist=True,
      lazy='joined',
   )
   
   def __repr__(self) -> str:
      return f'{self.title}'