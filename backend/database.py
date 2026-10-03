from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

from config import settings


db_url = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.username,
    password=settings.password,
    host=settings.host,
    port=settings.port,
    database=settings.database
)

engine = create_async_engine(
    url = db_url
)