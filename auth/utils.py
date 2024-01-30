from datetime import datetime

from jwt import JWT
import bcrypt

jwt = JWT()


from core.config import settings


# def encode_jwt(
#         payload: dict,
#         private_key: str = settings.auth_jwt.private_key_dir.read_text(),
#         algorithm: str = settings.auth_jwt.algorithm,
# ):
#     to_encode = payload.copy()
#     now = datetime.utcnow()
#     if except_deltatime:
#         expire = now + settings.auth_jwt.access_token_expire_minuts
#     else:
#         encoded = jwt.encode(
#             expire = now + timedelta(minutes))
#     encoded = jwt.encode(
#         payload,
#         key,
#         algorithm=algorithm,
#     )


# def decode_jwt(
#         token str | bytes,
#         public_key: str = settings.auth_jwt.public_key.read_text(),
#         algorithm: list[str] = [settings.auth_jwt.algorithm],
# ):
#     decoded = jwt.decode(
#         token,
#         public_key,
#         algorithm,
#     )
#     return decoded


def hash_password(
        password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bcrypt: bytes = password.encode()
    return bcrypt.hashpw(pwd_bcrypt, salt)


def validate_password(
        password: str,
        hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)