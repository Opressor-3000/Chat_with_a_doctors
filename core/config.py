from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os 

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PASS = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_NAME")
DB_POST = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_PASS")

BASE_DIR = Path(__file__).parent

class DBSettings(BaseModel):
   db_url: str = "postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s?async_fallback=True"
   db_echo: bool = False

#postgres+asyncpg://user:pass@localhost:5432/foobar

class Settings(BaseSettings):
   api_v1_prefix:str = "/api/v1/"
   db: DBSettings = DBSettings()


settings = Settings()
