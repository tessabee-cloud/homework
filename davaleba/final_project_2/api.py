from typing import Optional

import jwt

from fastapi import (
    FastAPI,
    HTTPException,
    Depends
)

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)


from sqlalchemy.orm import Session

from database import get_db, Base, engine
from models.db_models import User, Transaction, Budget

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
)

from schemas import UserCreate, UserResponse, Token, LoginRequest

from pydantic import BaseModel

from jwt.exceptions import InvalidTokenError


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Personal Finance Tracker API",
    description="API for managing personal finances",
    version="1.0.0"
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
def root():
    return {
        "message": "Finance Tracker API is running"
    }

@app.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "username": new_user.username
    }
def authenticate_user(
    db: Session,
    username: str,
    password: str
) -> User:
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user or not verify_password(
        password,
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    return user


def issue_token(user: User) -> dict:
    return {
        "access_token": create_access_token(
            user.username,
            user.id
        ),
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }


@app.post("/login", response_model=Token)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        data.username,
        data.password
    )

    return issue_token(user)


@app.post("/token", response_model=Token)
def login_form(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Form-encoded login used by the Swagger "Authorize" button."""
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    return issue_token(user)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        user_id = payload.get("user_id")

        if username is None or user_id is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user = db.query(User).filter(
        User.id == user_id,
        User.username == username
    ).first()

    if user is None:
        raise credentials_exception

    return user


@app.get("/users/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username
    }




class TransactionRequest(BaseModel):
    type: str
    amount: float
    category: str
    date: str
    comment: Optional[str] = ""


class BudgetRequest(BaseModel):
    category: str
    limit: float


@app.post("/transactions")
def create_transaction(
    data: TransactionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if data.type.lower() not in ["income", "expense"]:
        raise HTTPException(
            status_code=400,
            detail="Transaction type must be income or expense"
        )

    if data.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )

    transaction = Transaction(
        type=data.type.lower(),
        amount=data.amount,
        category=data.category,
        date=data.date,
        comment=data.comment or "",
        user_id=current_user.id
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return {
        "id": transaction.id,
        "type": transaction.type,
        "amount": transaction.amount,
        "category": transaction.category,
        "date": transaction.date,
        "comment": transaction.comment,
        "user_id": transaction.user_id
    }

@app.get("/transactions")
def get_transactions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    return [
        {
            "id": transaction.id,
            "type": transaction.type,
            "amount": transaction.amount,
            "category": transaction.category,
            "date": transaction.date,
            "comment": transaction.comment,
            "user_id": transaction.user_id
        }
        for transaction in transactions
    ]

@app.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    if transaction.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You can only delete your own transaction"
        )

    db.delete(transaction)
    db.commit()

    return {
        "message": "Transaction deleted successfully"
    }

@app.post("/budgets")
def create_budget(
    data: BudgetRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if data.limit <= 0:
        raise HTTPException(
            status_code=400,
            detail="Budget limit must be greater than zero"
        )

    budget = Budget(
        category=data.category,
        limit=data.limit,
        user_id=current_user.id
    )

    db.add(budget)
    db.commit()
    db.refresh(budget)

    return {
        "id": budget.id,
        "category": budget.category,
        "limit": budget.limit,
        "user_id": budget.user_id
    }

@app.get("/summary")
def general_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    income = sum(
        t.amount
        for t in transactions
        if t.type == "income"
    )

    expenses = sum(
        t.amount
        for t in transactions
        if t.type == "expense"
    )

    balance = income - expenses

    return {
        "income": income,
        "expenses": expenses,
        "balance": balance
    }


@app.get("/summary/monthly")
def monthly_summary(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if month < 1 or month > 12:
        raise HTTPException(
            status_code=400,
            detail="Month must be between 1 and 12"
        )

    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    monthly_transactions = [
        t for t in transactions
        if t.date.startswith(
            f"{year:04d}-{month:02d}"
        )
    ]

    income = sum(
        t.amount
        for t in monthly_transactions
        if t.type == "income"
    )

    expenses = sum(
        t.amount
        for t in monthly_transactions
        if t.type == "expense"
    )

    balance = income - expenses

    return {
        "year": year,
        "month": month,
        "income": income,
        "expenses": expenses,
        "balance": balance
    }


