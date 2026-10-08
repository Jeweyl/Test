from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from models.category import Category
from repositories.category_repository import CategoryRepository
from schemas.category_schemas import CategoryCreate, CategoryResponse, CategoryListResponse

class CategoryService:
    def __init__(self, db:AsyncSession):
        self.category_repository = CategoryRepository(db)
    
    async def get_all_category(self) -> CategoryListResponse:
        categories = await self.category_repository.get_all_category()
        result = [CategoryResponse.model_validate(category) for category in categories]
        return CategoryListResponse(categories=result, total_count=len(result))
    
    async def get_category_by_id(self, id:int)->CategoryResponse | None:
        category = await self.category_repository.get_category_by_id(id=id)
        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found category with that id")
        return CategoryResponse.model_validate(category)
    
    async def create_new_category(self, data:CategoryCreate)->CategoryResponse:
        new_category = await self.category_repository.create_new_category(
            data=data
        )
        return CategoryResponse.model_validate(new_category)