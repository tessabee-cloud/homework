from fastapi import FastAPI

from router import router as user_router
from router import router as product_router
from router import router as category_router
from router import router as subcategory_router
from router import router as order_router
from router import router as order_item_router


app = FastAPI(
    title="E-Commerce API"
)


app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(order_router)
app.include_router(order_item_router)