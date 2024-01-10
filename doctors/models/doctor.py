from datetime import datetime


from sqlalchemy.orm import Mapped


from core.models.base import Base



class Doctor(Base):
    user_id: Mapped[int]
    sepiciality:Mapped[int]
    rating:Mapped[int]


class CurrentDoctor(Base):
    cetificate:Mapped[int]
    doctor: Mapped[int]


class Certificate(Base):
    agency:Mapped[int]
    numder: Mapped[str]


class GovAgency(Base):
    title: Mapped[str]


class Feedback(Base):
    chat_id: Mapped[int]
    doctor_id:Mapped[int]
    user_id:Mapped[int]
