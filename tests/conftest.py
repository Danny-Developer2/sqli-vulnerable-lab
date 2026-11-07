"""
Configuración común de las pruebas del laboratorio.

Las pruebas asumen que los servicios están corriendo (scripts/start.sh) y
contactan con la aplicación a través de http://127.0.0.1:8080.
"""

import os

import pytest


@pytest.fixture(scope="session")
def base_url():
    """URL base de la aplicación en ejecución."""
    return os.environ.get("LAB_URL", "http://127.0.0.1:8080")
