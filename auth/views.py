from fastapi import APIRouter


router = APIRouter(prefix="/auth", tags=["auth"])


@router.get('/')
async def get_auth():
    pass



@router.post('/')
async def set_auth(phone):
    pass


@router.get('/comfirmation_phone/')
async def get_phone():
    pass



@router.post('/comfirmation_phone/')
async def comfirmation_phone():
    pass