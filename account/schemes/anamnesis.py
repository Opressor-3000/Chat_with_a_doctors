from pydantic import BaseModel

from .account import AccountId
from .disease import DiseaseID
from doctors.schemes import DoctorId
   

class AnamnesisBase(BaseModel):
   account_id: AccountId
   disease_id: DiseaseID
   doctor_id: DoctorId

   class Config:
      orm_mode = True


class AnamnesisUpdate(AnamnesisBase):
   account_id: AccountId | None = None
   disease_id: DiseaseID | None = None
   doctor_id: DoctorId | None = None


class AnamnesisID(AnamnesisBase):
   id: int


class AnamnesisDelete(AnamnesisID):
   pass


