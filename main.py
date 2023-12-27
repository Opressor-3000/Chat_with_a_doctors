from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import REAL_DATABASE_URL
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
import uvicorn


engine = create_async_engine(REAL_DATABASE_URL, future=True, echo=True)


async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


app = FastAPI()

if __name__ == "__main__":
   uvicorn.run("main:app", reload=True)

   