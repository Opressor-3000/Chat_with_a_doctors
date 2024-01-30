
from fastapi import Request, Response, status, Cookie
from fastapi.responses import RedirectResponse
from core.models import db_connect

from account.crud import get_user_cookie
from main import app, COOKIE_SESSION_ID


@app.middleware("http")
async def check_cookie(request: Request, call_next):
    response = await call_next(request)
    user_cookie = Cookie(alias=COOKIE_SESSION_ID)
    if user_cookie:
        if get_user_cookie(user_cookie):
            return response
    return RedirectResponse(url='/auth/add_cookie/', status_code=status.HTTP_401_UNAUTHORIZED,)