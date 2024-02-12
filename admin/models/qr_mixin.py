from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .qr import QR


class QRRelationMixin:
    _qr_ondelete:str = 'RESTRICT'
    _qr_onupdate: str = 'CASCADE'
    _qr_foreignkey_name: str
    _qr_back_populate: str
    _qr_lazy: str
    _qr_uselist: str

    @declared_attr
    def qr_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, 
            ForeignKey(
                'qr.id', 
                name=cls._qr_foreignkey_name,
                ondelete=cls._qr_ondelete, 
                onupdate=cls._qr_onupdate,
               ),
            )

    @declared_attr
    def qr(cls) -> Mapped['QR']:
        return relationship(
            'qr',
            back_populates=cls._qr_back_populate,
            lazy=cls._qr_lazy,
            uselist=cls._qr_uselist,
        )
