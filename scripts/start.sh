#!/usr/bin/env bash
# Construye y arranca el laboratorio (db + web) en segundo plano.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[start] Construyendo imágenes y levantando servicios..."
docker compose build
docker compose up -d

echo "[start] Laboratorio iniciado. Acceso: http://127.0.0.1:8080"
