from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint, ForeignKey

from core.models import Base
from .accounts_mixin import AccountListRelationMixin, AccountRelationMixin

from admin.models.mixin import CreaterRelationMixin
from doctors.models.mixin import DoctorRelationMixin


class Disease(
    CreaterRelationMixin,
    AccountListRelationMixin,
    Base,
):
    _creater_back_populates = "disease"
    _creater_foreignkey_name = "disease_creater_fk"

    _accounts_back_populate = "disease"
    _accounts_secondary = "diagnosis"
    _accounts_lazy = "joined"
    _accounts_uselist = True

    title: Mapped[str] = mapped_column(String(64), unique=True)
    code: Mapped[int] = mapped_column(Integer, unique=True)

    def __repr__(self) -> str:
        return f"{self.title}"
    

class Diagnosis(
    AccountRelationMixin,
    DoctorRelationMixin,
    Base,
):
    _account_foreignkey_name = "diagnosis_account_fk"
    _account_nullable = False
    _account_unique = False
    _account_onupdate = "CASCADE"
    _account_ondelete = "CASCADE"
    _account_back_populate = "diagnosis"
    _account_lazy = "joined"
    _account_uselist = False

    _doc_back_populate = "diagnosis"
    _doc_lazy = "joined"
    _doc_uselist = False
    _doc_foreignkey_name = "diagnosis_doc_fk"

    text: Mapped[str] = mapped_column(String(1024))
    disease_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "disease.id",
            name="disease_diagnosis",
            ondelete="NO ACTION",
            onupdate="NO ACTION",
        ),
        nullable=True,
    )
    current_disease:Mapped[bool] = mapped_column(Boolean, default=True)
    disease: Mapped[Disease] = relationship(
        "Disease", back_populates="diagnosis", uselist=True, lazy="joined"
    )
    __table_args__ = (
        UniqueConstraint(
            "account_id", "disease_id", name="diagnosis_account_disease_uc"
        ),
    )

    def __repr__(self) -> str:
        return f"disease:{self.disease.title}"


























# class Anamnesis(
#     AccountRelationMixin,
#     DoctorRelationMixin,
#     Base,
# ):
#     _account_foreignkey_name = 'anamnesis_account_fk'
#     _account_nullable = False
#     _account_unique = False
#     _account_onupdate = 'CASCADE'
#     _account_ondelete = 'CASCADE'
#     _account_back_populate = 'anmnesis'
#     _account_lazy = 'joined'
#     _account_uselist = False

#     _doc_back_populate = "anamnesis"
#     _doc_foreignkey_name = 'anamnesis_doctor_fk'
#     _doc_lazy = "joined"
#     _doc_uselist = False

#     disease_id: Mapped[int] = mapped_column(
#         Integer,
#         ForeignKey(
#             "disease.id",
#             name="disesase_anamnesis",
#             ondelete="CASCADE",
#         ),
#     )

#     __table_args__ = (
#         UniqueConstraint(
#             "account_id", "disease_id", name="anamnesis_account_disease_uc"
#         ),
#     )
#     disease: Mapped[Disease] = relationship(
#         "Anamnesis", back_populates="anamnesis", uselist=True, lazy="joined"
#     )

#     def __repr__(self) -> str:
#         return f"disease:{self.disease.title}"


