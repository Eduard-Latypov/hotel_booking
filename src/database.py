import os
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

from config import settings

# env_path = Path(__file__).parent.parent / ".env"
#
#
# load_dotenv(env_path)
# DB_PORT = os.getenv("DB_PORT")
# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
#
#
# DATABASE_ASYNC_URL = (
#     f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

async_engine = create_async_engine(settings.DATABASE_URL)


async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
