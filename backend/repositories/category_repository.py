from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.category import Category
from schemas.category_schemas import CategoryCreate

class CategoryRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
        
    async def get_all_category(self)-> list[Category]:
        request = select(Category)
        result = await self.db.execute(request)
        categories = result.scalars().all()
        return categories
    
    async def get_category_by_id(self, id:int)-> Category | None:
        request = select(Category).where(Category.id == id)
        result = await self.db.execute(request)
        category = result.scalar_one_or_none()
        return category
    
    async def create_new_category(self, data:CategoryCreate)->Category:
        new_category = Category(
            name=data.name, 
            description=data.description,
        )
        self.db.add(new_category)
        await self.db.commit()
        return new_category
        
        