from fastapi import FastAPI
from routers.html_router import router as html_router
from routers.api_router import router as api_router

app = FastAPI(title="Basic FastAPI app")
app.include_router(html_router, tags=["HTML"])
app.include_router(api_router, prefix="/api/products", tags=["Products"])  # tags для Swagger документации

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
