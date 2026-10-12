from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from redis import Redis

from database import get_session
from redis_client import get_redis
from services.user_service import UserService
from schemas.user_schemas import UserResponse, UserRegistration
from dependency.auth import get_current_user

router = APIRouter(
    prefix="/user"
)

@router.get("/get_all", response_model=list[UserResponse])
async def get_all_users(session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = UserService(session, redis)
    result = await service.get_all_user()
    return result

@router.get("/get_by_id/{id}", response_model=UserResponse)
async def get_user_by_id(id:int, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = UserService(session, redis)
    result = await service.get_user_by_id(id)
    return result

@router.get("/get_by_username/{username}", response_model=UserResponse)
async def get_user_by_username(username:str, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = UserService(session, redis)
    result = await service.get_user_by_username(username)
    return result

@router.post("/create_user", response_model=UserResponse)
async def create_new_user(data:UserRegistration, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = UserService(session, redis)
    new_user = await service.create_new_user(data)
    return new_user

@router.get("/me", response_model=UserResponse)
async def get_me(current_user = Depends(get_current_user)):
    return current_user
     