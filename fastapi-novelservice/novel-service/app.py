from fastapi import FastAPI
from .routers import novels

app = FastAPI()

app.include_router(novels.router)


@app.get("/")
def index():
    return "Hello World"
