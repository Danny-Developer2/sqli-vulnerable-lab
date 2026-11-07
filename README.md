# SQLi Vulnerable Lab

[![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PyMySQL](https://img.shields.io/badge/PyMySQL-1.1.1-00758F?logo=mysql&logoColor=white)](https://pypi.org/project/PyMySQL/)
[![MariaDB](https://img.shields.io/badge/MariaDB-11.4-003545?logo=mariadb&logoColor=white)](https://mariadb.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-23.0.0-499848?logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![pytest](https://img.shields.io/badge/pytest-9.x-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/Purpose-Educational-blue)](SECURITY.md)

An **intentionally vulnerable** SQL Injection laboratory built with **Flask +
PyMySQL + MariaDB + Docker Compose**, used to teach how SQL injection works and
why parameterized queries are the correct defense.

> ⚠️ **WARNING**: This application is intentionally insecure. Do **not** deploy
> it on a public network and never use its techniques against systems without
> explicit authorization. All data is fictitious.

---

## Table of Contents

- [Description](#description)
- [Educational Objectives](#educational-objectives)
- [Features](#features)
- [Technologies](#technologies)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Lab](#running-the-lab)
- [Access](#access)
- [Demo Credentials](#demo-credentials)
- [Available Scenarios](#available-scenarios)
- [Testing Examples](#testing-examples)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Security Warnings](#security-warnings)
- [Author](#author)
- [License](#license)
- [Instructions in Spanish / Instrucciones en español](#instructions-in-spanish--instrucciones-en-español)

---

## Description

**SQLi Vulnerable Lab** is a containerized, intentionally vulnerable web
application designed for hands-on learning of SQL injection. It exposes a set of
deliberately unsafe endpoints alongside a secure, parameterized alternative, so
students can compare an attack surface with its correct remediation in the same
running environment.

The lab runs entirely in Docker Compose: a Flask/Gunicorn web service and a
MariaDB database on an isolated bridge network. The database publishes **no**
ports, and the web service binds only to `127.0.0.1:8080`.

## Educational Objectives

- Recognize how string concatenation in SQL queries creates injection points.
- Execute and understand classic authentication-bypass payloads.
- Differentiate **error-based**, **boolean-based**, and **time-based** SQLi.
- Learn how to infer data through response differences and time delays.
- Understand why parameterized queries (`%s` placeholders) neutralize injection.
- Practice safe, responsible, and authorized vulnerability testing.
- Adopt secure coding habits from a concrete, working example.

## Features

- ✅ Vulnerable login with classic `' OR '1'='1' -- -` bypass.
- ✅ Secure login using parameterized queries for side-by-side comparison.
- ✅ Error-based search endpoint that surfaces the raw SQL error.
- ✅ Boolean-based product lookup with observable true/false responses.
- ✅ Time-based product lookup using `SLEEP(5)`.
- ✅ Session-based dashboard listing fictitious users and activity.
- ✅ Fictitious seed data (users, products, customers, logs).
- ✅ Docker Compose orchestration with a health-checked database.
- ✅ Automated pytest suite covering every scenario plus infrastructure checks.

## Technologies

| Layer | Technology |
| --- | --- |
| Language | Python 3.12 |
| Web framework | Flask 3.1.0 |
| WSGI server | Gunicorn 23.0.0 |
| Database driver | PyMySQL 1.1.1 |
| Database | MariaDB 11.4 |
| Orchestration | Docker + Docker Compose v2 |
| Testing | pytest 9.x + requests |

## Architecture

```
┌─────────────────────────────┐        ┌─────────────────────────────┐
│  Host: 127.0.0.1:8080       │        │  Internal network: sqli-net │
│                             │        │                             │
│  ┌───────────────────────┐  │        │  ┌───────────────────────┐  │
│  │  web (gunicorn)       │  │        │  │  db (mariadb:11.4)    │  │
│  │  Flask app            │──┼────────┼─▶│  no published ports   │  │
│  │  port 8080            │  │        │  │  volume: db-data      │  │
│  └───────────────────────┘  │        │  └───────────────────────┘  │
└─────────────────────────────┘        └─────────────────────────────┘
```

- `app/` — Flask application. Blueprints: `auth`, `dashboard`, `scenarios`.
- `app/db.py` — PyMySQL helper exposing a raw (vulnerable) and a parameterized
  (safe) query variant.
- `database/` — `init.sql` (schema) and `seed.sql` (fictitious data).
- `docker-compose.yml` — `db` and `web` services on the `sqli-net` bridge.
- `scripts/` — helper scripts for start, stop, reset, logs, and cleanup.
- `tests/` — pytest suite using `requests` against the running app.
- `docs/` — additional documentation (`seguridad.md`) and the four PDF guides.

## Requirements

- Docker 29+ and Docker Compose v2+
- Python 3.12+ (only to run the local pytest suite)
- A virtualenv with `pytest` and `requests` (optional, for tests)

## Installation

```bash
git clone <repository-url>
cd sqli-vulnerable-lab

# (optional) configure local environment
cp .env.example .env
```

> `.env` is git-ignored. Only `.env.example` with fictitious placeholders is
> committed. Do not put real credentials in it.

## Running the Lab

```bash
./scripts/start.sh
```

This runs `docker compose build` and `docker compose up -d`. The application
will be available at **http://127.0.0.1:8080** (bound only to `127.0.0.1`; the
database publishes no ports).

### Helper Scripts

| Script | Description |
| --- | --- |
| `scripts/start.sh` | `docker compose build` + `up -d` |
| `scripts/stop.sh` | `docker compose down` (keeps the volume) |
| `scripts/reset_db.sh` | `down -v` and reinitialize schema + seed |
| `scripts/cleanup.sh` | `down -v --rmi all` (removes images) |
| `scripts/logs.sh` | `docker compose logs -f` |

## Access

- Web application: **http://127.0.0.1:8080**
- Login (vulnerable): `http://127.0.0.1:8080/login`
- Secure login: `http://127.0.0.1:8080/secure-login`
- Dashboard (session required): `http://127.0.0.1:8080/dashboard`
- Search (error-based): `http://127.0.0.1:8080/search?q=`
- Product (boolean/time-based): `http://127.0.0.1:8080/product?id=`

## Demo Credentials

All accounts are **fictitious** and exist only in the local seed data.

| Username | Password | Role |
| --- | --- | --- |
| `admin` | `Password123!` | admin |
| `jdoe` | `Password123!` | user |
| `asmith` | `Password123!` | user |
| `mbrown` | `Password123!` | auditor |

## Available Scenarios

1. **Vulnerable login** (`/login`) — direct concatenation in
   `SELECT ... WHERE username = '{u}' AND password = '{p}'`.
   - Bypass payload: `admin' OR '1'='1' -- -`
2. **Secure login** (`/secure-login`) — parameterized query using `%s`.
3. **Error-based search** (`/search?q=`) — returns the real SQL error.
   Payload: `'`
4. **Boolean-based product** (`/product?id=`) — `1' AND '1'='1` vs `1' AND '1'='2`.
5. **Time-based product** (`/product?id=`) — `1' AND SLEEP(5) -- -` (~5 s delay).

## Testing Examples

Start the lab, then run the pytest suite:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest requests
pytest -v
```

The tests contact `http://127.0.0.1:8080` (configurable via `LAB_URL`).

Manual examples:

```bash
# Vulnerable login bypass
curl -i -X POST http://127.0.0.1:8080/login \
  -d "username=admin' OR '1'='1' -- -&password=anything"

# Error-based search
curl "http://127.0.0.1:8080/search?q='"

# Boolean-based product
curl "http://127.0.0.1:8080/product?id=1' AND '1'='1"

# Time-based product (should take ~5 seconds)
curl "http://127.0.0.1:8080/product?id=1' AND SLEEP(5) -- -"

# Secure login rejects the bypass
curl -i -X POST http://127.0.0.1:8080/secure-login \
  -d "username=admin' OR '1'='1' -- -&password=anything"
```

## Documentation

- [README.md](README.md) — this document.
- [docs/seguridad.md](docs/seguridad.md) — security notes (Spanish).
- [SECURITY.md](SECURITY.md) — security policy and responsible disclosure.
- [LICENSE](LICENSE) — MIT license.
- [docs/INSTALLATION_GUIDE.pdf](docs/INSTALLATION_GUIDE.pdf) — installation and configuration manual.
- [docs/SQL_INJECTION_LAB_GUIDE.pdf](docs/SQL_INJECTION_LAB_GUIDE.pdf) — lab and exploitation guide.
- [docs/SECURITY_ASSESSMENT_REPORT.pdf](docs/SECURITY_ASSESSMENT_REPORT.pdf) — technical security report.
- [docs/SQL_INJECTION_REMEDIATION_GUIDE.pdf](docs/SQL_INJECTION_REMEDIATION_GUIDE.pdf) — remediation guide.

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `Connection refused` on port 8080 | Lab not started | Run `./scripts/start.sh` and wait for the DB healthcheck |
| `docker compose` command not found | Compose v2 missing | Install Docker Desktop or the Compose plugin |
| Tests fail with connection errors | App unreachable / wrong URL | Set `LAB_URL=http://127.0.0.1:8080` and confirm the app is up |
| Database schema not applied | Stale volume | Run `./scripts/reset_db.sh` |
| Changes not reflected in `web` | Image not rebuilt | Run `docker compose build` (or `./scripts/reset_db.sh`) |
| Port 8080 already in use | Another process bound to it | Stop the other process or change the host port mapping |

## Security Warnings

- The application is **intentionally vulnerable**. Never deploy it publicly.
- Do not point any payload at systems you do not own or are not authorized to
  test.
- Passwords in the seed data are stored in **plain text only** so the lab is
  reproducible. Real systems must use hashing (`bcrypt`, `argon2`, ...).
- No elevated privileges inside the containers.
- The database publishes **no ports** to the host.
- The web service binds **only** to `127.0.0.1:8080`.
- No sensitive host directories are mounted.

See [SECURITY.md](SECURITY.md) for the full policy.

## Author

**Danny-Developer2**

## License

This project is licensed under the [MIT License](LICENSE).

---

## Instructions in Spanish / Instrucciones en español

# Laboratorio de SQLi Vulnerable

Laboratorio **educativo** de inyección SQL con Flask + PyMySQL + MariaDB,
empaquetado con Docker Compose. La aplicación es **intencionalmente vulnerable**
y solo debe usarse en entornos locales y controlados.

> ⚠️ **ADVERTENCIA**: No despliegues este laboratorio en una red pública ni uses
> sus técnicas contra sistemas sin autorización expresa. Todos los datos son
> ficticios.

### Objetivos educativos

- Reconocer cómo la concatenación de cadenas en consultas SQL crea puntos de
  inyección.
- Ejecutar y comprender payloads clásicos de omisión de autenticación.
- Diferenciar los tipos **error-based**, **boolean-based** y **time-based**.
- Aprender a inferir datos mediante diferencias de respuesta y retardos.
- Comprender por qué las consultas parametrizadas neutralizan la inyección.
- Practicar pruebas de vulnerabilidades de forma segura y autorizada.

### Requisitos

- Docker 29+ y Docker Compose v2+
- Python 3.12+ (solo para ejecutar las pruebas locales)
- Un venv con `pytest` y `requests` (opcional, para las pruebas)

### Instalación

```bash
git clone <url-del-repositorio>
cd sqli-vulnerable-lab

# (opcional) configura el entorno local
cp .env.example .env
```

### Ejecución

```bash
./scripts/start.sh
```

La aplicación quedará disponible en **http://127.0.0.1:8080** (solo enlazada a
`127.0.0.1`; la base de datos no publica puertos).

| Script | Descripción |
| --- | --- |
| `scripts/start.sh` | `docker compose build` + `up -d` |
| `scripts/stop.sh` | `docker compose down` (conserva el volumen) |
| `scripts/reset_db.sh` | `down -v` y reinicializa esquema + seed |
| `scripts/cleanup.sh` | `down -v --rmi all` (borra imágenes) |
| `scripts/logs.sh` | `docker compose logs -f` |

### Credenciales ficticias de demostración

| Usuario | Contraseña | Rol |
| --- | --- | --- |
| `admin` | `Password123!` | admin |
| `jdoe` | `Password123!` | user |
| `asmith` | `Password123!` | user |
| `mbrown` | `Password123!` | auditor |

### Escenarios disponibles

1. **Login vulnerable** (`/login`): concatenación directa en
   `SELECT ... WHERE username = '{u}' AND password = '{p}'`.
   - Bypass: `admin' OR '1'='1' -- -`
2. **Login seguro** (`/secure-login`): consulta parametrizada con `%s`.
3. **Buscador error-based** (`/search?q=`): muestra el error SQL real.
   Payload: `'`
4. **Producto boolean-based** (`/product?id=`): `1' AND '1'='1` vs `1' AND '1'='2`.
5. **Producto time-based** (`/product?id=`): `1' AND SLEEP(5) -- -` (~5 s).

### Ejemplos de pruebas

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest requests
pytest -v
```

Las pruebas contactan con `http://127.0.0.1:8080` (configurable con `LAB_URL`).

Ejemplos manuales:

```bash
# Bypass del login vulnerable
curl -i -X POST http://127.0.0.1:8080/login \
  -d "username=admin' OR '1'='1' -- -&password=loquesea"

# Buscador basado en errores
curl "http://127.0.0.1:8080/search?q='"

# Producto boolean-based
curl "http://127.0.0.1:8080/product?id=1' AND '1'='1"

# Producto time-based (tarda ~5 segundos)
curl "http://127.0.0.1:8080/product?id=1' AND SLEEP(5) -- -"

# El login seguro rechaza el bypass
curl -i -X POST http://127.0.0.1:8080/secure-login \
  -d "username=admin' OR '1'='1' -- -&password=loquesea"
```

### Documentación

- [README.md](README.md) — este documento.
- [docs/seguridad.md](docs/seguridad.md) — notas de seguridad.
- [SECURITY.md](SECURITY.md) — política de seguridad y divulgación responsable.
- [LICENSE](LICENSE) — licencia MIT.
- [docs/INSTALLATION_GUIDE.pdf](docs/INSTALLATION_GUIDE.pdf) — manual de instalación y configuración.
- [docs/SQL_INJECTION_LAB_GUIDE.pdf](docs/SQL_INJECTION_LAB_GUIDE.pdf) — guía del laboratorio y explotación.
- [docs/SECURITY_ASSESSMENT_REPORT.pdf](docs/SECURITY_ASSESSMENT_REPORT.pdf) — informe técnico de seguridad.
- [docs/SQL_INJECTION_REMEDIATION_GUIDE.pdf](docs/SQL_INJECTION_REMEDIATION_GUIDE.pdf) — guía de remediación.

### Solución de problemas

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `Connection refused` en el puerto 8080 | Laboratorio no iniciado | Ejecuta `./scripts/start.sh` y espera el healthcheck de la BD |
| Comando `docker compose` no encontrado | Falta Compose v2 | Instala Docker Desktop o el plugin de Compose |
| Las pruebas fallan por conexión | App inaccesible / URL incorrecta | Define `LAB_URL=http://127.0.0.1:8080` y verifica que esté activa |
| El esquema no se aplica | Volumen obsoleto | Ejecuta `./scripts/reset_db.sh` |
| Los cambios no se reflejan en `web` | Imagen no reconstruida | Ejecuta `docker compose build` (o `./scripts/reset_db.sh`) |
| Puerto 8080 ocupado | Otro proceso lo usa | Detén el otro proceso o cambia el mapeo de puertos |

### Advertencias de seguridad

- La aplicación es **intencionalmente vulnerable**. Nunca la despliegues
  públicamente.
- No apuntes ningún payload a sistemas que no te pertenezcan o no estés
  autorizado a probar.
- Las contraseñas del seed están en **texto plano solo** para que el laboratorio
  sea reproducible. Los sistemas reales deben usar hash (`bcrypt`, `argon2`, ...).
- Sin privilegios elevados en los contenedores.
- La base de datos **no publica puertos** al host.
- El servicio web se enlaza **solo** a `127.0.0.1:8080`.
- No se montan directorios sensibles del host.

### Autor y licencia

- **Autor:** Danny-Developer2
- **Licencia:** [MIT](LICENSE)
