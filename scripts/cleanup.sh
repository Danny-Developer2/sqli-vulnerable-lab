#!/usr/bin/env bash
# Limpieza total: contenedores, volumen de datos e imágenes construidas.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[cleanup] Eliminando contenedores, volumen e imágenes..."
docker compose down -v --rmi all

echo "[cleanup] Limpieza completada."
