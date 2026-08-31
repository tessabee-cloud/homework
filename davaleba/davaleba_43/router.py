from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_session
from schemas import (
    UserCreate,
    UserUpdate,
    UserRead
)
import service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserRead
)
def create_user(
    data: UserCreate,
    session: Session = Depends(get_session)
):
    return service.create_user(
        session,
        data
    )


@router.get(
    "/",
    response_model=list[UserRead]
)
def get_users(
    session: Session = Depends(get_session)
):
    return service.get_users(session)


@router.get(
    "/{user_id}",
    response_model=UserRead
)
def get_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = service.get_user(
        session,
        user_id
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserRead
)
def update_user(
    user_id: int,
    data: UserUpdate,
    session: Session = Depends(get_session)
):
    user = service.update_user(
        session,
        user_id,
        data
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = service.delete_user(
        session,
        user_id
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }