from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import models
from db import get_db

router = APIRouter(prefix="/summary")

@router.get("/")
def get_summary(db: Session = Depends(get_db)):
    income = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "expense").scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }