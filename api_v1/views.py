from fastapi import FastAPI

from fastapi import APIRouter


from account.views import router as account_router
from chat.views import router as chat_router
from doctors.views import router as doctor_router
from auth.views import router as auth_router


router = APIRouter(prefix='/api/v1', tags=['api_v1'])


router.include_router(auth_router, tags=['Auth'])
router.include_router(account_router, tags=['Account'])
router.include_router(chat_router, tags=['Chat'])