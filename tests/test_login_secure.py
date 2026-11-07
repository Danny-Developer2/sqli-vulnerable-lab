"""Pruebas del login seguro (consulta parametrizada)."""

import requests


def test_secure_login_normal(base_url):
    session = requests.Session()
    response = session.post(
        f"{base_url}/secure-login",
        data={"username": "admin", "password": "Password123!"},
        allow_redirects=False,
        timeout=15,
    )
    assert response.status_code == 302, response.text
    assert "/dashboard" in response.headers.get("Location", "")


def test_secure_login_bypass_bloqueado(base_url):
    session = requests.Session()
    response = session.post(
        f"{base_url}/secure-login",
        data={"username": "admin' OR '1'='1' -- -", "password": "loquesea"},
        allow_redirects=False,
        timeout=15,
    )
    # No hay redirect: se queda en el formulario con el error.
    assert response.status_code == 200
    assert "Login seguro" in response.text
    assert "Credenciales inválidas" in response.text

    # La sesión no queda autenticada.
    dashboard = session.get(f"{base_url}/dashboard", allow_redirects=False, timeout=15)
    assert dashboard.status_code == 302
    assert "/login" in dashboard.headers.get("Location", "")
