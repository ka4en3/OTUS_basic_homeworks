from fastapi import FastAPI
from views import api_router, html_router

app = FastAPI(title="Docker Compose && FastAPI")
app.include_router(api_router)
app.include_router(html_router)

# root
@app.get("/")
def hello_root():
    return {
        "message": "Hello World!",
    }
