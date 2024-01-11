from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint

from core.models.base import Base

import uuid


# class User(Base):
#    id: Mapped[int] = mapped_column(
#       autoincrement=True, unique=True
#    )
#    uuid: Mapped[str] = mapped_column(
#       default=uuid.uuid4,
#       server_default=uuid.uuid4,
#       primary_key=True,
#       )
#    cookie: Mapped[str]
#    created_at: Mapped[datetime] = mapped_column(unique=True, index=True)
#    last_enter: Mapped[datetime] = mapped_column()
#    qr_id:Mapped[int]
#    btk_db_id: Mapped[int] = mapped_column(unique=True)
#    username: Mapped[str] = mapped_column(String(50))
#    phone:Mapped[str] = mapped_column(unique=True)
#    email:Mapped[str]
#    password:Mapped[str]
#    avatar:Mapped[bytes]
#    is_active:Mapped[bool]
#    groups:Mapped[int]
#    role:Mapped[int]
#    gender:Mapped[int]
#    birthday:Mapped[datetime]
   
#    @declared_attr.directive
#    def __table_args__(cls):
#       return (
#          CheckConstraint('id > 0', name="id_constraint"),
#       )
      
   