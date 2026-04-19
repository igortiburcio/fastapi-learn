from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="FastAPI Learn",
    description="API inicial com a melhor estrutura",
    version="0.1.0",
)

# Adiciona todas as rotas da v1 com o prefixo "/api/v1"
app.include_router(api_router, prefix="/api/v1")
