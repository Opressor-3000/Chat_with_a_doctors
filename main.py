from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import REAL_DATABASE_URL
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
import uvicorn
from core.models.base import Base

from core.models.db_connector import db_connect, DataBaseConnector


@asynccontextmanager
async def lifespan(app: FastAPI):
   async with db_connect.engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
   yield


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
   uvicorn.run("main:app", reload=True)

   