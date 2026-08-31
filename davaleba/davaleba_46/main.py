from fastapi import FastAPI

from routers import router as auth_router
from routers import router as user_router
from routers import router as product_router
from routers import router as category_router
from routers import router as subcategory_router
from routers import router as order_router
from routers import router as order_item_router


app = FastAPI(
    title="E-Commerce API"
)


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(order_router)
app.include_router(order_item_router)


#davaleba_47

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from middleware import CorrelationIDMiddleware


app = FastAPI(
    title="E-Commerce API"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GZip
app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)


# Correlation ID
app.add_middleware(
    CorrelationIDMiddleware
)


# Routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(order_router)
app.include_router(order_item_router)
