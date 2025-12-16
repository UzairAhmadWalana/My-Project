from fastapi import APIRouter
from app.database import get_connection

router = APIRouter()

@router.post("/students")
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

@router.get("/students")
def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows