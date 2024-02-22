from fastapi import APIRouter


router = APIRouter(prefix="/doctor", tags=['Doctor'])
'''
    router for doctors 

    #########     DOCTOR      #########

'''

#    FEEDBACK

@router.get('/{uuid}/feedbacks/')
async def get_feedback_list():
    '''
        return all doctor feedbacks 
            1. feedback chat speciality title
            2. feedback chat created_at
    '''
    pass


@router.get('/{feedback_id}/')
async def get_feedback(feedback_id):
    '''
        return doctor feedback if they is exist
    '''
    pass


#   CHAT


@router.get('/{chat_id}/')
async def get_chat():
    '''
        return chat
    '''
    pass


@router.get('/current_chat_list/')
async def get_current_chat_list():
    '''
        return all current (active) chats doctors 
            показывать в каких чатах user online
    '''
    pass


@router.get('/{doctor_id}/chat_list/')
async def get_all_chat_list():
    '''
        return one current (active) chats doctors 
            показывать в каких чатах user online
    '''
    pass



#   USER


@router.get('/{user_id}/')
async def get_user_from_chat():
    '''
        return user (username, chats, diagnosis, anamnesis, )
    '''
    pass


#     MESSAGE



@router.post('/{doctor_id}/{active_chat_id}/')
async def doctor_post_message_to_chat(chat_id):
    '''
        chat is active True
        chat doctor = account.doctor
        text > 0

    '''
    pass


