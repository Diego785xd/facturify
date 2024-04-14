import uvicorn
from fastapi import FastAPI

from app.routers import health
from app.routers import ocr
from app.routers import users
from app.routers import scraper

app = FastAPI()

app.include_router(health.router)
app.include_router(ocr.router)
app.include_router(users.router)
app.include_router(scraper.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
