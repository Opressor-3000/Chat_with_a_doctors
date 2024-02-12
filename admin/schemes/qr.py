
from pydantic import BaseModel

from admin.schemes import PermissionId


class BaseQR(BaseModel):
    qr: str


class CreateQR(BaseQR):
    creater_id:PermissionId


