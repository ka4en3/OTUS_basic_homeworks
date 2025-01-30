from fastapi import FastAPI
from src.routers.api_router import router as api_router

app = FastAPI(title="Basic FastAPI app for Docker")
app.include_router(api_router)