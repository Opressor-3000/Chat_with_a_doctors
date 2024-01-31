from fastapi import APIRouter


router = APIRouter(prefix="/chat", tags=["Chats"])

'''
    router for user chats
'''


@router.get('/')
async def get_user_chats():
    '''
        Вернуть all chats user  if:
            1. user is exist 
                filters (rating, doctors)
                sort (rating, datetime)
    '''
    pass


@router.post('/{chat_id}/')
async def get_current_chat(chat_id):
    '''
        return current chat user if:
            1. if user chat exist
    '''
    return await chat_id


@router.get('/doctors/')
async def get_doctors(user):
    '''
        return all chat doctor  and count chat with doctor
    '''
    pass


@router.get('/{doctor_id}/')
async def get_doctor(doctor_id):
    pass





