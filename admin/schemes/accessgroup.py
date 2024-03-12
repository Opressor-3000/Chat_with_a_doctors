from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemes import AccessID
    from account.schemes import AccountID


class AccessAccountBase(BaseModel):
    account: 'AccountID'
    access: 'AccessID'


class AccessAccountID(AccessAccountBase):
    id: int


class CreateAccessAccount(AccessAccountBase):
    creater_id: 'AccessID'


class AccessAccountInfo(CreateAccessAccount):
    id: int


class AccessAccountUpdate(AccessAccountBase):
    account: 'AccountID'
    access: 'AccessID'