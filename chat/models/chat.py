from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Boolean

from core.models.base import Base
from doctors.models.mixin import UserDocRelationMixin, SpecialityRelationMixin
from doctors.models.doc_chatuser_mxn import DoctorAccountRelationMxn
from account.models.accounts_mixin import AccountRelationMixin
from chat.models.mixin_ import MessageListRelationMixin


class Chat(
    UserDocRelationMixin,
    MessageListRelationMixin,
    SpecialityRelationMixin,
    AccountRelationMixin,
    DoctorAccountRelationMxn,
    Base,
):
    _messages_back_populate = 'chat'
    _messages_lazy = 'joined'
    _messages_uselist = True
    _messages_secondary = 'chatuser'

    _doc_back_populate = "chat"
    _doc_lazy = "joined"
    _doc_foreignkey_name = "chat_doctor_fk"
    _doc_uselist = False
    _doc_nullable = True

    _user_back_populates = "chat"
    _user_lazy = "joined"
    _user_foreignkey_name = "chat_user_fk"
    _user_uselist = False

    _spec_foreignkey_name = "chat_speciality_fk"
    _spec_back_populate = "chat"
    _spec_lazy = "selectin"
    _spec_uselist = False
    _spec_secondary = "doctor"
    _spec_nullable = True

    _account_back_populate = "chat"
    _account_foreignkey_name = "chat_account_fk"
    _account_nullable = True
    _account_uselist = False

    _doctor_account_back_populate = "chat"
    _doctor_account_secondary = 'doctor'
    _doctor_account_lazy = 'joined'
    _doctor_account_uselist = False

    active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    previous_chat_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "chat.id", name="previous_chat_id", ondelete="RESTRICT", onupdate="RESTRICT"
        ),
        unique=True,
    )

    previous_chat: Mapped["Chat"] = relationship(
        "Chat", back_populates="chat", remote_side=[id], uselist=False, lazy="joined"
    )

    def __repr__(self) -> str:
        return f"{self.user} {self.doctor_account} {self.speciality} {self.created_at}"
