from typing import TYPE_CHECKING

from sqlalchemy.orm import declared_attr, Mapped, relationship

if TYPE_CHECKING:
    from .agency import Agency


class AgencyRelationMixin:
    _agency_back_populate: str
    _agency_lazy: str
    _agency_uselist: bool

    @declared_attr
    def agency(cls) -> Mapped['Agency']:
        return relationship(
            back_populates=cls._agency_back_populate, 
            lazy=cls._agency_lazy, 
            uselist=cls._agency_uselist,
        )
