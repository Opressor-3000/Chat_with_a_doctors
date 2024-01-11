from fastapi import APIRouter
from account.views import router as account_router

from api_v1.views import router as api_v1_router


router = APIRouter(prefix="")

router.include_router(api_v1_router, tags=['api_v1_router'])






