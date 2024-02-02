from pydantic import BaseModel


from account.schemes import AccountId


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
