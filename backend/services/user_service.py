from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from redis import Redis

import json

from security import hash_password, verify_password, create_access_token
from schemas.user_schemas import UserResponse, UserRegistration, UserLogin, UserLoginResponse
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, db:AsyncSession, redis:Redis):
        self.user = UserRepository(db)
        self.db = db
        self.redis = redis
    
    async def get_all_user(self) -> list[UserResponse]:
        cache_key = "get_all_users"
        cached = await self.redis.get(cache_key)
        if cached is not None:
            return [UserResponse.model_validate(user) for user in json.loads(cached)]
        response = await self.user.get_all_users()
        users = [UserResponse.model_validate(user) for user in response]
        json_data = json.dumps(
            [user.model_dump() for user in users]
            )
        await self.redis.set(cache_key, json_data, ex=300)
        return users
    
    async def get_user_by_id(self, id:int) -> UserResponse | None:
        cache_key = f"get_user_{id}"
        cached = await self.redis.get(cache_key)
        if cached is not None:
            return UserResponse.model_validate_json(cached)
        response = await self.user.get_user_by_id(id=id)
        if response is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        user = UserResponse.model_validate(response)
        await self.redis.set(cache_key, user.model_dump_json(), ex=300)
        return user
    
    async def get_user_by_username(self, username:str) -> UserResponse | None:
        cache_key = f"get_user_{username}"
        cached = await self.redis.get(cache_key)
        if cached is not None:
            return UserResponse.model_validate_json(cached)
        response = await self.user.get_user_by_username(username=username)
        if response is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        user = UserResponse.model_validate(response)
        await self.redis.set(cache_key, user.model_dump_json(), ex=300)
        return user
    
    async def create_new_user(self, data:UserRegistration) -> UserResponse | None:
        async with self.db.begin():
            if await self.user.get_user_by_username(username=data.username) is not None:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with that username alredy exist")
            data.password = hash_password(data.password)
            new_user = await self.user.user_register(data=data)
        user = UserResponse.model_validate(new_user)
        await self.redis.delete("get_all_users")
        return user
            
    async def user_login(self, data:UserLogin) -> UserLoginResponse:
        user_dict = await self.user.get_user_by_username(data.username)
        if user_dict is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        if not verify_password(data.password, user_dict.hashable_password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        token = create_access_token(user_dict.id)
        return {"access_token": token, "token_type": "bearer"}
        
        
        
        