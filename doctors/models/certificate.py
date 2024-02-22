from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from core.models import Base
from doctors.models.mixin import CreaterDocSpecMixin
from .agency import Agency


class Certificate(
    CreaterDocSpecMixin, 
    Base
):
    _creater_back_populates = 'certificate'
    _creater_foreignkey_name = 'cretificate_creater_id'

    _doc_back_populate = 'certificate'
    _doc_foreignkey_name = 'cretificate_doctor_id'
    _doc_lazy = 'joined'
    _doc_uselist = False
    
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
        lazy='joined',
    )