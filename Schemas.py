from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from models import TransactionType

class CategoryBase(BaseModel):
    name: str
    type: TransactionType

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    class Config:
       from_attributes=True

class TransactionBase(BaseModel):
    title: str
    amount: float = Field(gt=0)
    type: TransactionType
    category_id: int
    date: date
    note: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True