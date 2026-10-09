from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from redis.asyncio import Redis

from repositories.product_repository import ProductRepository
from schemas.product_schema import ProductResponse, ProductListResponse, ProductCreate
from models.product import Product

class ProductService:
    def __init__(self, db:AsyncSession, redis:Redis):
        self.product = ProductRepository(db)
        self.redis = redis
    
    async def get_all(self) -> ProductListResponse:
        cache_key = "product:all"
        
        cached = await self.redis.get(cache_key)
        if cached is not None:
            print("CACHE HIT")
            return ProductListResponse.model_validate_json(cached)
        
        print("CACHE MISS")
        
        products = await self.product.get_all_product()
        
        result = [ProductResponse.model_validate(product) for product in products]
        
        response = ProductListResponse(products=result, total = len(result))
        
        await self.redis.set(cache_key, response.model_dump_json(), ex=60)
        
        return response 
            
    async def get_by_id(self, id:int)->ProductResponse | None:
       result = await self.product.get_by_id(id)
       if result is None:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
       return ProductResponse.model_validate(result)
   
    async def create_new(self, data:ProductCreate) -> ProductResponse:
        cache_key = "product:all"
        
        result = await self.product.create_product(data=data)
        response = ProductResponse.model_validate(result)
        await self.redis.delete(cache_key)
        print("CACHE DELETE")
        return response
   
   