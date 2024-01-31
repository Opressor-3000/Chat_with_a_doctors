from pydantic import BaseModel

from account.schemes import AccountId


# -----------------  ACCESS -------------------


class BaseAccess(BaseModel):
    title: str
    parent_id: 'Accessid' | None = None


class Accessid(BaseAccess):
    id: int


# -----------------  ACCESS GROUP ----------------


class BaseAccessGroup(BaseModel):
    group_id: 'GroupId'
    access_id: Accessid


class AccessGroupId(BaseAccessGroup):
    id: int


class CreateAccessGroup(BaseAccessGroup):
    creater_id: 'PermissionId'


# -------------------  GROUP --------------------


class BaseGroup(BaseModel):
    title: str
    is_active: bool


class CreateGroup(BaseGroup):
    creater_id: 'PermissionId'


class GroupId(BaseGroup):
    id: int


class UpdateGroup(GroupId):
    is_active: bool | None = None



# -------------------  PERMISSION ----------------


class BasePermission(BaseModel):
    account_id: AccountId
    group_id: int
    creater_id: 'PermissionId'
    is_active: bool


class PermissionId(BasePermission):
    id: BasePermission


class PermissionCreate(PermissionId):
    pass


class PermissionUpdate(PermissionId):
    is_active: bool  | None = None


# ----------------------- QR --------------------
    

class BaseQR(BaseModel):
    qr: str


class CreateQR(BaseQR):
    creater_id:PermissionId


