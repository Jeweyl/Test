from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


#OrderItem
class OrderItemBase(BaseModel):
    product_id: int
    count: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    product_id: int
    count: int
    price: Decimal
    



#Order
class OrderBase(BaseModel):
    user_id: int
    order_items: list[OrderItemCreate]
    
class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    create_at: datetime
    
class OrderListResponse(BaseModel):
    orders: list[OrderResponse]