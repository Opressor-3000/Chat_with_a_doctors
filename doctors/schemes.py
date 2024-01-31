from datetime import datetime

from pydantic import BaseModel

from chat.schemes import ChatId
from account.schemes import AccountId, UserID
from admin.schemes import PermissionId


#----------------   SPECIALITY   -----------------------


class BaseSpeciality(BaseModel):
    title: str
    

class CreateSpeciality(BaseSpeciality):
    creater_id: PermissionId


class SpecialityId(BaseSpeciality):
    id: int


class SpecialityUpdate(SpecialityId):
    title: str
    creater_id: PermissionId


# -----------------   DOCTOR  ----------------------


class BaseDoctor(BaseModel):
    account_id: AccountId
    speciality_id: SpecialityId


class DoctorId(BaseDoctor):
    id: int


class ActiveDoctor(BaseDoctor):
    is_active: bool


class CreateDoctor(BaseDoctor):
    creater_id: PermissionId


#  ------------------  AGENCY  -------------------


class BaseAgency(BaseModel):
    title: str


class CreateAgency(BaseAgency):
    creater_id: PermissionId


# -------------------  CERTIFICATE  -----------------


class BaseCertificate(BaseModel):
    doctor_id: DoctorId
    certificate_id: str
    validity: datetime
    agency_id: BaseAgency


class CertificateId(BaseCertificate):
    id: int


class CreateCertificate(BaseCertificate):
    creater_id: PermissionId


# ----------------   FEEDBACK  --------------------


class BaseFeedback(BaseModel):
    chat_id: ChatId
    dcotor_id: DoctorId
    user_id: UserID
    text: str


class FeedbackID(BaseFeedback):
    id: int


class BanFeedback(FeedbackID):
    creater_id: PermissionId
    delete: bool
    deleted_at: datetime


# ------------------   RATING ------------------


class BaseRating(BaseModel):
    user_id: UserID
    chat_id: ChatId
    doctor_id: DoctorId
    point: int


class RatingID(BaseRating):
    id: int


    
