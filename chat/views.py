from typing import List

from core.models.db_connector import db_connect
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.chat import UserChatMessageDoctor
from account.schemes import User
from auth.utils import get_current_user


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


@router.post("/", response_model=List[UserChatMessageDoctor])
async def set_all_chat_message_list(
    session: AsyncSession = Depends(db_connect.scope_session_dependency),
    user_id: User = Depends(get_current_user)
):
    """
        return история messages
    """
    return [message from ]


@router.get("/doctors/")
async def get_doctors(user):
    """
        return all chat doctor and count chat with doctor
    """
    pass


@router.get("/{doctor_id}/")
async def get_doctor(doctor_id):
    pass



