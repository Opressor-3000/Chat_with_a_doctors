
from pydantic import BaseModel
from admin.schemes import PermissionId



class GenderBase(BaseModel):
   title:str

   class Config:
       orm_mode = True


class GenderID(GenderBase):
   id: int


class GenderCreate(GenderID):
   creater_id: PermissionId


class GenderUpdate(GenderCreate):
      title:str
      creater_id: PermissionId


