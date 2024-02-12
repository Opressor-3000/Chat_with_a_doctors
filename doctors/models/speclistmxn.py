from typing import TYPE_CHECKING


from sqlalchemy.orm import declared_attr, mapped_column, relationship, Mapped

if TYPE_CHECKING:
    from .speciality import Speciality


class SpecialityListRelationMixin:
    _specs_back_populate: str
    _specs_lazy: str
    _specs_uselist: bool
    _specs_secondary: str | None = None

    @declared_attr
    def specialities(cls) -> Mapped[list['Speciality']]:
        return relationship(
            'Speciality',
            back_populates=cls._spec_back_populate,
            secondary=cls._spec_secondary,
            lazy=cls._spec_lazy,
            uselist=cls._spec_uselist,
        )
