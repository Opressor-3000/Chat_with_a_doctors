from pydantic import BaseModel
from admin.schemes import PermissionId


class DiseaseBase(BaseModel):
   title: str
   code: int

   class Config:
      orm_mode = True


class DiseaseID(DiseaseBase):
   id: int


class CreateDisease(DiseaseBase):
   creater_id: PermissionId