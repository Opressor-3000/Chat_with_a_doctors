from contextlib import asynccontextmanager
from fastapi import FastAPI, Cookie
import uvicorn
from typing import Annotated
from uuid import uuid5

from core.models.base import Base
from core.models.db_connector import db_connect, DataBaseConnector
from core.views import router as main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
   async with db_connect.engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)
   yield


app = FastAPI(lifespan=lifespan, title="BTK chat")


app.include_router(main_router, tags=["Main"])


async def session_id_generate() -> str:
   return uuid5().hex


COOKIE_SESSION_ID = 'web_app_hekim_chat_uid'


if __name__ == "__main__":
   uvicorn.run("main:app", reload=True)

   