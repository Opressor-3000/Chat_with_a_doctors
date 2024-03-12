from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
   from .account import AccountID


class DiseaseBase(BaseModel):
   title: str
   code: int

   class Config:
      orm_mode = True

class DiseaseID(DiseaseBase):
   id: int


class CreateDisease(DiseaseBase):
   creater_id: 'AccountID'


class DiseaseInfo(CreateDisease):
   id: int


class DiseaseUpdate(DiseaseID):
   title: str | None = None
   code: int | None = None
   creater_id: 'AccountID'


   