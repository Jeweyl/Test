from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession 
from redis.asyncio import Redis

from services.product_service import ProductService
from schemas.product_schema import ProductUpdate, ProductListResponse, ProductResponse, ProductCreate
from database import get_session
from redis_client import get_redis

router = APIRouter(
    prefix="/product"
)

@router.get("/all", response_model=ProductListResponse)
async def get_all_product(session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = ProductService(session, redis)
    return await service.get_all()

@router.get("/{id}", response_model=ProductResponse)
async def get_by_id(id:int, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = ProductService(session, redis)
    return await service.get_by_id(id)

@router.post("/create_new", response_model=ProductResponse)
async def create_new_product(data_new_product:ProductCreate, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = ProductService(session, redis)
    return await service.create_new(data=data_new_product)

@router.put("/update/{id}", response_model=ProductResponse)
async def update_product(id:int, data_update_product:ProductUpdate, session:AsyncSession = Depends(get_session), redis:Redis = Depends(get_redis)):
    service = ProductService(session, redis)
    return await service.update_product(id=id, data=data_update_product)