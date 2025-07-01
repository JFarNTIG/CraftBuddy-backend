"""
Shared pytest fixtures.
"""

import pytest
from flask import Flask
from app import create_app

# ---------- core fixtures ----------

@pytest.fixture(scope="session")
def app():
    """Flask application configured for tests."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture(scope="session")
def client(app: Flask):
    """Flask test client (handles cookies, headers)."""
    return app.test_client()

