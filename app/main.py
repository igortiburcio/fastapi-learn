from fastapi import FastAPI

from app.view.controllers.router import api_router

app = FastAPI(
    title="FastAPI Learn",
    description="API inicial com a melhor estrutura",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")
