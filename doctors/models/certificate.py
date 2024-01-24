from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr
from sqlalchemy import ForeignKey

from core.models import Base
from doctors.models.mixin import CreaterDocSpecMixin
from .agency import Agency


class Certificate(CreaterDocSpecMixin, Base):
    _creater_back_populates = 'certificate'
    _doc_back_populate = 'certificate'
    
    cretificate_id: Mapped[str] = mapped_column(String(64), unique=True)
    validity: Mapped[datetime]   # constrain не более 5 лет
    agency_id: Mapped[int] = mapped_column(Integer, ForeignKey('agency.id', name='certificate_agency'))
    agency:Mapped['Agency'] = relationship('Agency', back_populates='certificate')
