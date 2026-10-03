from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import make_url
from sqlalchemy.orm import sessionmaker
import os


db_url = make_url(
    os.getenv()
)

engine = create_async_engine(
    url = db_url
)