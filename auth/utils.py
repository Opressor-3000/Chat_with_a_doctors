from datetime import datetime, timedelta


from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status, Cookie
import bcrypt
import jwt

from account.schemes import AccountID, CreateAccount, AccountLogin, UserID
from middleware import get_user_cookie
from core.config import COOKIE_SESSION_ID

from .crud import get_account


from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_dir.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_minutes
    else:
        expire = now + timedelta(minutes=timedelta)
    to_encode.update(exp=expire, iat=now)
    return jwt.encode(
        payload,
        private_key,
        algorithm=algorithm,
    )


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key.read_text(),
    algorithms: list[str] = [settings.auth_jwt.algorithm],
):
    return jwt.decode(
        token,
        public_key,
        algorithms,
    )


# CREATE HASH PASSWORD
def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bcrypt: bytes = password.encode()
    return bcrypt.hashpw(pwd_bcrypt, salt)


def validate_password(login_data: AccountLogin, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(login_data.password.encode(), hashed_password)


# CHECK PHONE NUMBER CONSIST ONLY DIGITS
async def validation_phone(account: AccountID):
    phone: str = account.phone
    if phone.isdigit:
        return True
    else:
        return "phone number does not consist only of numbers"


#  VALIDATE >>>  LOGIN  <<<
async def validation_auth_jwt(
    session: AsyncSession,
    login_data: AccountLogin,
):

    account = get_account(session, login_data)
    if not account:
        return False
    if validate_password(login_data.password, account.password):
        return login_data
    else:
        return False


async def account_created_phone_validate(
    session: AsyncSession,
    singin_data: CreateAccount,
):
    phone_exist = get_account(session, singin_data)
    if not phone_exist:
        a = 1


async def get_current_user(user: UserID = Depends()):
    user_cookie = Cookie(alias=COOKIE_SESSION_ID)
    if user_cookie:
        if get_user_cookie(user_cookie):
            return

