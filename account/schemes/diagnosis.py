from pydantic import BaseModel
from doctors.schemes import DoctorId
from .user import UserID

class DiagnosisBase(BaseModel):
   doctor_id: DoctorId
   user_id: UserID
   text: str

   class Config:
      orm_mode = True


class DiagnosisID(DiagnosisBase):
   id: int


class DiagnosisUpdate(DiagnosisID):
   doctor_id: DoctorId | None = None
   user_id: UserID | None = None
   text: str | None = None


class DiagnosisDelete(DiagnosisID):
   doctor_id: DoctorId