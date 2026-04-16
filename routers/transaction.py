from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models, Schemas
from db import get_db
from datetime import date

router = APIRouter(prefix="/transactions")

@router.post("/", response_model=Schemas.TransactionResponse)
def create_transaction(txn: Schemas.TransactionCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == txn.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Invalid category")

    if txn.date > date.today():
        raise HTTPException(status_code=400, detail="Date cannot be future")

    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn


@router.get("/", response_model=list[Schemas.TransactionResponse])
def get_transactions(
    type: str = None,
    category_id: int = None,
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)
    if category_id:
        query = query.filter(models.Transaction.category_id == category_id)
    if start_date:
        query = query.filter(models.Transaction.date >= start_date)
    if end_date:
        query = query.filter(models.Transaction.date <= end_date)

    return query.all()


@router.get("/{id}", response_model=Schemas.TransactionResponse)
def get_transaction(id: int, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not txn:
        raise HTTPException(status_code=404)
    return txn


@router.put("/{id}")
def update_transaction(id: int, data: Schemas.TransactionCreate, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not txn:
        raise HTTPException(status_code=404)

    for key, value in data.dict().items():
        setattr(txn, key, value)

    db.commit()
    return txn


@router.delete("/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not txn:
        raise HTTPException(status_code=404)

    db.delete(txn)
    db.commit()
    return {"message": "Deleted"}