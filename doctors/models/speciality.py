from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

from .doc_list_mxn import DoctorListRelationMixin
from .certificatemxn import CertificateListRelationMixin
from account.models.accounts_mixin import AccountListRelationMixin
from admin.models.mixin import CreaterRelationMixin
from chat.models.chatlistmxn import ChatListRelationMixin

class Speciality(
    CreaterRelationMixin, 
    ChatListRelationMixin,
    AccountListRelationMixin,
    CertificateListRelationMixin, 
    Base
):  
    _chats_back_populate = 'speciality'
    _chats_lazy = 'joined'
    _chats_uselist = True
    _chats_secondary = 'doctor'

    _creater_back_populates = 'speciality'
    _creater_foreignkey_name = 'speciality_creater_fk'

    _accounts_back_populate = 'speciality'
    _accounts_lazy = 'joined'
    _accounts_uselist = True
    _accounts_secondary = 'doctor'

    _certificates_back_populate = 'speciality'
    _certificates_lazy = 'joined'
    _certificates_uselist = True

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self) -> str:
        return f'{self.title}'


