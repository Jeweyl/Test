from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal


#OrderItem
class OrderItemBase(BaseModel):
    product_id: int
    count: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    order_id: int
    product_id: int
    count: int
    price: Decimal
    



#Order
class OrderBase(BaseModel):
    user_id: int
    
class OrderCreate(OrderBase):
    order_items: list[OrderItemCreate]

class OrderResponse(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    create_at: datetime
    order_items: list[OrderItemResponse]
    
class OrderListResponse(BaseModel):
    orders: list[OrderResponse]