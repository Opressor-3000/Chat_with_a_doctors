from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint, ForeignKey

from core.models import Base
from .mixin import UserRelationMixin
from admin.models.mixin import CreaterRelationMixin
from .account import Account
from doctors.models.mixin import DoctorRelationMixin


class Disease(CreaterRelationMixin, Base):
    _creater_back_populates = 'disease'

    title:Mapped[str] = mapped_column(String(64), unique=True)
    code:Mapped[int] = mapped_column(Integer, unique=True)



class Anamnesis(DoctorRelationMixin, Base):
    _doc_back_populate = 'anamnesis'

    account_id:Mapped[int] = mapped_column(ForeignKey('account.id', ondelete='RESTRICT'))
    disease_id:Mapped[int] = mapped_column(ForeignKey('disease.id', ondelete='RESTRICT'))

    account:Mapped['Account'] = relationship('Account', back_populates='anamnesis')
    disease:Mapped['Disease'] = relationship('Disease', back_populates='anamnesis')
    
    __table_args__ = (UniqueConstraint('account_id', 'disease_id', name='account_disease_uc'), )



class Diagnosis(DoctorRelationMixin, UserRelationMixin, Base):
    _doc_back_populate = 'diagnosis'
    _user_back_populates = 'diagnosis'

    text:Mapped[str] = mapped_column(String(1024))