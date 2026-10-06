from decimal import Decimal

from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    description: str
    
class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    description: str
    
    