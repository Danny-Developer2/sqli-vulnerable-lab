"""
SQLi Vulnerable Lab - Aplicación Flask intencionalmente vulnerable.

ADVERTENCIA: este proyecto es un laboratorio educativo. No debe desplegarse
en una red pública ni usarse contra sistemas sin autorización expresa.
"""

import os

from flask import Flask


def create_app():
    """Factory de la aplicación Flask con configuración por variables de entorno."""
    app = Flask(__name__)

    app.config.update(
        DB_HOST=os.environ.get("DB_HOST", "db"),
        DB_PORT=int(os.environ.get("DB_PORT", "3306")),
        DB_NAME=os.environ.get("DB_NAME", "sqli_lab"),
        DB_USER=os.environ.get("DB_USER", "lab_user"),
        DB_PASSWORD=os.environ.get("DB_PASSWORD", "lab_pass_ficticio_cambiar"),
        SECRET_KEY=os.environ.get("SECRET_KEY", "secreto_ficticio_cambiar"),
    )

    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.scenarios import scenarios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(scenarios_bp)

    return app


# Instancia global para gunicorn:  gunicorn "app:app"
app = create_app()
