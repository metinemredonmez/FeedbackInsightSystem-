from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Flight Experience Intelligence System (FEIS)")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "API is up and running!"}
