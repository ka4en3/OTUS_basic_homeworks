from fastapi import FastAPI
from routers.api_router import router as api_router

app = FastAPI(title="Basic FastAPI app for Docker")
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
