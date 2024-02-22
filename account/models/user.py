from datetime import datetime
from typing import TYPE_CHECKING

from fastapi import Cookie
from sqlalchemy import (
    Column,
    String,
    Boolean,
    CheckConstraint,
    DateTime,
    func,
)

from sqlalchemy.orm import Mapped, mapped_column

from chat.models.chatlistmxn import ChatListRelationMixin
from core.models import Base
from admin.models.qr_mixin import QRRelationMixin
from doctors.models.doc_list_mxn import DoctorListRelationMixin
from .accounts_mixin import AccountRelationMixin
from .gender_mixin import GenderRelationMixin
from auth.utils import COOKIE_SESSION_ID


class User(
    AccountRelationMixin,
    ChatListRelationMixin,
    DoctorListRelationMixin,
    GenderRelationMixin,
    QRRelationMixin,
    Base,
):
    _chats_back_populate = "user"
    _chats_lazy = "joined"
    _chats_uselist = True

    _account_foreignkey_name = "account_user_fk"
    _account_ondelete = "RESTRICT"
    _account_onupdate = "CASCADE"
    _account_back_populate = "user"
    _account_lazy = "joined"
    _account_uselist = False

    _doctors_back_populate = "user"
    _doctors_lazy = "selectin"
    _doctors_secondary = "chat"
    _doctors_uselist = True

    _qr_foreignkey_name = "user_qr_id"
    _qr_back_populate = "user"
    _qr_uselist = False
    _qr_lazy = "joined"

    _gender_back_populate = "user"
    _gender_foreignkey_name = "user_gender_fk"
    _gender_ondelete = "RESTRICT"
    _gender_onupdate = "CASCADE"
    _gender_lazy = "joined"
    _gender_uselist = False

    cookie: Mapped[str] = mapped_column(
        String(150), unique=True, default=Cookie(alias=COOKIE_SESSION_ID)
    )
    username: Mapped[str] = mapped_column(String(60), nullable=False)

    last_enter: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow(), nullable=False
    )
    avatar: Mapped[str] = mapped_column(String(250), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint(func.char_length(username) <= 3, name="username_constraint"),
    )

    def __repr__(self) -> str:
        return (
            f"username:{self.username}, gender{self.gender}, birthday:{self.birthday}"
        )
