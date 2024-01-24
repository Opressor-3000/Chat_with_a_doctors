from fastapi import APIRouter


router = APIRouter(prefix='adminpanel', tags=['Admin_Panel'])


@router.get('/')
async def get_panel():
    pass