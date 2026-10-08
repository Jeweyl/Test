from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from models.order import OrderItem
from schemas.order_schemas import OrderItemCreate, OrderResponse, OrderListResponse
from repositories.order_respository import OrderRepository
from repositories.product_repository import ProductRepository

class OrderService:
    def __init__(self, db:AsyncSession):
        self.db = db
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
        
        products_ids = [order_item.product_id for order_item in order_items]
        
        new_order_items = []
        
        async with self.db.begin():   

            products = await self.product.get_by_ids(products_ids)

            for order_item in order_items:
                product = products.get(order_item.product_id)

                if product is None:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND
                    )

                if product.count < order_item.count:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN
                    )
                    
                product.count -= order_item.count
                
                raise Exception("BOOM")

                new_order_items.append(
                    OrderItem(
                        product_id=product.id,
                        count=order_item.count,
                        price=product.price
                    )
                )

            new_order = await self.order.create_order(
                user_id=user_id,
                order_items=new_order_items
            )

        return new_order
        
        
        