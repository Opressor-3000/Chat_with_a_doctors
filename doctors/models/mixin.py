from sqlalchemy.orm import declared_attr, mapped_column, relationship, Mapped
from sqlalchemy import ForeignKey

from account.models.mixin import UserRelationMixin
from .doctor import Doctor
from .speciality import Speciality, CreaterRelationMixin


class SpecialityRelationMixin:
    _spec_back_populate: str | None = None
    _spec_nullable: bool = False
    _spec_unique: bool = False
    
    @declared_attr
    def speciality_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('speciality.id'), unique=cls._spec_unique, nullable=cls._spec_nullable)
    

    @declared_attr
    def speciality(cls) -> Mapped['Speciality']:
        return relationship('Speciality', back_populates=cls._spec_back_populate)


class DoctorRelationMixin:
    _doc_back_populate: str | None = None
    _doc_nullable: bool = False
    _doc_unique: bool = False

    @declared_attr
    def doctor_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('doctor.id'), nullable=cls._doc_nullable, unique=cls._doc_unique)
    
    @declared_attr
    def user(cls) -> Mapped['Doctor']:
        return relationship('Doctor', back_populates=cls._doc_back_populate)


class CreaterDocSpecMixin(DoctorRelationMixin, CreaterRelationMixin):
    pass


class UserDocRelationMixin(DoctorRelationMixin, UserRelationMixin):
    pass

