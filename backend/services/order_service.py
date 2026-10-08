from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from models.order import OrderItem, Order
from schemas.order_schemas import OrderItemCreate, OrderItemResponse, OrderCreate, OrderResponse, OrderListResponse
from schemas.product_schema import ProductListResponse
from repositories.order_respository import OrderRepository
from repositories.product_repository import ProductRepository

class OrderService:
    def __init__(self, db:AsyncSession):
        self.order = OrderRepository(db)
        self.product = ProductRepository(db)
            
    async def get_all_orders(self) ->OrderListResponse:
        result = await self.order.get_all_orders()
        return result
    
    async def get_order_by_id(self, id:int) -> OrderResponse | None:
        result = await self.order.get_orders_by_id(id=id)
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return result
    
    async def create_new_order(self, order_items:list[OrderItemCreate], user_id:int = 1) -> OrderResponse:
        async def create_new_order_item(order_item:OrderItemCreate, products:ProductListResponse) -> OrderItem:
            if products.count < order_item.count:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
            new_order_item = OrderItem(
                product_id = order_item.product_id,
                count = order_item.count,
                price = products[order_item.product_id].price
            )
            return new_order_item
        
        products_ids = [order_item.product_id for order_item in order_items]
        products = await self.product.get_by_ids(products_ids)
        
        new_order_items = [await create_new_order_item(order_item=order_item, products=products) for order_item in order_items]
        
        new_order = await self.order.create_order(user_id=user_id, order_items=new_order_items)
        return new_order
        
        
        
        