from typing import TYPE_CHECKING, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


if TYPE_CHECKING:
    from account.schemes import AccountID
    from doctors.schemes import FeedbackID

from doctors.models import Feedback
from account.crud import get_account_feedback, get_account_feedbacks
from auth.utils import get_current_user
from core.models import db_connect

router = APIRouter(prefix="/doctor", tags=["Doctor"])


################    FEEDBACK    ###############


@router.get("/{feedback}/")
async def get_feedback(feedback: FeedbackID = Depends(get_account_feedback)) -> Feedback:
    return {'feedback':feedback}


##################    CHAT    ###################


@router.get("/{chat_id}/")
async def get_chat(
    session: AsyncSession = Depends(db_connect.scope_session_dependency),
    account: AccountID = Depends(get_current_user),
):
    """
    return chat
    """
    


@router.get("/current_chat_list/")
async def get_current_chat_list():
    """
    return all current (active) chats doctors
        показывать в каких чатах user online
    """
    pass


@router.get("/{doctor_id}/chat_list/")
async def get_all_chat_list():
    """
    return one current (active) chats doctors
        показывать в каких чатах user online
    """
    pass


#####################     USER      #####################


@router.get("/{user_id}/")
async def get_user_from_chat():
    """
    return user (username, chats, diagnosis, anamnesis, )
    """
    pass


####################     MESSAGE     ######################


@router.post("/{doctor_id}/{active_chat_id}/")
async def doctor_post_message_to_chat(chat_id):
    """
    chat is active True
    chat doctor = account.doctor
    text > 0

    """
    pass
