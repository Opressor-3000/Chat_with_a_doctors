from datetime import datetime

from fastapi import Cookie
from sqlalchemy import (
    Column, 
    String, 
    Boolean, 
    Integer, 
    Constraint, 
    CheckConstraint, 
    Index, 
    UniqueConstraint, 
    ForeignKey, 
    DateTime, 
    ForeignKeyConstraint,
    func
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint


from core.models import Base
from admin.models import QR
from .account import Account
from .gender import Gender
from auth.utils import COOKIE_SESSION_ID


class User(Base):
   cookie: Mapped[str] = mapped_column(String(150), unique=True, default=Cookie(alias=COOKIE_SESSION_ID))
   username: Mapped[str] = mapped_column(String(60), nullable=False)
   account_id: Mapped[int] = mapped_column(Integer, ForeignKey('account.id', onupdate='CASCADE', ondelete='RESTRICT', name='account_user_fk'), nullable=True)
   last_enter: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow(), nullable=False)
   qr_id:Mapped[int] = mapped_column(Integer, ForeignKey('qr.id', onupdate='CASCADE', ondelete='RESTRICT', name='qr_user_fk'), nullable=True)
   avatar:Mapped[str] = mapped_column(String(250), nullable=True)
   is_active:Mapped[bool] = mapped_column(Boolean, default=True)
   gender_id:Mapped[int] = mapped_column(Integer, ForeignKey('gender.id', onupdate='CASCADE', ondelete='RESTRICT', name='user_gender_fk'), nullable=True)
   birthday:Mapped[datetime] = mapped_column(DateTime, nullable=True)

   gender: Mapped['Gender'] = relationship('Gender', back_populates='user')
   qr: Mapped['QR'] = relationship('QR', back_populates='user')
   account: Mapped['Account'] = relationship('Account', back_populates='user')

   __table_args__ = (CheckConstraint(func.char_length(username) <= 3, name='username_constraint'),)
   
