from typing import TYPE_CHECKING


from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer


if TYPE_CHECKING:
    from .feedback import Feedback


class FeedbackRelationMixin:
    _feedback_back_populate: str
    _feedback_uselist:bool
    _feedback_lazy:str
    _feedback_secondary: str | None = None
    _feedback_foreignkey_name:str
    _feedback_ondelete: str = 'CASCADE'
    _feedback_onupdate: str = 'CASCADE'
    _feedback_unique: bool = False
    _feedback_nullable: bool = True

    @declared_attr
    def feedback_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, 
            ForeignKey(
                'feedback.id',
                name=cls._feedback_foreignkey_name,
                ondelete=cls._feedback_ondelete,
                onupdate=cls._feedback_onupdate,
            ),
            unique=cls._feedback_unique,
            nullable=cls._feedback_nullable
        )

    @declared_attr
    def feedback(cls) -> Mapped['Feedback']:
        return relationship(
            'Feedback',
            back_populates=cls._feedback_back_populate,
            uselist=cls._feedback_uselist,
            lazy=cls._feedback_lazy,
        )


class FeedbacksRelationMixin:
    _feedback_back_populate: str
    _feedback_uselist:bool
    _feedback_lazy:str
    _feedback_secondary: str | None = None

    @declared_attr
    def feedbacks(cls) -> Mapped[list['Feedback']]:
        return relationship(
            'Feedback',
            back_populates=cls._feedback_back_populate,
            uselist=cls._feedback_uselist,
            lazy=cls._feedback_lazy,
            secondary=cls._feedback_secondary
        )