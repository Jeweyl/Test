from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import URL
from sqlalchemy.ext.declarative import declarative_base

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

SessionLocal = async_sessionmaker(
    class_= AsyncSession, 
    bind= engine,
    expire_on_commit=False, 
)

Base = declarative_base()
