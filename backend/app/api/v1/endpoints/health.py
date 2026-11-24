# backend/app/api/v1/endpoints/health.py
"""Health check endpoints for the FastAPI application.
Provides liveness (/health) and readiness (/health/ready) checks.
Readiness verifies Firebase Admin initialization and a simple Firestore ping.
"""

from fastapi import APIRouter, HTTPException, status

from backend.app.core.config import config
from backend.app.infrastructure.firebase.firebase_admin import firebase_app
from backend.app.infrastructure.firebase.firestore_client import get_firestore_client

router = APIRouter()


@router.get("/health", tags=["health"])
async def health() -> dict:
    """Liveness probe – always returns OK if the app is running."""
    return {
        "status": "healthy",
        "application": config.APP_NAME,
    }


@router.get("/health/ready", tags=["health"])
async def readiness() -> dict:
    """Readiness probe – checks critical dependencies.
    Returns 200 when Firebase is initialized and Firestore can be contacted.
    """
    # Verify Firebase initialization
    if firebase_app is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Firebase not initialized",
        )
    # Simple Firestore ping: attempt to get a reference to a known collection.
    try:
        client = get_firestore_client()
        # Perform a minimal operation – list collections (no data needed).
        _ = list(client.collections())
    except Exception as exc:  # pragma: no cover – defensive
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Firestore connectivity issue",
        ) from exc

    return {
        "status": "ready",
        "application": config.APP_NAME,
    }
