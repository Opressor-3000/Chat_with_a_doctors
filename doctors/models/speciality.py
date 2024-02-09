from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from admin.models.mixin import CreaterRelationMixin
from .doctor import Doctor
from chat.models import Chat
from chat.models.chatlistmxn import ChatListRelationMixin
from doc_list_mxn import DoctorListRelationMixin

class Speciality(
    CreaterRelationMixin, 
    DoctorListRelationMixin,
    ChatListRelationMixin,
    Base
):  
    _chats_back_populate = 'speciality'
    _chats_lazy = 'joined'
    _chats_uselist = True
    _chats_secondary = 'doctor'

    _doctors_back_populate = 'speciality'
    _doctors_lazy = 'joined'
    _doctors_uselist = True

    _creater_back_populates = 'speciality'
    _creater_lazy = 'joined'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self) -> str:
        return f'{self.title}'


