# backend/tests/conftest.py
"""Pytest fixtures for FastAPI app testing.
Provides an ``AsyncClient`` fixture that wraps the FastAPI ``app``
instance using ``httpx.AsyncClient``. The client is yielded for each
test and closed afterward.
"""

import asyncio
import sys
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from backend.app.main import app

# Ensure the event loop policy works on Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
