from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base
from account.models import Account
from account.models.mixin import CreaterRelationMixin


class Doctor(CreaterRelationMixin, Base):
    account_id:Mapped[int] = mapped_column(ForeignKey('account.id')) # create if exist current sertificate CHECH
    speciality:Mapped[int] 

    account:Mapped['Account'] = relationship(back_populates='account.id')
