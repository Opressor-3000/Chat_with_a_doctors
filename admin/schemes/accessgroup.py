from pydantic import BaseModel


from admin.schemes import Accessid, PermissionId, GroupId


class BaseAccessGroup(BaseModel):
    group_id: GroupId
    access_id: Accessid


class AccessGroupId(BaseAccessGroup):
    id: int


class CreateAccessGroup(BaseAccessGroup):
    creater_id: PermissionId
