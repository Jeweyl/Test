from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from repositories.product_repository import ProductRepository
from schemas.product_schema import ProductResponse, ProductListResponse, ProductCreate
from models.product import Product

class ProductService:
    def __init__(self, db:AsyncSession):
        self.product = ProductRepository(db)
    
    async def get_all(self) -> ProductListResponse:
        products = await self.product.get_all_product()
        result = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=result, total = len(result))
            
    async def get_by_id(self, id:int)->ProductResponse | None:
       result = await self.product.get_by_id(id)
       if result is None:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
       return ProductResponse.model_validate(result)
   
    async def create_new(self, data:ProductCreate) -> ProductResponse:
        result = await self.product.create_product(data=data)
        return result
   
   