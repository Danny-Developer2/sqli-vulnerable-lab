#!/usr/bin/env bash
# Muestra los logs en tiempo real de todos los servicios.
set -euo pipefail

cd "$(dirname "$0")/.."

docker compose logs -f
