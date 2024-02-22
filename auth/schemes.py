from datetime import datetime
from typing import Annotated
import uuid

from fastapi import Cookie
from fastapi.security import HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, EmailStr, ConfigDict


class AuthJWTScheme(BaseModel):
   model_config = ConfigDict(strict=True)
   
   first_name: str
   last_name: str
   phone: int
   password: bytes
   email: EmailStr | None = None


class TokenInfo(BaseModel):
   access_token:str
   token_type: str


class BasicCookieAuth(HTTPBasicCredentials):
   password: Annotated[str, Cookie]
   

