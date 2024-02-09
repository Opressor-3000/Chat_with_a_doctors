from fastapi import APIRouter


router = APIRouter(prefix="/doctor", tags=['Doctor'])
'''
    router for doctors 
'''

@router.get('/{doctor_id}/')
async def get_doctor(doctor_id):
    '''
        return doctor profile if it exist (check account)
    '''
    pass


@router.get('/{doctor_id}/feedbacks/')
async def get_feedbacks():
    '''
        return all doctor feedbacks 
    '''
    pass


@router.get('/{doctor_id}/{feedback}/')
async def get_feedback():
    pass


@router.get('/{chat_id}/')
async def get_doctor_chat():
    '''
        return all doctor feedbacks 
    '''
    pass


@router.get('/{feedback_id}/')
async def get_feedback(feedback_id):
    '''
        return doctor feedback if they is exist
    '''
    pass


@router.get('/{doctor_id}/chat_list/')
async def get_doctor_chat_list():
    '''
        return one current (active) chats doctors 
            показывать в каких чатах user online
    '''
    pass


@router.get('/{doctor_id}/current_chat_list/')
async def get_doctor_current_chat_list():
    '''
        return all current (active) chats doctors 
            показывать в каких чатах user online
    '''
    pass


@router.get('/{doctor_id}/{active_chat_id}/')
async def get_current_chat(chat_id):
    pass



@router.post('/{doctor_id}/{active_chat_id}/')
async def send_message(chat_id):
    pass



@router.get('/{user_id}/')
async def get_user_chats():
    '''
        return user (username, chats, diagnosis, anamnesis, )
    '''
    pass


