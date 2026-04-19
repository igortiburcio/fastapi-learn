from fastapi import APIRouter

from app.api.v1.endpoints import health

api_router = APIRouter()

# Inclui o router do health check
api_router.include_router(health.router, tags=["health"])
