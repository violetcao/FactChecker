import sqlite3
from fastapi import FastAPI

conn = sqlite3.connect("claims.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS claims
             (id INTEGER PRIMARY KEY, text TEXT, status TEXT, source TEXT)""")
conn.commit()

# Initialise API
app = FastAPI()


@app.get("/")
def main_page():
    return {"message": "Hello, FastAPI!"}

