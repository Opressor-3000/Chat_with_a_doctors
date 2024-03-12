from typing import Optional, List, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from account.schemes import AccountID
    from doctors.schemes import SpecialityId


class BaseDoctor(BaseModel):  #  1
    account_id: 'AccountID'
    speciality_id: 'SpecialityId'


# class AccountDoctorData('AccountID'):
#     Speciality: List['SpecialityId']


class DoctorId(BaseDoctor):  #  1
    id: int


class ChangeDoctorActive(BaseDoctor):
    is_active: bool


class CreateDoctor(BaseDoctor):
    creater_id: 'AccountID'


