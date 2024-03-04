from sqlalchemy.orm import relationship, Mapped, declared_attr

from .mixin import UserDocRelationMixin, UserDocRelationMixin
from chat.models.mixin import ChatRelationMixin
from account.models import Account

class DocChatUserRelationMixin(ChatRelationMixin, UserDocRelationMixin):
    pass


class DoctorAccountRelationMxn:
    _doctor_account_back_populate: str
    _doctor_account_uselist: bool
    _doctor_account_lazy:str | None = None
    _doctor_account_secondary: str | None = None

    @declared_attr
    def doctor_account(cls) -> Mapped['Account']:
        return relationship(
            'Account', 
            back_populates=cls._doctor_account_back_populate, 
            uselist=cls._doctor_account_uselist, 
            lazy=cls._doctor_account_lazy,
            secondary=cls._doctor_account_secondary,
        )