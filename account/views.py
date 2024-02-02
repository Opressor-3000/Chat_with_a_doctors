from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
# from .schemes.user import UserCreate, UserID

router = APIRouter(prefix="/account", tags=["account"])

'''
    router for user 
'''


@router.post('/registration/')  #
async def create_account(create_account_scheme):
    '''
        возвращает account если есть :
            1. user в БД, иначе создает -> redirect
            2. все поля заполнены правильно 
            3. удачно отправлена смс на телефон
            4. верно указан код из смс
            5. создает account присваивает Bearer token
    '''
    pass


@router.get('/{uuid}/')
async def get_account():
    '''
        return account if is auth
    '''
    pass


@router.get('/{uuid}/users/')
async def get_account():
    '''
        return list user referance account_id 
            divice users , status users, 
    '''
    pass


# @router.patch('/edit/{uuid}/')  # after click edit account 
# async def account_active():
#     '''
#         возвращает форму с заполненными полями для редактирования если:
#             1. Account 
            
#     '''
#     pass 


@router.get('/{uuid}/my_doctors/')
async def get_doctors():
    '''
        return doctor with which chats 
            1. count chats with doctors
    '''
    pass


@router.post('/support/')
async def create_issue():
    pass


@router.get('/{user_id}/')
async def get_user():
    pass


@router.patch('/{uuid}/{feedback_id}/')
async def patch_feedback():
    pass



