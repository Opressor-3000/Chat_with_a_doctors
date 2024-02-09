from sqlalchemy.orm import declared_attr, Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey

from .gender import Gender


class GenderRelationMixin:
    _gender_foreignkey_name:str
    _gender_ondelete: str = 'RESTRICT'
    _gender_onupdate:str = "RESTRICT"
    _gender_back_populate: str
    _gender_uselist: bool
    _gender_lazy: str

    @declared_attr
    def gender_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, 
            ForeignKey(
                "gender.id", 
                ondelete=cls._gender_ondelete, 
                onupdate=cls._gender_onupdate,
                name=cls._gender_foreignkey_name,
            ),
        )

    @declared_attr
    def gender(cls) -> Mapped[Gender]:
        return relationship(
            'Gender',
            back_populates=cls._gender_back_populate,
            lazy=cls._gender_lazy,
            uselist=cls._gender_uselist,
        )
