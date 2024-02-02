from pydantic import BaseModel


from account.schemes import AccountId
from admin.schemes import PermissionId
from doctors.schemes import SpecialityId


class BaseDoctor(BaseModel):
    account_id: AccountId
    speciality_id: SpecialityId


class DoctorId(BaseDoctor):
    id: int


class ActiveDoctor(BaseDoctor):
    is_active: bool


class CreateDoctor(BaseDoctor):
    creater_id: PermissionId