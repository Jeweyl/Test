from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import SessionLocal
from models.product import Product
from schemas.product_schema import ProductCreate, ProductResponse

async def get_session():
    async with SessionLocal() as session:
        yield session

app = FastAPI()

@app.get("/")
async def root(session: AsyncSession = Depends(get_session)):
    return {"message": "Hello!"}

@app.get("/product/all")
async def get_all_product(session:AsyncSession = Depends(get_session)):
    response_product = select(Product)
    result = await session.execute(response_product)
    products = result.scalars().all()
    return products

@app.get("/product/{id}")
async def get_product(session:AsyncSession = Depends(get_session), id:int=id) -> ProductResponse:
    stmt = select(Product).where(Product.id == id)
    result = await session.execute(stmt)
    product = result.scalar_one_or_none()
    return product

@app.post("/add_product")
async def add_product(data:ProductCreate, session:AsyncSession = Depends(get_session)) -> ProductResponse:
    product = Product(
        name = data.name, 
        description = data.description,
        price = data.price
    )
    session.add(product)
    await session.commit()
    return product
