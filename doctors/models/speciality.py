from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base
from account.models.mixin import CreaterRelationMixin


class Speciality(CreaterRelationMixin, Base):
    _creater_back_populates = 'speciality'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)



