#!/usr/bin/env bash
# Borra el volumen de base de datos y reinicializa el esquema y el seed.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[reset_db] Eliminando contenedores y volumen de datos..."
docker compose down -v

echo "[reset_db] Levantando de nuevo (init.sql + seed.sql se ejecutarán)..."
docker compose up -d --build

echo "[reset_db] Base de datos reinicializada."
