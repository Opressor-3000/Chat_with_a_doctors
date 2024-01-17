from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from core.models import RelationMixin

if TYPE_CHECKING:
   from account.models import User, Account


class UserRelationMixin(RelationMixin):
   _id_unique: bool = False
   _user_back_populates: str | None = None
   _user_id_nullable: bool = False

   @declared_attr
   def user_id(cls) -> Mapped[int]:
      return mapped_column(ForeignKey("user.id"), unique=cls._id_unique, nullable=cls._user_id_nullable)

   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship("User", back_populates=cls._user_back_populates)


class CreaterRelationMixin:
   _unique: bool = False
   _account_back_populates: str | None = 'account'
   _account_id_nullable: bool = False

   @declared_attr
   def creater_id(cls) -> Mapped[int]:
      return mapped_column(ForeignKey("account.id"), nullable=cls._account_id_nullable, unique=cls._unique)

   @declared_attr
   def account_creater(cls) -> Mapped["Account"]:
      return relationship("Account", back_populates=cls._account_back_populates)
   

