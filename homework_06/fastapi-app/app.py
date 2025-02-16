from fastapi import FastAPI
from views import router as api_router

app = FastAPI(title="Docker Compose && FastAPI")
app.include_router(api_router)


# root
@app.get("/")
def hello_root():
    return {
        "message": "Hello World!",
    }
