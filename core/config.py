from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os 

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")
DB_POST = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


BASE_DIR = Path(__file__).parent

class DBSettings(BaseModel):
   url: str = "postgresql+asyncpg://yusif:BTKChat@localhost:5433/btk_db"
   url1: str = "postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:5433/%(DB_NAME)s?async_fallback=True"

   echo: bool = False


class Settings(BaseSettings):
   api_v1_prefix:str = "/api/v1"
   db: DBSettings = DBSettings()
   class Config:
      env_file = "../env"




settings = Settings()
