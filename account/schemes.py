from datetime import datetime

from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, EmailStr, ConfigDict
from admin.schemes import PermissionId
from doctors.schemes import DoctorId


'''
описываем взаимодействия с 
      1. User
         UserBase [хранит все поля кроме id cookie, account_id, qr, is_active]
         User
            CreateUser
            GetUser_id(cookie=user.cookie)
            GetAccount
            set_username
            set_gender
            set_birthday
            set_avatar


      2. Account
            get_account
               set_patch_account
               get_users_chats
                  

      3. Chats(GetUser_id)
            Doctors()
               speciality
                  chat
            Specialities
               doctors
                  chat
            chat
               message

      4. CurrentChat
            user
               chat
                  current_chat

      5. Doctors(list[Chats])
            doctor
               feedback
               chat
                  message
               rating
'''


class GenderBase(BaseModel):
   title:str


class GenderID(GenderBase):
   id: int


class GenderCreate(GenderID):
   creater_id: PermissionId


class GenderUpdate(GenderCreate):
      title:str
      creater_id: PermissionId

#  -----------------------------   USER  SCHEMES   --------------------------


class UserBase(BaseModel):   # поля по умолчанию
   username: str
   avatar: str | None = None
   birthday: datetime | None = None
   gender_id: GenderID | None = None


class UserID(UserBase): # присваивается при входе
   id: int


class UserCreate(UserID):
   account_id: 'AccountId' | None = None
   qr_id: int | None = None


class AccountUsers(UserID):
   account_id: 'AccountId' | None = None


# class UserUpdate(UserBase):
#    username: str | None = None


# -------------------------   ACCOUNT  SCHEMES   ---------------------


class AccountBase(BaseModel):
   first_name: str
   last_name: str
   phone: int
   email: EmailStr | None = None


class AccountId(AccountBase):
   id: int


class CreateAccount(AccountBase):
   password: bytes



class AccountUpdate(AccountBase):
   first_name: str | None = None
   last_name: str | None = None
   email: EmailStr | None = None


class ChangePassword(AccountBase):
   phone: int | None = None
   password: bytes


class 


# ----------------------  DISEASE  ---------------------
   

class DiseaseBase(BaseModel):
   title: str
   code: int


class DiseaseID(DiseaseBase):
   id: int


class CreateDisease(DiseaseBase):
   creater_id: PermissionId


# --------------------- ANAMNESIS ---------------------
   

class AnamnesisBase(BaseModel):
   account_id: AccountId
   disease_id: DiseaseID
   doctor_id: DoctorId


class AnamnesisUpdate(AnamnesisBase):
   account_id: AccountId | None = None
   disease_id: DiseaseID | None = None
   doctor_id: DoctorId | None = None


class AnamnesisID(AnamnesisBase):
   id: int


class AnamnesisDelete(AnamnesisID):
   pass


# ------------------- DIAGNOSIS -----------------------


class DiagnosisBase(BaseModel):
   doctor_id: DoctorId
   user_id: UserID
   text: str


class DiagnosisID(DiagnosisBase):
   id: int


class DiagnosisUpdate(DiagnosisID):
   doctor_id: DoctorId | None = None
   user_id: UserID | None = None
   text: str | None = None


class DiagnosisDelete(DiagnosisID):
   doctor_id: DoctorId
