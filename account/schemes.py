from datetime import datetime
import uuid
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, EmailStr 

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


class Gender(GenderBase):
   id: str


class UserBase(BaseModel):   # поля по умолчанию
   gender: Gender | None = None
   birthday: datetime | None = None
   avatar: str | None = None
   username: str


class User(UserBase): # присваивается при входе
   cookie_id: str


class NewUser(User):  #  обязательное поле для открытия чата 
   qr: str | None = None


class UserUpdate(UserBase):
   pass


class AccountBase(BaseModel):
   first_name: str
   last_name: str


class Account(AccountBase):
   id: int


class CreateAccount(AccountBase):
   phone: int
   email: EmailStr | None = None
   password: bytes



class UserAccount():
   pass


class Speciality(BaseModel):
    title: str
    user: 'UserBase.uuid'
