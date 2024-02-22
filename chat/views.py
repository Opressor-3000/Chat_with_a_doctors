from fastapi import APIRouter


router = APIRouter(prefix="/chat", tags=["Chats"])

"""
    router for user chats
"""


@router.get("/chats/")
async def get_user_chat_list():
    """ 
        return chat_list (date, {speciality}, {doctor})
    """
    return


@router.post("/")
async def set_all_chat_message_list():
    """
        return история messages
    """
    return


@router.get("/doctors/")
async def get_doctors(user):
    """
        return all chat doctor and count chat with doctor
    """
    pass


@router.get("/{doctor_id}/")
async def get_doctor(doctor_id):
    pass


