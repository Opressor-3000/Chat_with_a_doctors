from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import REAL_DATABASE_URL
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
import uvicorn
from core.models.base import Base

from core.models.db_connector import db_connect, DataBaseConnector
from core.views import router as main_router
from account.views import router as account_router
from chat.views import router as chat_router
from doctors.views import router as doctor_router
from auth.views import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
   async with db_connect.engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
   yield


app = FastAPI(lifespan=lifespan, title="BTK chat")


app.include_router(main_router, tags=["Main"])
app.include_router(auth_router, tags=['Auth'])
app.include_router(account_router, tags=['Account'])
app.include_router(chat_router, tags=['Chat'])


if __name__ == "__main__":
   uvicorn.run("main:app", reload=True)

   