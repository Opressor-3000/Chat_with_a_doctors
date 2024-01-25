from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship



if TYPE_CHECKING:
   from account.models import User




class UserRelationMixin:
   _user_unique: bool = False
   _user_back_populates: str | None = None
   _user_id_nullable: bool = False

   @declared_attr
   def user_id(cls) -> Mapped[int]:
      return mapped_column(ForeignKey("user.id"), unique=cls._user_unique, nullable=cls._user_id_nullable)

   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship("User", back_populates=cls._user_back_populates)
   




