from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.models.db_connector import db_connect
from chat.models.chat import Chat


async def get_chats(session: AsyncSession):
    stmt = select(Chat, )