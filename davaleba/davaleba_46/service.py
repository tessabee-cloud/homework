from sqlalchemy.orm import Session

from models import User, UserRole
import repository
from schemas import RegisterRequest, LoginRequest
from security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register(
        session: Session,
        data: RegisterRequest
    ):
        existing_user = repository.get_user_by_email(
            session,
            data.email
        )

        if existing_user:
            raise ValueError(
                "User with this email already exists"
            )

        hashed_password = hash_password(
            data.password
        )

        user = User(
            name=data.name,
            email=data.email,
            hashed_password=hashed_password,
            is_active=True,
            role=UserRole.CUSTOMER
        )

        return repository.create_user(
            session,
            user
        )


    @staticmethod
    def login(
        session: Session,
        data: LoginRequest
    ):
        user = repository.get_user_by_email(
            session,
            data.email
        )

        if user is None:
            raise ValueError(
                "Invalid email or password"
            )

        if not verify_password(
            data.password,
            user.hashed_password
        ):
            raise ValueError(
                "Invalid email or password"
            )

        if not user.is_active:
            raise ValueError(
                "User is inactive"
            )

        token = create_access_token(
            user.id
        )

        return token