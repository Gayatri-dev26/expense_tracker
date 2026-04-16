from fastapi import FastAPI
import models
from db import engine
from routers import categories, transaction, summary

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(categories.router)
app.include_router(transaction.router)
app.include_router(summary.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API Running"}