from sqlalchemy.orm import declared_attr, Mapped, relationship


from .disease import Disease


class DiseaseListRelationMixin:
    _diseases_back_populate:str
    _diseases_lazy:str
    _diseases_uselist:bool
    _diseases_secondary:str | None = None

    @declared_attr
    def disease(cls) -> Mapped[list[Disease]]:
        return relationship(
            back_populates=cls._diseases_back_populate,
            secondary=cls._diseases_secondary,
            lazy=cls._diseases_lazy,
            uselist=cls._diseases_uselist,
        )