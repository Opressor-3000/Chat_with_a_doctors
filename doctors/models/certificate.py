from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr
from sqlalchemy import ForeignKey

from core.models import Base
from doctors.models import CreaterDocSpecMixin
from .speciality import Speciality
from .agency import Agency

class Certificate(CreaterDocSpecMixin, Base):
    _creater_back_populates = 'certificate'
    _doc_back_populate = 'certificate'
    _spec_back_populate = 'certificate'
    
    validity: Mapped[datetime]   # constrain не более 5 лет
    agency_id: Mapped[str] = mapped_column(ForeignKey('agency.id'))



