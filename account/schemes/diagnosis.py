from pydantic import BaseModel
from doctors.schemes import DoctorId
from .user import User

class DiagnosisBase(BaseModel):
   doctor_id: DoctorId
   user_id: User
   text: str

   class Config:
      orm_mode = True


class DiagnosisID(DiagnosisBase):
   id: int


class DiagnosisUpdate(DiagnosisID):
   doctor_id: DoctorId | None = None
   user_id: User | None = None
   text: str | None = None


class DiagnosisDelete(DiagnosisID):
   doctor_id: DoctorId