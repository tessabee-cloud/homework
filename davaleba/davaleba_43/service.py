from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate, UserUpdate
import repository


def create_user(
    session: Session,
    data: UserCreate
):
    user = User(
        name=data.name,
        email=data.email
    )

    return repository.create_user(
        session,
        user
    )


def get_users(session: Session):
    return repository.get_users(session)


def get_user(
    session: Session,
    user_id: int
):
    return repository.get_user(
        session,
        user_id
    )


def update_user(
    session: Session,
    user_id: int,
    data: UserUpdate
):
    user = repository.get_user(
        session,
        user_id
    )

    if user is None:
        return None

    user.name = data.name
    user.email = data.email

    session.commit()
    session.refresh(user)

    return user


def delete_user(
    session: Session,
    user_id: int
):
    user = repository.get_user(
        session,
        user_id
    )

    if user is None:
        return None

    repository.delete_user(
        session,
        user
    )

    return user