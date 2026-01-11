import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


conn = sqlite3.connect("claims.db")
c = conn.cursor()

engine = create_engine("sqlite:///mydb.sqlite", echo=True)
SessionLocal = sessionmaker(bind=engine)