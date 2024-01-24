from fastapi import APIRouter
from account.views import router as account_router

from api_v1.views import router as api_v1_router


router = APIRouter(prefix="")

router.include_router(api_v1_router, tags=['api_v1_router'])



@router.get("/")  # страница для отправки сообщения и регистрации 
async def create_user(token: str | None = None, cookie: str | None = None, username=None):
    '''
        возвращает all chats user order_by(created_at) 
         all message chats order_by(created_at) если есть:
            1. Bearer token -> account with DB, а иначе
            2. user в DB с таким cookie, а иначе
            3. create cookie and create new User and redirect 
            4. для отправки сообщения просит ввести имя 
    '''
    pass


@router.post("/")
async def set_message(user, message):
    '''
        используется есть отправляется сообщение в чат от пользователя
        возвращает страницу (1. пердидущие сообщения последних чатов и их статус  2. Список чатов  3. Список Врачей из Чатов 4. form message)
        если:
            1. User:username not null
            2. exist current chat if not create new chat
    '''
    pass