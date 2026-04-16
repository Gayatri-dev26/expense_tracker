from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, Schemas
from db import get_db

router = APIRouter(prefix="/categories")

@router.post("/", response_model=Schemas.CategoryResponse)
def create_category(category: Schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=list[Schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

@router.get("/{id}", response_model=Schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{id}")
def update_category(id: int, data: Schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404)
    
    for key, value in data.dict().items():
        setattr(category, key, value)

    db.commit()
    return category

@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404)

    db.delete(category)
    db.commit()
    return {"message": "Deleted"}