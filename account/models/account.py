from typing import TYPE_CHECKING
from datetime import datetime
import uuid
from uuid import UUID as sqluuid


from sqlalchemy import (
    String,
    Boolean,
    Integer,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import EmailStr

if TYPE_CHECKING:
    from doctors.models import Doctor
from admin.models.groupsmxn import GroupListRelationMixin
from chat.models.chatlistmxn import ChatListRelationMixin
from core.models import Base
from diseaselistmxn import DiseaseListRelationMixin
from user_mixin import UserListRelationMixin


class Account(
    UserListRelationMixin,
    GroupListRelationMixin,
    ChatListRelationMixin, 
    DiseaseListRelationMixin,
    Base,
):
    _users_back_populates = "account"
    _users_lazy = "joined"
    _users_uselist = True

    _groups_back_populate = "account"
    _groups_secondary = "permission"
    _groups_lazy = "joined"
    _groups_uselist = True

    _doc_uselist = False
    _doc_lazy = "selectin"
    _doc_back_populate = "account"

    _chats_back_populate = 'account'
    _chats_lazy = 'joined'
    _chats_uselist = True
    _chats_secondary = 'user'

    _diseases_back_populate = "account"
    _diseases_secondary = "diagnosis"
    _diseases_lazy = "joined"
    _diseases_uselist = True

    uuid: Mapped[sqluuid] = mapped_column(
        default=uuid.uuid4,
        unique=True,
    )
    first_name: Mapped[str] = mapped_column(String(60), nullable=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    last_enter: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    btk_db_id: Mapped[int] = mapped_column(Integer, unique=True)
    phone: Mapped[int] = mapped_column(Integer, unique=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[bytes] = mapped_column(String(250))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, index=True)

    doctor: Mapped[Doctor] = relationship(
        "Doctor", back_populates="account", uselist=False, lazy="joined"
    )

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"
