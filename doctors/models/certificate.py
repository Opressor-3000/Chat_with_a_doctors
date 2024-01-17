from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr
from sqlalchemy import ForeignKey

from core.models import Base
from account.models import CreaterRelationMixin
from .speciality import Speciality
from .agency import Agency

class Certificate(CreaterRelationMixin, Base):
    doctor_id: Mapped[int] = mapped_column(ForeignKey('account.id'))
    speciality: Mapped[int] = mapped_column(ForeignKey('speciality.id'))
    validity: Mapped[datetime]  # constrain не более 5 лет
    agency: Mapped[str] = mapped_column(ForeignKey('agency.id'))



