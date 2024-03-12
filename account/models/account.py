from datetime import datetime
from typing import TYPE_CHECKING, List
import uuid
from uuid import UUID as sqluuid


from sqlalchemy import (
    String,
    Boolean,
    Integer,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import EmailStr
if TYPE_CHECKING:
    from doctors.models import Feedback
from core.models import Base
from .diseaselistmxn import DiseaseListRelationMixin
from .user_mixin import UserListRelationMixin
from doctors.models.mixin import SpecialityListRelationMxn
from admin.models.accessesmxn import AccessListRelationMixin
from doctors.models.feedbackmixin import FeedbacksRelationMixin, RatingRelationMixin


class Account(
    UserListRelationMixin,
    FeedbacksRelationMixin,
    RatingRelationMixin,
    DiseaseListRelationMixin,
    AccessListRelationMixin,
    SpecialityListRelationMxn,
    Base,
):
    _ratings_back_populate = 'account'
    _ratings_uselist = True
    _ratings_lazy = 'joined'
    _ratings_secondary = 'doctor'

    _users_back_populates = "account"
    _users_lazy = "joined"
    _users_uselist = True

    _feedbacks_back_populate = 'account'
    _feedbacks_lazy = 'joined'
    _feedbacks_uselist = True
    _feedbacks_secondary = 'doctor'

    _diseases_back_populate = "account"
    _diseases_secondary = "diagnosis"
    _diseases_lazy = "joined"
    _diseases_uselist = True

    _accesses_back_populate = "account"
    _accesses_secondary = "accessaccount"
    _accesses_lazy = "joined"
    _accesses_uselist = True

    _spec_back_populate = "Account"
    _spec_lazy = "joined"
    _spec_uselist = True
    _spec_secondary = "doctor"

    uuid: Mapped[sqluuid] = mapped_column(
        default=uuid.uuid4,
        unique=True,
    )
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_enter: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    btk_db_id: Mapped[int] = mapped_column(Integer, unique=True)
    phone: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=True)
    password: Mapped[bytes] = mapped_column(String(250))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)

    account_feedbacks:Mapped[List['Feedback']] = relationship(
            'Feedback',
            back_populates='account',
            uselist=True,
            lazy='joined',
        )

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"
