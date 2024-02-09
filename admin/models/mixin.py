from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from .qr import QR
from admin.models.permission import Permission


class CreaterRelationMixin:
    _creater_unique: bool = False
    _creater_back_populates: str
    _creater_id_nullable: bool = False
    _creater_lazy: str | None = None
    _creater_ondelete: str = "RESTRICT"
    _creater_onupdate: str = "RESTRICT"
    _creater_foreignkey_name: str

    @declared_attr
    def creater_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey(
                "permission.id",
                name=cls._creater_foreignkey_name,
                ondelete=cls._creater_ondelete,
                onupdate=cls._creater_onupdate,
            ),
            nullable=cls._creater_id_nullable,
            unique=cls._creater_unique,
        )

    @declared_attr
    def creater(cls) -> Mapped["Permission"]:
        return relationship(
            "Permission",
            back_populates=cls._creater_back_populates,
            lazy=cls._creater_lazy,
        )


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
    def qr(cls) -> Mapped[QR]:
        return relationship(
            'qr',
            back_populates=cls._qr_back_populate,
            lazy=cls._qr_lazy,
            uselist=cls._qr_uselist,
        )
