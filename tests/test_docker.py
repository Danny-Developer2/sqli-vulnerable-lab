"""Pruebas de infraestructura: contenedores y exposición de puertos."""

import json
import subprocess


def _running_containers():
    output = subprocess.check_output(
        ["docker", "ps", "--format", "{{json .}}"],
        text=True,
    )
    return [json.loads(line) for line in output.splitlines() if line.strip()]


def test_contenedores_del_lab_activos():
    containers = _running_containers()
    names = [container["Names"] for container in containers]
    assert any("sqli-lab-web" in name for name in names), names
    assert any("sqli-lab-db" in name for name in names), names


def test_db_no_expone_puertos():
    containers = _running_containers()
    db = next(c for c in containers if "sqli-lab-db" in c["Names"])
    # "3306/tcp" es el puerto expuesto internamente; no debe haber publicación
    # con "->" (enlace a un puerto del host).
    assert "->" not in db["Ports"], f"La DB publica puertos: {db['Ports']}"


def test_web_expone_solo_127_0_0_1_8080():
    containers = _running_containers()
    web = next(c for c in containers if "sqli-lab-web" in c["Names"])
    assert "127.0.0.1:8080->8080/tcp" in web["Ports"], web["Ports"]
