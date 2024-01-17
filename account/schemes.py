from datetime import datetime
import uuid
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, EmailStr 



class NewUser(BaseModel):
   last_enter: datetime
   username: str
   gender_id: bool
   birthday: datetime
   qr: str | None = None


class Cookie(NewUser):
   cookie_id: NewUser


class Phone(BaseModel):
   user: 'CreateUser.uuid'
   num: int


class Role(BaseModel):
   title: str


class UserRole(BaseModel):
   uuid: uuid4
   roles: Role
   

class Speciality(BaseModel):
    title: str
    user: 'CreateUser.uuid'


class Permission(BaseModel):
   title: str
   created_at: datetime
   user: 'CreateUser.uuid'


class Groupe(BaseModel):
   title:str
   permissions:Permission
   created_at: datetime


class CreateUser(NewUser):
   uuid: uuid4
   user_id: int
   phone: Phone
   last_entrance: datetime
   email: EmailStr
   password: bytes
   avatar: bytes
   is_active: bool
   groups_id: Groupe
   role_id: Role
   created_at: datetime

