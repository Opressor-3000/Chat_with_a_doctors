from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import ForeignKey, UniqueConstraint, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
if TYPE_CHECKING:
    from chat.models import Chat
    from account.models import Account, User
    from .speciality import Speciality
from .certificate import Certificate
from admin.models.mixin import CreaterRelationMixin
from .feedback import Feedback


class Doctor(CreaterRelationMixin, Base):
    _creater_back_populates = 'doctor'
    _creater_foreignkey_name = 'doctor_creater_id'
    _creater_lazy = 'joined'
    _creater_uselist = False
    
    account_id:Mapped[int] = mapped_column(Integer, ForeignKey('account.id', name='doctor_account_id', ondelete='RESTRICT', onupdate='CASCADE'),) # create if exist current sertificate CHECH
    speciality_id:Mapped[int] = mapped_column(Integer, ForeignKey('speciality.id', ondelete='RESTRICT', onupdate='CASCADE', name='speciality_doc'),)
    is_active:Mapped[bool] = mapped_column(Boolean, default=True, index=True)

    account:Mapped['Account'] = relationship('Account', back_populates='doctor', uselist=False, lazy='joined')
    speciality:Mapped['Speciality'] = relationship('Speciality', back_populates='doctor', lazy='joined')
    certificates:Mapped[list[Certificate]] = relationship('Certificate', back_populates='doctor', uselist=True, lazy='selectin')
    chats:Mapped[list[Chat]] = relationship('Chat', back_populates='doctor', uselist=True, lazy='subquery')
    users:Mapped[list[User]] = relationship('User', back_populates='doctor', secondary='chat', uselist=True, lazy='subquery')
    feedbacks:Mapped[list[Feedback]] = relationship('Feedback', back_populates='doctor', lazy='joined', uselist=True)

    __table_args__ = (UniqueConstraint('account_id', 'speciality_id', name='account_speciality_uc'), )

    def __repr__(self) -> str:
        return f'{self.account.last_name} {self.account.first_name}\n speciality:{self.speciality.title}'

