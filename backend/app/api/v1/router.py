# backend/app/api/v1/router.py
"""Root API router for version 1 endpoints.
Includes health endpoints and will later include auth, users, tickets.
"""

from fastapi import APIRouter

from backend.app.api.v1.endpoints import health

api_router = APIRouter()

# Include health routers
api_router.include_router(health.router)
