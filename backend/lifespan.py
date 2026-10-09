from contextlib import asynccontextmanager
from fastapi import FastAPI

from redis_client import redis_client

@asynccontextmanager
async def lifespan(app:FastAPI):
    app.state.redis = redis_client
    yield
    await redis_client.aclose()