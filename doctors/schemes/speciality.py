from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel
if TYPE_CHECKING:
    from account.schemes import AccountID


class BaseSpeciality(BaseModel):
    title: str


class CreateSpeciality(BaseSpeciality):
    creater_id: 'AccountID'


class SpecialityId(BaseSpeciality):
    id: int


class SpecialityUpdate(SpecialityId):
    title: str
    creater_id: 'AccountID'
