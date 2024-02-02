from pydantic import BaseModel


from admin.schemes import PermissionId



class BaseAgency(BaseModel):
    title: str


class AgencyID(BaseAgency):
    id: int


class CreateAgency(BaseAgency):
    creater_id: PermissionId


