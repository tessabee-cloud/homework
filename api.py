from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from main import manager
from exceptions import FinanceError


app = FastAPI(
    title="Personal Finance Tracker API",
    description="API for managing personal finances",
    version="1.0.0"
)


class TransactionRequest(BaseModel):
    type: str
    amount: float
    category: str
    date: str
    comment: Optional[str] = ""


class BudgetRequest(BaseModel):
    category: str
    limit: float


@app.get("/transactions")
def get_transactions():
    return [
        transaction.to_dict()
        for transaction in manager.get_transactions()
    ]


@app.post("/transactions")
def create_transaction(data: TransactionRequest):
    try:
        manager.add_transaction(
            data.amount,
            data.type,
            data.category,
            data.date,
            data.comment or ""
        )

        return manager.get_transactions()[-1].to_dict()

    except FinanceError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    try:
        manager.delete_transaction(transaction_id)

        return {
            "message": "Transaction deleted successfully"
        }

    except FinanceError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@app.post("/budgets")
def create_budget(data: BudgetRequest):
    try:
        manager.set_budget(
            data.category,
            data.limit
        )

        return {
            "message": "Budget saved successfully"
        }

    except FinanceError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/summary")
def general_summary():
    income, expenses, balance = manager.calculate_summary()

    return {
        "income": income,
        "expenses": expenses,
        "balance": balance
    }


@app.get("/summary/monthly")
def monthly_summary(year: int, month: int):
    try:
        transactions, income, expenses, balance = manager.monthly_summary(
            year,
            month
        )

        return {
            "year": year,
            "month": month,
            "income": income,
            "expenses": expenses,
            "balance": balance,
            "budget_status": manager.get_budget_status(transactions)
        }

    except FinanceError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )