from fastapi import FastAPI
from app.routers import auth_routher

app= FastAPI()

app.include_router(auth_routher.router)

@app.get("/")
def root():
    return {"message": "AuthCore API running"}

