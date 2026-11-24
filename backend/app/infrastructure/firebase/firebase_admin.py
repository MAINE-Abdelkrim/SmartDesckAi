# backend/app/infrastructure/firebase/firebase_admin.py
"""Firebase Admin SDK initialization.
Ensures a singleton Firebase app instance based on configuration.
"""

from __future__ import annotations

import logging
from typing import Optional

from firebase_admin import credentials, initialize_app, get_app, _apps

from backend.app.core.config import config

logger = logging.getLogger(__name__)

# Global reference to the initialized Firebase app (or None)
firebase_app: Optional[object] = None


def init_firebase() -> None:
    """Initialise Firebase Admin SDK if not already initialised.

    Uses a service‑account JSON file if ``FIREBASE_CREDENTIALS_PATH`` is set,
    otherwise falls back to Application Default Credentials.
    """
    global firebase_app
    if _apps:
        # Already initialised – reuse existing app
        firebase_app = get_app()
        logger.debug("Firebase app already initialised; reusing existing instance.")
        return

    if config.firebase_credentials_path:
        cred = credentials.Certificate(str(config.firebase_credentials_path))
        logger.info(
            "Initializing Firebase with service‑account credentials from %s",
            config.firebase_credentials_path,
        )
    else:
        cred = credentials.ApplicationDefault()
        logger.info("Initializing Firebase using Application Default Credentials.")

    firebase_app = initialize_app(cred, {"projectId": config.FIREBASE_PROJECT_ID})
    logger.info("Firebase app initialised for project %s", config.FIREBASE_PROJECT_ID)
