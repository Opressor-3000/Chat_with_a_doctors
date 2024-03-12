from typing import TYPE_CHECKING, List


from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer


if TYPE_CHECKING:
    from .feedback import Feedback, Rating


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
    _feedbacks_back_populate: str
    _feedbacks_uselist:bool
    _feedbacks_lazy:str
    _feedbacks_secondary: str | None = None

    @declared_attr
    def feedbacks(cls) -> Mapped[List['Feedback']]:
        return relationship(
            'Feedback',
            back_populates=cls._feedbacks_back_populate,
            uselist=cls._feedbacks_uselist,
            lazy=cls._feedbacks_lazy,
            secondary=cls._feedbacks_secondary
        )


class FeedbackRelationMxn:
    _feedback_back_populate: str
    _feedback_uselist:bool
    _feedback_lazy:str
    _feedback_secondary: str | None = None

    @declared_attr
    def feedbacks(cls) -> Mapped['Feedback']:
        return relationship(
            'Feedback',
            back_populates=cls._feedback_back_populate,
            uselist=cls._feedback_uselist,
            lazy=cls._feedback_lazy,
            secondary=cls._feedback_secondary
        )


class RatingRelationMixin:
    _ratings_back_populate: str
    _ratings_uselist:bool
    _ratings_lazy:str
    _ratings_secondary: str | None = None

    @declared_attr
    def feedbacks(cls) -> Mapped['Rating']:
        return relationship(
            'Rating',
            back_populates=cls._rating_back_populate,
            uselist=cls._rating_uselist,
            lazy=cls._rating_lazy,
            secondary=cls._rating_secondary
        )
    

