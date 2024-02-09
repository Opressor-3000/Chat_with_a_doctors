from datetime import datetime

from pydantic import BaseModel

from admin.schemes import PermissionId


class BaseSpeciality(BaseModel):
    title: str
    

class CreateSpeciality(BaseSpeciality):
    creater_id: PermissionId


class SpecialityId(BaseSpeciality):
    id: int


class SpecialityUpdate(SpecialityId):
    title: str
    creater_id: PermissionId


