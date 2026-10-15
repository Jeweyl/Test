import pytest

from services.user_service import UserService
from redis_client import redis_client


@pytest.mark.asyncio
async def test_create_user(user):
    assert user.username.startswith("test_")

    
@pytest.mark.asyncio
async def test_get_user_by_username(session, user):
    service = UserService(session, redis_client)

    result = await service.get_user_by_username(user.username)

    assert result is not None
    assert result.username == user.username