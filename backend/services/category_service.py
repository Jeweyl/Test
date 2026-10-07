from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from models.category import Category
from repositories.category_repository import CategoryRepository
from schemas.category_schemas import CategoryCreate, CategoryResponse, CategoryListResponse

class CategoryService:
    def __init__(self, db:AsyncSession):
        self.category_repository = CategoryRepository(db)
    
    async def get_all_category(self) -> Category:
        categories = self.category_repository.get_all_category()
        result = [CategoryResponse.model_validate(category) for category in categories]
        return CategoryListResponse(categories=result, total_count=len(result))
    
    async def get_category_by_id(self, id:int)->Category | None:
        category = self.category_repository.get_category_by_id(id=id)
        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Now found category with that id")
        return CategoryResponse.model_validate(category)
    
    async def create_new_category(self, data:CategoryCreate)->Category:
        new_category = self.category_repository.create_new_category(
            name = data.name,
            descriptionw = data.description
        )
        return CategoryResponse.model_validate(new_category)