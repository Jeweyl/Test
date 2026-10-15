import pytest_asyncio
from uuid import uuid4
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from redis_client import redis_client
from schemas.user_schemas import UserRegistration
from services.user_service import UserService
from tests.test_db import SessionLocal


@pytest_asyncio.fixture
async def session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


@pytest_asyncio.fixture
async def user(session: AsyncSession):
    username = f"test_{uuid4().hex}"

    data = UserRegistration(
        username=username,
        password="12345678",
    )

    service = UserService(session, redis_client)

    created_user = await service.create_new_user(data)

    try:
        yield created_user
    finally:
        await session.execute(
            delete(User).where(User.id == created_user.id)
        )
        await session.commit()