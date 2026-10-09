from fastapi import Request
from redis.asyncio import Redis

import os




redis_client = Redis.from_url(
    os.getenv("REDIS_URL", "redis://redis:6379/0"),
    decode_responses = True
)

async def get_redis(reqiest: Request) -> Redis:
    return reqiest.app.state.redis