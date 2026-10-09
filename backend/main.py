from fastapi import FastAPI, Request

from routers.product_router import router as product_router
from routers.category_router import router as category_router
from routers.order_router import router as order_router

from lifespan import lifespan



app = FastAPI(lifespan=lifespan)

app.include_router(product_router)
app.include_router(category_router)
app.include_router(order_router)

@app.get("/redis")
async def redis(request: Request):
    request = request.app.state.redis
    
    await request.set("test_key", "Hello Redis")
    value = await request.get("test_key")
    
    return {"value":value}