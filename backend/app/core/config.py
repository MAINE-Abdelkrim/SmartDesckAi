# backend/app/core/config.py
"""Application configuration using Pydantic Settings.
Provides environment‑variable based configuration for the FastAPI app.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import List, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Basic app info
    APP_NAME: str = "SmartDesk AI"
    APP_ENV: str = "development"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    # CORS configuration – comma‑separated list in env var
    CORS_ORIGINS: str = "http://localhost:5173"

    # Firebase configuration
    FIREBASE_PROJECT_ID: str = "your-firebase-project-id"
    FIREBASE_CREDENTIALS_PATH: Optional[
        str
    ] = None  # Path to service‑account JSON; if omitted, use ADC

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS_ORIGINS into a list of origins.
        Supports a comma‑separated string.
        """
        return [
            origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()
        ]

    @property
    def firebase_credentials_path(self) -> Optional[Path]:
        if self.FIREBASE_CREDENTIALS_PATH:
            return Path(self.FIREBASE_CREDENTIALS_PATH).expanduser().resolve()
        return None


config = Config()
