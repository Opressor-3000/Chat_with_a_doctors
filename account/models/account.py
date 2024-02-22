
from datetime import datetime
import uuid
from uuid import UUID as sqluuid


from sqlalchemy import (
    String,
    Boolean,
    Integer,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr


from core.models import Base
from .diseaselistmxn import DiseaseListRelationMixin
from .user_mixin import UserListRelationMixin
from doctors.models.mixin import DocRelationMixin
from admin.models.accessesmxn import AccessListRelationMixin


class Account(
    UserListRelationMixin,
    DocRelationMixin,
    DiseaseListRelationMixin,
    AccessListRelationMixin,
    Base,
):   
    _users_back_populates = "account"
    _users_lazy = "joined"
    _users_uselist = True

    _doc_uselist = True
    _doc_lazy = "selectin"
    _doc_back_populate = "account"

    _diseases_back_populate = "account"
    _diseases_secondary = "diagnosis"
    _diseases_lazy = "joined"
    _diseases_uselist = True

    _accesses_back_populate = 'account'
    _accesses_secondary = 'accessaccount'
    _accesses_lazy = 'joined'
    _accesses_uselist = True

    uuid: Mapped[sqluuid] = mapped_column(
        default=uuid.uuid4,
        unique=True,
    )
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_enter: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    btk_db_id: Mapped[int] = mapped_column(Integer, unique=True)
    phone: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=True)
    password: Mapped[bytes] = mapped_column(String(250))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    is_staff:Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"


