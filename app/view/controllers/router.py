from fastapi import APIRouter

from app.view.controllers.health import health_controller

api_router = APIRouter()

# Inclui o router do health check
api_router.include_router(health_controller.router, tags=["health"])
