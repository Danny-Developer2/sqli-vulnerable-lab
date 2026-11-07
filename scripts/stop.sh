#!/usr/bin/env bash
# Detiene los contenedores conservando el volumen de datos.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[stop] Deteniendo el laboratorio..."
docker compose down

echo "[stop] Contenedores detenidos."
