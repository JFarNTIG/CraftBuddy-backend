"""
Flask application factory.

Gunicorn (or wsgi.py) will call `create_app()` to obtain the runnable instance.
"""

import os
from pathlib import Path

from flask import Flask

from app.api.games import bp as games_bp
from app.api.items import bp as items_bp
from app.api.errors import bp as errors_bp


def create_app() -> Flask:
    """
    Application factory.

    Returns
    -------
    flask.Flask
        Configured Flask application.
    """
    app = Flask(__name__)
    configure_app(app)
    register_blueprints(app)
    return app


def configure_app(app: Flask) -> None:
    """Load basic settings and secrets into *app.config*."""
    app.config.update(
        ENV=os.getenv("FLASK_ENV", "production"),
    )


def register_blueprints(app: Flask) -> None:
    """Attach blueprints to the application."""
    app.register_blueprint(games_bp, url_prefix="/api")
    app.register_blueprint(items_bp, url_prefix="/api")
    app.register_blueprint(errors_bp, url_prefix="/api")