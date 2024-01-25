from fastapi import APIRouter


from account.views import router as account_router
from chat.views import router as chat_router
from doctors.views import router as doctor_router
from auth.views import router as auth_router
from admin.views import router as admin_router


router = APIRouter(prefix='/api/v1', tags=['api_v1'])


router.include_router(auth_router, tags=['Auth'])
router.include_router(account_router, tags=['Account'])
router.include_router(chat_router, tags=['Chat'])
router.include_router(doctor_router, tags=['Doctor'])
router.include_router(admin_router, tags=['Admin'])