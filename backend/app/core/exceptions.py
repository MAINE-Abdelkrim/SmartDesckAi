# backend/app/core/exceptions.py
"""Centralised exception hierarchy and FastAPI handler registration.
Only a simple implementation for Milestone 1 – a generic ``AppException``
that maps to a ``HTTPException`` with a configurable status code and detail.
"""

from __future__ import annotations

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    """Base application exception.
    Sub‑classes should provide ``status_code`` and ``detail`` attributes.
    """

    status_code: int = 500
    detail: str = "Internal server error"

    def __init__(
        self, detail: str | None = None, status_code: int | None = None
    ) -> None:
        if detail:
            self.detail = detail
        if status_code:
            self.status_code = status_code
        super().__init__(self.detail)


def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    """Convert ``AppException`` to a JSON response."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


def add_exception_handlers(app) -> None:
    """Register global exception handlers on a FastAPI app."""
    app.add_exception_handler(AppException, app_exception_handler)

    # Generic HTTPException handler
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})
