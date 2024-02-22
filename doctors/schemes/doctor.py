from typing import Optional, List

from pydantic import BaseModel


from account.schemes import AccountId
from doctors.schemes import SpecialityId


class BaseDoctor(BaseModel):  #  1
    account_id: AccountId
    speciality_id: SpecialityId


class AccountDoctorData(AccountId):
    Speciality:List[SpecialityId]


class DoctorId(BaseDoctor):  #  1
    id: int


class ChangeDoctorActive(BaseDoctor):
    is_active: bool


class CreateDoctor(BaseDoctor):
    creater_id: AccountId
