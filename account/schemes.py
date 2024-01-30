from datetime import datetime
import uuid

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, EmailStr, ConfigDict


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


#  -----------------------------   USER  SCHEMES   --------------------------


class GenderBase(BaseModel):
   title:str


class Gender(GenderBase):
   id: int


class UserBase(BaseModel):   # поля по умолчанию
   gender: Gender | None = None
   birthday: datetime | None = None
   avatar: str | None = None
   username: str


class UserCookie(UserBase):
   cookie: str


class UserScheme(UserCookie): # присваивается при входе
   model_config = ConfigDict(from_attributes=True)

   id: str


class UserCreate(UserScheme):
   pass


class UserUpdate(UserBase):
   username: str | None = None


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


