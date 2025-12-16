from fastapi import FastAPI
from app.database import init_db
from app.routes import router
app = FastAPI(title="Student API")
@app.on_event("startup")
def startup():
    init_db()
app.include_router(router)
@app.get("/")
def root():
    return {"message": "Hello, Uzair! FastAPI is working 🎉"}