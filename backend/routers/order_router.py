from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from services.order_service import OrderService
from schemas.order_schemas import OrderListResponse, OrderCreate, OrderResponse
from database import get_session

router = APIRouter(
    prefix="/order"
)

@router.post("/create_new", response_model=OrderResponse)
async def create_new_order(data_new_order: OrderCreate, session:AsyncSession = Depends(get_session)):
    service = OrderService(session)
    new_order = await service.create_new_order(order_items=data_new_order.order_items, user_id=data_new_order.user_id)
    return new_order

@router.get("/all", response_model=OrderListResponse)
async def get_all_orders(session:AsyncSession=Depends(get_session)):
    service = OrderService(session)
    return await service.get_all_orders()