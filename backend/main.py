from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from routers.product_router import router as product_router
from routers.category_router import router as category_router
from routers.order_router import router as order_router

import models



app = FastAPI()

app.include_router(product_router)
app.include_router(category_router)
app.include_router(order_router)
