from fastapi import APIRouter

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


@router.put('/edit/{uuid}/')  # after click edit account 
async def update_account():
    '''
        возвращает форму с заполненными полями для редактирования если:
            1. Account 
            
    '''
    pass 


@router.get('/my_doctors/')
async def get_doctors():
    '''
        return doctor with which chats 
            1. count chats with doctors
    '''
    pass


@router.post('/support')
async def create_issue():
    pass