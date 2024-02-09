from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, Constraint, CheckConstraint, Index, UniqueConstraint, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.schema import UniqueConstraint
from pydantic import EmailStr
from sqlalchemy import ForeignKey

from core.models import Base
if TYPE_CHECKING:
    from doctors.models import Doctor
from doctors.models.mixin import CreaterDocSpecMixin
from .agency import Agency


class Certificate(CreaterDocSpecMixin, Base):
    _creater_back_populates = 'certificate'
    _creater_foreignkey_name = 'cretificate_creater_id'
    _creater_lazy = 'joined',
    _creater_uselist = False
    _doc_back_populate = 'certificate'
    _doc_foreignkey_name = 'cretificate_doctor_id'
    _doc_lazy = 'joined'
    
    cretificate_id: Mapped[str] = mapped_column(String(64), unique=True)
    validity: Mapped[datetime] = mapped_column(DateTime) # constrain не более 5 лет
    agency_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey(
            'agency.id', 
            name='certificate_agency', 
            ondelete='RESTRICT',
            onupdate='CASCADE',
        ),
    )
    
    agency:Mapped['Agency'] = relationship(
        'Agency', 
        back_populates='certificate', 
        uselist=False, 
        lazy='joined'
    )

    doctors:Mapped[list[Doctor]] = relationship(
        'Doctor', 
        back_populates='cretificate', 
        uselist=True, lazy='joined'
    )