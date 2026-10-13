from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import URL

from tests.test_config import settings

db_url_test = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.username,
    password=settings.password,
    host=settings.host,
    port=settings.port, 
    database=settings.database
    )

engine = create_async_engine(url=db_url_test)


SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with SessionLocal() as session:
        yield session