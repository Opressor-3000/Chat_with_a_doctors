from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from account.schemes import AccountID
    from doctors.schemes.agency import AgencyID


class BaseCertificate(BaseModel):
    certificate_id: str
    validity: datetime
    agency_id: 'AgencyID'


class CertificateID(BaseCertificate):
    id: int


class CreateCertificate(BaseCertificate):
    creater_id: 'AccountID'


class Certificatenfo(CreateCertificate):
    id: int


