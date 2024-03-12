from typing import TYPE_CHECKING, List


from sqlalchemy.orm import declared_attr, Mapped, relationship

if TYPE_CHECKING:
    from .doctor import Doctor


class DoctorListRelationMixin:
    _doctors_back_populate:str
    _doctors_lazy:str
    _doctors_secondary:str | None = None
    _doctors_uselist:bool

    @declared_attr
    def doctors(cls) -> Mapped[List['Doctor']]:
        return relationship(
            back_populates=cls._doctors_back_populate,
            secondary=cls._doctors_secondary,
            lazy=cls._doctors_lazy,
            uselist=cls._doctors_uselist,
        )
