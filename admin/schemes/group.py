from typing import Optional

from pydantic import BaseModel


from admin.schemes import PermissionId


class BaseGroup(BaseModel):
    title: str
    is_active: bool


class CreateGroup(BaseGroup):
    creater_id: 'PermissionId'


class GroupId(BaseGroup):
    id: int


class UpdateGroup(GroupId):
    is_active: bool | None = None
