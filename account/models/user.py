from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr

from core.models import Base
from .mixin import CreaterRelationMixin, UserRelationMixin

import uuid
from uuid import UUID as sqluuid


class User(Base):
   cookie: Mapped[str] = mapped_column(String(150), unique=True)
   username: Mapped[str] = mapped_column(String(60))
   account_id: Mapped[int] = mapped_column(ForeignKey('account.id'), nullable=True)
   last_enter: Mapped[datetime] = mapped_column()
   qr_id:Mapped[int]
   avatar:Mapped[bytes]
   is_active:Mapped[bool]
   gender:Mapped[int]
   birthday:Mapped[datetime]

      
class Account(Base):
   _user_back_populates = 'user'
   _id_unique = True
   _user_id_nullable = False

   uuid: Mapped[sqluuid] = mapped_column(
      default=uuid.uuid4,
      )
   last_enter: Mapped[datetime] = mapped_column()
   btk_db_id: Mapped[int] = mapped_column(unique=True)
   phone:Mapped[str] = mapped_column(unique=True)
   email:Mapped[str]
   password:Mapped[str]
   is_active:Mapped[bool]
   groups:Mapped[int]
   role:Mapped[int]


class Group(CreaterRelationMixin, Base):
    _unique = True
    _account_back_populates = 'account'
    
    title:Mapped[str] = mapped_column(String(60))
    creater:Mapped[int]


class Gender(Base):
   title:Mapped[str] = mapped_column(unique=True)