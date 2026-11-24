# backend/app/infrastructure/firebase/firestore_client.py
"""Firestore client singleton.
Provides a thin wrapper to obtain a Firestore client from the initialized
Firebase app. The client is created lazily on first use.
"""

from __future__ import annotations

import logging
from typing import Optional

from firebase_admin import firestore

from backend.app.infrastructure.firebase.firebase_admin import firebase_app

logger = logging.getLogger(__name__)

_firestore_client: Optional[firestore.Client] = None


def get_firestore_client() -> firestore.Client:
    """Return a Firestore client instance.

    Raises:
        RuntimeError: If Firebase has not been initialised.
    """
    global _firestore_client
    if _firestore_client is not None:
        return _firestore_client
    if firebase_app is None:
        raise RuntimeError(
            "Firebase app is not initialised; cannot create Firestore client."
        )
    _firestore_client = firestore.client()
    logger.debug("Firestore client initialised.")
    return _firestore_client
