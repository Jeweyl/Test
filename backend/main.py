from fastapi import FastAPI, Request

from routers.product_router import router as product_router
from routers.category_router import router as category_router
from routers.order_router import router as order_router
from routers.user_router import router as user_router

from lifespan import lifespan



app = FastAPI(lifespan=lifespan)

app.include_router(product_router)
app.include_router(category_router)
app.include_router(order_router)
app.include_router(user_router)
