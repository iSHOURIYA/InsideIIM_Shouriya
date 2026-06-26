from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router

api_router = APIRouter()

for route in health_router.routes:
    api_router.routes.append(route)
