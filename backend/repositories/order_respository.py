from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.order import OrderItem, Order

class OrderRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
        
    async def get_all_orders(self) -> list[Order]:
        request = select(Order)
        result = await self.db.execute(request)
        orders = result.scalars().all()
        return orders
    
    async def get_orders_by_id(self, id:int) -> Order|None:
        request = select(Order).where(Order.id == id)
        result = await self.db.execute(request)
        order = result.scalar_one_or_none()
        return order
    
    async def create_order(self, order_items:list[OrderItem], user_id:int) -> Order:
        new_order = Order(
            user_id = user_id,
            order_items = order_items   
        )
        self.db.add(new_order)
        return new_order