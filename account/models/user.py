from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint


from core.models import Base
from .qr import QR
if TYPE_CHECKING:
   from gender import Gender



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

