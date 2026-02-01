from constants import app
from initialisator.database import init_db, get_db
from initialisator.models import Claims
from sqlalchemy.orm import Session
from fastapi import Depends


# create database
init_db()

@app.get("/")
def main_page():
    return {"message": "Uploaded Successfully!"}

@app.get("/claims")
def read_claims(db: Session = Depends(get_db)):
    return db.query(Claims).all()