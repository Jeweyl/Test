from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from fastapi import HTTPException, status

from models.product import Product
from schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
    
    async def get_all_product(self) -> list[Product]:
        request = select(Product)
        result = await self.db.execute(request)
        products = result.scalars().all()
        return products
    
    async def get_by_id(self, id:int=None)->Product|None:
        request = select(Product).where(Product.id == id)
        result = await self.db.execute(request)
        product = result.scalar_one_or_none()
        return product
    
    async def get_by_category(self, category_id:int=None)->list[Product]:
        request = select(Product).where(Product.category_id == category_id)
        result = await self.db.execute(request)
        products = result.scalars().all()
        return products
    
    async def create_product(self, data:ProductCreate)->Product:
        data = Product(
            name=data.name,
            description=data.description,
            price=data.price,
            category_id = data.category_id,
            )
        self.db.add(data)
        await self.db.commit()
        return data