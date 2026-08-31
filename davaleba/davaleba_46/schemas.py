
from pydantic import BaseModel,ConfigDict

from models import UserRole

from datetime import datetime

#auth




class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


#user

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    role: UserRole

    model_config = ConfigDict( from_attributes = True)

#product

class ProductCreate(BaseModel):
    name: str
    price: int
    category_id: int
    subcategory_id: int | None = None


class ProductUpdate(BaseModel):
    name: str
    price: int
    category_id: int
    subcategory_id: int | None = None


class ProductRead(BaseModel):
    id: int
    name: str
    price: int
    category_id: int
    subcategory_id: int | None

    model_config = ConfigDict( from_attributes = True)

#orders

class OrderCreate(BaseModel):
    user_id: int


class OrderUpdate(BaseModel):
    user_id: int


class OrderRead(BaseModel):
    id: int
    user_id: int
    order_date: datetime

    class Config:
        from_attributes = True