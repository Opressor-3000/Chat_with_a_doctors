from datetime import datetime

from pydantic import BaseModel


from admin.schemes import PermissionId
from .doctor import DoctorId
from doctors.schemes import AgencyID


class BaseCertificate(BaseModel):
    doctor_id: DoctorId
    certificate_id: str
    validity: datetime
    agency_id: AgencyID


class CertificateId(BaseCertificate):
    id: int


class CreateCertificate(BaseCertificate):
    creater_id: PermissionId

