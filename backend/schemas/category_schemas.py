from pydantic import Field, BaseModel

class CategoryBase(BaseModel):
    name:str
    description: str | None = None
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    
    