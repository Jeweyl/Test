from pydantic import Field, BaseModel

class UserBase(BaseModel):
    username:str = Field(min_length=3, max_length=100)

class UserRegistration(UserBase):
    password:str = Field(min_length=8, max_length=128)
    
class UserLogin(UserBase):
    password:str
class UserResponse(UserBase):
    id:int
    
    model_config = {"from_attributes": True}
    
class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")
    