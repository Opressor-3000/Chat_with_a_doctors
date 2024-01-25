from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.models.db_connector import db_connect
from .schemes import UserId
from .models import User



async def get_user(session: AsyncSession, user_id: int) -> User | None:
    
    return await session.get(User, user_id)

