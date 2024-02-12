from typing import TYPE_CHECKING

from sqlalchemy.orm import declared_attr, Mapped, relationship

if TYPE_CHECKING:
    from .certificate import Certificate


class CertificateListRelationMixin:
    _certificates_back_populate: str
    _certificates_lazy: str
    _certificates_uselist:str
    _certificates_secondary:str | None = None

    @declared_attr
    def certificate(cls) -> Mapped[list['Certificate']]:
        return relationship(
            'Certificate',
            back_populates=cls._certificates_back_populate, 
            lazy=cls._certificates_lazy, 
            uselist=cls._certificates_uselist,
            secondary=cls._certificates_secondary,
        )
