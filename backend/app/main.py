"""FastAPI application entry point for SmartDesk AI backend.
Initialises Firebase, registers routers, configures CORS, logging and exception handling.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import config
from backend.app.core.logging import setup_logging
from backend.app.core.exceptions import add_exception_handlers
from backend.app.infrastructure.firebase.firebase_admin import init_firebase
from backend.app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan context manager.
    Initialise Firebase on startup and clean up on shutdown.
    """
    # Initialise Firebase (singleton)
    init_firebase()
    yield
    # No explicit shutdown needed for Firebase Admin SDK


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Creating FastAPI app for %s", config.APP_NAME)

    app = FastAPI(
        title=config.APP_NAME,
        debug=config.DEBUG,
        version="0.1.0",
        lifespan=lifespan,
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    app.include_router(api_router, prefix=config.API_V1_PREFIX)

    # Exception handlers
    add_exception_handlers(app)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=config.DEBUG,
    )
