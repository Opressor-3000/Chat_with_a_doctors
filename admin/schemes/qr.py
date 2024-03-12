from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from account.schemes import AccountID


class BaseQR(BaseModel):
    qr: str


class CreateQR(BaseQR):
    creater_id: 'AccountID'


class QRID(BaseModel):
    id: int


class QRInfo(CreateQR):
    id: int

