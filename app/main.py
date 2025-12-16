from fastapi import FastAPI
from app.database import init_db, get_connection

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "Hello, Uzair! FastAPI is working 🎉"}

@app.post("/students")
def add_student(name: str, marks: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    conn.close()
    return {"status": "student added"}

@app.get("/students")
def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows