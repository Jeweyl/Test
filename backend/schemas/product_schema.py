from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict

class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=255, description="name of product")
    price: Decimal = Field(description="Price of product")
    description: str | None = None
    category_id: int | None = None
    
    
class ProductCreate(ProductBase):
    pass
class ProductResponse(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
    

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(description="total number of product")