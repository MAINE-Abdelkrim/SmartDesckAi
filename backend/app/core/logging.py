"""Simple logging configuration for the FastAPI application.
Uses the standard library ``logging`` module and respects the ``LOG_LEVEL``
environment variable via the ``Config`` object.
"""

import logging
from typing import Optional

from backend.app.core.config import config


def setup_logging(level: Optional[str] = None) -> None:
    """Configure the root logger.

    Args:
        level: Optional explicit log level string (e.g., "DEBUG"). If omitted the
            level from :class:`backend.app.core.config.Config` is used.
    """
    log_level = (level or config.LOG_LEVEL).upper()
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Reduce noise from uvicorn loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
