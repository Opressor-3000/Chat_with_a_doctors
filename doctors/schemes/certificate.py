from datetime import datetime

from pydantic import BaseModel


from account.schemes import AccountID
from doctors.schemes.agency import AgencyID


class BaseCertificate(BaseModel):
    certificate_id: str
    validity: datetime
    agency_id: AgencyID


class CertificateID(BaseCertificate):
    id: int


class CreateCertificate(BaseCertificate):
    creater_id: AccountID


class Certificatenfo(CreateCertificate):
    id: int