from datetime import datetime
import uuid
from uuid import UUID as sqluuid


from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr


from core.models import Base


class Account(Base):
   uuid: Mapped[sqluuid] = mapped_column(
      default=uuid.uuid4, unique=True,
      )
   last_enter: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
   btk_db_id: Mapped[int] = mapped_column(Integer, unique=True)
   phone:Mapped[int] = mapped_column(Integer, unique=True)
   email:Mapped[str] = mapped_column(String, unique=True)
   password:Mapped[bytes] = mapped_column(String(250))
   is_active:Mapped[bool] = mapped_column(Boolean, default=False)
