from sqlalchemy.orm import declared_attr, mapped_column
from sqlalchemy import ForeignKey

from account.models import UserRelationMixin



class SpecialityRelationMixin:
    _spec_back_populate: str = 'speciality'
    
    @declared_attr
    def speciality_id(cls):
        return mapped_column(ForeignKey('speciality.id'), back_populates=cls._spec_back_populate)


class DoctorRelationMixin:
    _doc_back_populate: str = 'doctor'

    @declared_attr
    def doctor_id(cls):
        return mapped_column(ForeignKey('doctor.id'), back_populates=cls._doc_back_populate)
    


class DocSpecRelationMixin(DoctorRelationMixin, SpecialityRelationMixin):
    pass


class UserDocSpecMixin(DocSpecRelationMixin, UserRelationMixin):
    pass


