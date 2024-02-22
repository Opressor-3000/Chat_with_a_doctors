from typing import TYPE_CHECKING


from sqlalchemy.orm import declared_attr, mapped_column, relationship, Mapped
from sqlalchemy import ForeignKey, Integer

from account.models.user_mixin import UserRelationMixin
from admin.models.mixin import CreaterRelationMixin
if TYPE_CHECKING:
    from account.models.user_mixin import UserRelationMixin
    from .doctor import Doctor
    from .speciality import Speciality


class SpecialityRelationMixin:
    _spec_back_populate: str
    _spec_nullable: bool = False
    _spec_unique: bool = False
    _spec_lazy: str | None = None
    _spec_uselist: bool
    _spec_ondelete: str = 'RESTRICT'
    _spec_onupdate: str = 'CASCADE'
    _spec_foreignkey_name: str
    
    @declared_attr
    def speciality_id(cls) -> Mapped[int | None]:
        return mapped_column(
            Integer, 
            ForeignKey(
                'speciality.id', 
                name=cls._spec_foreignkey_name,
                ondelete=cls._spec_ondelete, 
                onupdate=cls._spec_onupdate,
            ), 
            unique=cls._spec_unique, 
            nullable=cls._spec_nullable
        )
    

    @declared_attr
    def speciality(cls) -> Mapped['Speciality']:
        return relationship(
            'Speciality', 
            back_populates=cls._spec_back_populate, 
            lazy=cls._spec_lazy, 
            uselist=cls._spec_uselist,
        )


class DocRelationMixin:
    _doc_back_populate: str
    _doc_lazy: str 
    _doc_uselist: bool
    _doc_secondary:str | None = None


    @declared_attr
    def doctor(cls) -> Mapped['Doctor']:
        return relationship(
            'Doctor', 
            back_populates=cls._doc_back_populate, 
            lazy=cls._doc_lazy, 
            uselist=cls._doc_uselist,
            secondary=cls._doc_secondary,
        )


class DoctorRelationMixin:
    _doc_back_populate: str
    _doc_nullable: bool = False
    _doc_unique: bool = False
    _doc_lazy: str 
    _doc_uselist: bool
    _doc_ondelete: str = 'RESTRICT'
    _doc_onupdate: str = 'CASCADE'
    _doc_foreignkey_name: str
    _doc_secondary:str | None = None

    @declared_attr
    def doctor_id(cls) -> Mapped[int | None]:
        return mapped_column(
            Integer, 
            ForeignKey(
                'doctor.id', 
                name=cls._doc_foreignkey_name,
                onupdate=cls._doc_onupdate, 
                ondelete=cls._doc_ondelete,
            ), 
            nullable=cls._doc_nullable, 
            unique=cls._doc_unique,
        )
    
    @declared_attr
    def doctor(cls) -> Mapped['Doctor']:
        return relationship(
            'Doctor', 
            back_populates=cls._doc_back_populate, 
            lazy=cls._doc_lazy, 
            uselist=cls._doc_uselist,
            secondary=cls._doc_secondary,
        )


class CreaterDocSpecMixin(DoctorRelationMixin, CreaterRelationMixin):
    pass


class UserDocRelationMixin(DoctorRelationMixin, UserRelationMixin):
    pass

