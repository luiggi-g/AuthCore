from pydantic import BaseModel,EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8,max_length=70)

class UserLoggin(BaseModel):
    email: EmailStr
    password: str
    
class RefreshTokenRequest(BaseModel):
    refresh_token: str