
from fastapi import Request, status, Cookie
from fastapi.responses import RedirectResponse
from core.models import db_connect

from sqlalchemy import select
from fastapi import Cookie
from core.models.db_connector import db_connect
from account.models import User
from main import app
from auth.utils import COOKIE_SESSION_ID


async def get_user_cookie(
        session = db_connect.get_scope_session, 
        user_cookie: str = Cookie(alias=COOKIE_SESSION_ID),
        ) -> User | None:
    stmt = select(User).filter_by(cookie = user_cookie)
    return await session.execute(stmt)



# @app.middleware("http")
# async def check_cookie(request: Request, call_next):
#     response = await call_next(request)
#     user_cookie = Cookie(alias=COOKIE_SESSION_ID)
#     if user_cookie:
#         if get_user_cookie(user_cookie):
#             return response
#     return RedirectResponse(url='/auth/add_cookie/', status_code=status.HTTP_401_UNAUTHORIZED,)