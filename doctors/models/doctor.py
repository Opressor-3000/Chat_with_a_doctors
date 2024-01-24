from datetime import datetime
from sqlalchemy import ForeignKey, UniqueConstraint, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from account.models import Account
from account.models.mixin import CreaterRelationMixin
from .speciality import Speciality


class Doctor(CreaterRelationMixin, Base):
    _creater_back_populates = 'doctor'
    
    account_id:Mapped[int] = mapped_column(Integer, ForeignKey('account.id', ondelete='RESTRICT', onupdate='CASCADE'), name='account_doc') # create if exist current sertificate CHECH
    speciality_id:Mapped[int] = mapped_column(Integer, ForeignKey('speciality.id', ondelete='RESTRICT', onupdate='CASCADE', name='speciality_doc'))
    is_active:Mapped[bool] = mapped_column(Boolean, default=True)

    account:Mapped['Account'] = relationship('Account', back_populates='doctor')
    speciality:Mapped['Speciality'] = relationship('Speciality', back_populates='doctor')

    # __table_args__ = (UniqueConstraint('account_id', 'speciality_id', name='account_speciality_uc'), )


