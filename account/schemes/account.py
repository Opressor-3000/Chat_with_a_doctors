
from pydantic import BaseModel, EmailStr


class AccountBase(BaseModel):
   first_name: str
   last_name: str
   phone: int
   email: EmailStr | None = None

   class Config:
      orm_mode = True


class AccountId(AccountBase):
   id: int


class CreateAccount(AccountBase):
   password: bytes



class AccountUpdate(AccountBase):
   first_name: str | None = None
   last_name: str | None = None
   email: EmailStr | None = None


class ChangePassword(BaseModel):
   phone: int | None = None
   password: bytes

