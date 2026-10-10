from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.user import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def get_all_users(self) -> list[User]:
        request = select(User)    
        result = await self.db.execute(request)
        users = result.scalars().all()
        return users
        
    async def get_user_by_id(self, id:int) -> User | None:
        request = select(User).where(User.id == id)
        result = await self.db.execute(request)
        user = result.scalar_one_or_none()
        return user
    
    async def get_user_by_username(self, username:str) -> User | None:
        request = select(User).where(User.username == username)
        result = await self.db.execute(request)
        user = result.scalar_one_or_none()
        return user
    
    async def user_register(self, data:dict) -> User:
        new_user = User(
            username = data.username,
            password = data.hashable_password
        )
        self.db.add(new_user)
        self.db.flush()
        return new_user
    