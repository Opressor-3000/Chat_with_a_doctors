
from pydantic import BaseModel
from admin.schemes import PermissionId



class GenderBase(BaseModel):
   title:str

   class Config:
       orm_mode = True


class GenderID(GenderBase):
   id: int


class GenderUpdate(GenderID):
      title:str
      creater_id: PermissionId


