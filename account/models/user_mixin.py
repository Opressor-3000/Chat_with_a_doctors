from typing import TYPE_CHECKING, List


from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


if TYPE_CHECKING:
   from account.models import User


class UserRelationMixin:
   _user_unique: bool = False
   _user_back_populates: str 
   _user_id_nullable: bool = False
   _user_lazy: str 
   _user_uselist: bool 
   _user_ondelete: str = 'RESTRICT'
   _user_onupdate: str = 'CASCADE'
   _user_foreignkey_name: str
   _user_secondary:str | None = None

   @declared_attr
   def user_id(cls) -> Mapped[int]:
      return mapped_column(Integer, ForeignKey(
         "user.id", 
         name=cls._user_foreignkey_name,
         ondelete=cls._user_ondelete, 
         onupdate=cls._user_onupdate
      ), 
      unique=cls._user_unique, 
      nullable=cls._user_id_nullable
      )

   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship(
         "User", 
         back_populates=cls._user_back_populates, 
         lazy=cls._user_lazy, 
         uselist=cls._user_uselist
      )
   

class UserListRelationMixin:
   _users_back_populates: str
   _users_lazy: str
   _users_uselist: bool
   _users_secondary:str | None = None

   @declared_attr
   def users(cls) -> Mapped[List['User']]:
      return relationship(
         'User',
         back_populates=cls._users_back_populates, 
         lazy=cls._users_lazy, 
         secondary=cls._users_secondary, 
         uselist=cls._users_uselist,
      )


class UserRelationMxn:
   _user_back_populates: str 
   _user_lazy: str 
   _user_uselist: bool 
   _user_secondary:str | None = None


   @declared_attr
   def user(cls) -> Mapped["User"]:
      return relationship(
         "User", 
         back_populates=cls._user_back_populates, 
         lazy=cls._user_lazy, 
         uselist=cls._user_uselist,
         secondary=cls._user_secondary
      )