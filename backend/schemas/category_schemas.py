from pydantic import Field, BaseModel, ConfigDict

class CategoryBase(BaseModel):
    name:str
    description: str | None = None
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
    
class CategoryListResponse(BaseModel):
    categories: list[CategoryResponse]
    total_count: int

    
    