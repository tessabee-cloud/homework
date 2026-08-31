from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_session
from dependencies import get_current_user
from schemas import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)
from schemas import UserRead
from service import AuthService

from models import UserRole

from dependencies import require_role

from schemas import OrderCreate,ProductCreate

#auth

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserRead
)
def register(
    data: RegisterRequest,
    session: Session = Depends(get_session)
):
    try:
        return AuthService.register(
            session,
            data
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: LoginRequest,
    session: Session = Depends(get_session)
):
    try:
        token = AuthService.login(
            session,
            data
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )


@router.get(
    "/me",
    response_model=UserRead
)
def get_me(
    current_user=Depends(get_current_user)
):
    return current_user



#product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


#product

# public

@router.get("/")
def get_products():
    ...

@router.get("/{product_id}")
def get_product(product_id: int):
    ...

# admin

@router.post("/")
def create_product(
    data: ProductCreate,
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...

#orders

#public

@router.get("/")
def get_orders(
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    ...

@router.get("/{order_id}")
def get_order(
    order_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    ...

@router.post("/")
def create_order(
    data: OrderCreate,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user)
):
    ...

# admin

@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...

# users
# admin

@router.get("/")
def get_users(
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...

@router.get("/{user_id}")
def get_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user=Depends(
        require_role(UserRole.ADMIN)
    )
):
    ...