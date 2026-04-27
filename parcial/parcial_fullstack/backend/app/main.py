from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import create_db_and_tables
from app.routers import categorias, ingredientes, productos

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="Parcial Programacion 4 - Catalogo de Productos", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categorias.router, prefix="/api")
app.include_router(ingredientes.router, prefix="/api")
app.include_router(productos.router, prefix="/api")

@app.get("/")
def healthcheck():
    return {"status": "ok", "docs": "/docs"}
