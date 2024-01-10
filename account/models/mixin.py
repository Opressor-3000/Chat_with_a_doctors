from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


from core.models import Base
from account.models.user import User


class UserRelationMixin:
   _uuid_unique: bool = False
   _user_back_populates: str | None = None
   _user_id_nullable: bool = False

   @declared_attr
   def user_id(cls) -> Mapped[int]:
      return mapped_column(ForeignKey("user.uuid"), unique=cls._uuid_unique, nullable=cls._user_id_nullable)
   

   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship("User", back_populates=cls._user_back_populates)


class CreatedUser(Base):
   __abstract__ = True

   created_at:Mapped[datetime] = mapped_column(
      default=datetime.utcnow()
   )
   usercreated_id:Mapped[int] = mapped_column(ForeignKey=("user.id"))

   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship("User")


