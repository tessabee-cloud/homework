from pydantic import BaseModel,ConfigDict

from datetime import datetime



class UserCreate(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


class UserRead(BaseModel):
    id: int
    name: str
    email: str

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


#category


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str


class CategoryRead(BaseModel):
    id: int
    name: str

    model_config = ConfigDict( from_attributes = True)


#subcategory

class SubCategoryCreate(BaseModel):
    name: str
    category_id: int


class SubCategoryUpdate(BaseModel):
    name: str
    category_id: int


class SubCategoryRead(BaseModel):
    id: int
    name: str
    category_id: int

    model_config = ConfigDict( from_attributes = True)


#order

class OrderCreate(BaseModel):
    user_id: int


class OrderUpdate(BaseModel):
    user_id: int


class OrderRead(BaseModel):
    id: int
    user_id: int
    order_date: datetime

    model_config = ConfigDict( from_attributes = True)

#order_item


class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItemUpdate(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItemRead(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    model_config = ConfigDict( from_attributes = True)


