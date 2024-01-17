from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr

from core.models import Base
from .mixin import CreaterRelationMixin
from .qr import QR
from .user import User
import uuid
from uuid import UUID as sqluuid


class User(Base):
   cookie: Mapped[str] = mapped_column(String(150), unique=True)
   username: Mapped[str] = mapped_column(String(60), nullable=False)
   account_id: Mapped[int] = mapped_column(ForeignKey('account.id'))
   last_enter: Mapped[datetime] = mapped_column(default=datetime.utcnow(), nullable=False)
   qr_id:Mapped[int] = mapped_column(ForeignKey('qr.id'))
   avatar:Mapped[bytes] = mapped_column()
   is_active:Mapped[bool]
   gender_id:Mapped[int] = mapped_column(ForeignKey('gender.id'))
   birthday:Mapped[datetime] = mapped_column()

   gender: Mapped['Gender'] = relationship('Gender', back_populates='user')
   qr: Mapped['QR'] = relationship('QR', back_populates='user')
   account: Mapped['User'] = relationship('User', back_populates='user')

      
class Account(Base):
   uuid: Mapped[sqluuid] = mapped_column(
      default=uuid.uuid4,
      )
   last_enter: Mapped[datetime] = mapped_column(default=datetime.utcnow())
   btk_db_id: Mapped[int] = mapped_column(unique=True)
   phone:Mapped[str] = mapped_column(unique=True)
   email:Mapped[str] = mapped_column(unique=True)
   password:Mapped[bytes]
   is_active:Mapped[bool] = mapped_column(default=False)


class Group(CreaterRelationMixin, Base):
    _unique = True
    _account_back_populates = 'account'
    
    title:Mapped[str] = mapped_column(String(60))


class Gender(Base):
   title:Mapped[str] = mapped_column(unique=True)