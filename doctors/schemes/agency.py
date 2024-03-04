from pydantic import BaseModel


from account.schemes import AccountID


class BaseAgency(BaseModel):
    title: str


class AgencyID(BaseAgency):
    id: int


class CreateAgency(BaseAgency):
    creater_id: AccountID


class AccountInfo(CreateAgency):
    id: int