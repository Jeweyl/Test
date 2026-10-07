from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession 

from services.product_service import ProductService
from schemas.product_schema import ProductListResponse, ProductResponse
from database import get_session

router = APIRouter(
    prefix="/product"
)

@router.get("/all", response_model=ProductListResponse)
async def get_all_product(session:AsyncSession = Depends(get_session)):
    service = ProductService(session)
    return await service.get_all()

@router.get("/{id}", response_model=ProductResponse)
async def get_by_id(id:int, session:AsyncSession = Depends(get_session)):
    service = ProductService(session)
    return await service.get_by_id(id)