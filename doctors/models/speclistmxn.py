from sqlalchemy.orm import declared_attr, mapped_column, relationship, Mapped
from .speciality import Speciality


class SpecialityListRelationMixin:
    _spec_back_populate: str
    _spec_lazy: str
    _spec_uselist: bool
    _spec_secondary: str | None = None

    @declared_attr
    def specialities(cls) -> Mapped[list[Speciality]]:
        return relationship(
            'Speciality',
            back_populates=cls._spec_back_populate,
            secondary=cls._spec_secondary,
            lazy=cls._spec_lazy,
            uselist=cls._spec_uselist,
        )
