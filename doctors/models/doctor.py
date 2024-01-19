from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from account.models import Account
from account.models.mixin import CreaterRelationMixin
from .speciality import Speciality


class Doctor(CreaterRelationMixin, Base):
    _creater_back_populates = 'doctor'
    account_id:Mapped[int] = mapped_column(ForeignKey('account.id')) # create if exist current sertificate CHECH
    speciality_id:Mapped[int] = mapped_column(ForeignKey('speciality.id'))

    account:Mapped['Account'] = relationship('Account', back_populates='doctor')
    speciality:Mapped['Speciality'] = relationship('Speciality', back_populates='doctor')

