
from pydantic import BaseModel
from .account import AccountID



class GenderBase(BaseModel):
   title:str

   class Config:
       orm_mode = True


class GenderID(GenderBase):
   id: int


class GenderCreate(GenderBase):
      title:str
      creater_id: AccountID


class GenderInfo(GenderCreate):
    id: int


class GenderUpdate(GenderCreate):
      pass


