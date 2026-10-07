from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.category_service import CategoryService
from schemas.category_schemas import CategoryResponse, CategoryCreate, CategoryListResponse
from database import get_session

router = APIRouter(
    prefix="category"
)

@router.get("/all", response_model=CategoryListResponse)
async def get_all_category(session:AsyncSession = Depends(get_session)):
    service = CategoryService(session)
    categories = service.get_all_category()
    result = [CategoryResponse.model_validate(category) for category in categories]
    return CategoryListResponse(categories=result, total=len(result))

@router.get("/{id}", response_model=CategoryResponse)
async def get_category_by_id(id:int, session:AsyncSession = Depends(get_session)):
    service = CategoryService(session)
    result = service.get_category_by_id(id=id)
    return CategoryResponse.model_validate(result)

@router.post("/create_new", response_model=CategoryResponse)
async def create_new_category(data:CategoryCreate, session:AsyncSession=Depends(get_session)):
    service = CategoryService(session)
    result = service.create_new_category(data)
    return CategoryResponse.model_validate(result)