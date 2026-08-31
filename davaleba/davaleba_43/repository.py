from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


def create_user(
    session: Session,
    user: User
):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def get_users(session: Session):
    statement = select(User)

    result = session.execute(statement)

    return result.scalars().all()


def get_user(
    session: Session,
    user_id: int
):
    statement = select(User).where(
        User.id == user_id
    )

    result = session.execute(statement)

    return result.scalar_one_or_none()


def delete_user(
    session: Session,
    user: User
):
    session.delete(user)
    session.commit()