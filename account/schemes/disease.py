from pydantic import BaseModel
from admin.schemes import PermissionId


class DiseaseBase(BaseModel):
   title: str
   code: int

   class Config:
      orm_mode = True


class CreateDisease(DiseaseBase):
   creater_id: PermissionId


class DiseaseID(CreateDisease):
   id: int
