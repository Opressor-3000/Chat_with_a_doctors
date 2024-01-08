from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import REAL_DATABASE_URL
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
import uvicorn

from core.models.base import db_connect
engine = create_async_engine(REAL_DATABASE_URL, future=True, echo=True)


async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


@asynccontextmanager
async def lifespan(app: FastAPI):
   async with db_connect.engine.begin() as connection:
      await connection.run_sync(Base.metadata.create_all)
   yield


app = FastAPI()

if __name__ == "__main__":
   uvicorn.run("main:app", reload=True)

   