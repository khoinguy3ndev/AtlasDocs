from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title="AtlasDocs API",
    description="RESTful API backend for AtlasDocs",
    version="0.1.0",
)

app.include_router(health.router)
