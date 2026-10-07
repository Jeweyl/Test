from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from routers.product_router import router as product_router

import models



app = FastAPI()

app.include_router(product_router)

@app.get("/")
async def root():
    return {"message": "Hello!"}

