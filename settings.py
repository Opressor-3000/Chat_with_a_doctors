from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
   "REAL_DATABASE_URL",
   default="postgres+asyncpg://postgres:postgres@0.0.0.0:5432/btk"
) 