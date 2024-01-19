from datetime import datetime
import uuid
from uuid import UUID as sqluuid


from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr


from core.models import Base




class Account(Base):
   uuid: Mapped[sqluuid] = mapped_column(
      default=uuid.uuid4,
      )
   last_enter: Mapped[datetime] = mapped_column(default=datetime.utcnow())
   btk_db_id: Mapped[int] = mapped_column(unique=True)
   phone:Mapped[int] = mapped_column(unique=True)
   email:Mapped[str] = mapped_column(unique=True)
   password:Mapped[bytes]
   is_active:Mapped[bool] = mapped_column(default=False)
