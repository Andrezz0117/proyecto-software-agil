"""
Backend API - FastAPI
Punto de entrada principal de la API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Proyecto Software Ágil - API",
    description="API backend del proyecto de Ingeniería de Software II",
    version="0.1.0",
)

# Configuración de CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Endpoint raíz de la API."""
    return {"message": "API del Proyecto Software Ágil funcionando correctamente"}


@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud."""
    return {"status": "ok"}
