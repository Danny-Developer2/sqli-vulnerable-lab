#!/bin/sh
# Entrypoint: espera a que MariaDB esté disponible antes de arrancar gunicorn.
set -e

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-3306}"
DB_USER="${DB_USER:-lab_user}"
DB_PASSWORD="${DB_PASSWORD:-lab_pass_ficticio_cambiar}"

export DB_HOST DB_PORT DB_USER DB_PASSWORD

echo "[entrypoint] Esperando a la base de datos en ${DB_HOST}:${DB_PORT}..."

attempt=0
until python -c "
import os
import pymysql
pymysql.connect(
    host=os.environ['DB_HOST'],
    port=int(os.environ['DB_PORT']),
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    connect_timeout=3,
).close()
" 2>/dev/null; do
  attempt=$((attempt + 1))
  if [ "$attempt" -ge 60 ]; then
    echo "[entrypoint] Tiempo de espera agotado." >&2
    exit 1
  fi
  echo "[entrypoint] Base de datos no disponible, reintentando en 2s..."
  sleep 2
done

echo "[entrypoint] Base de datos disponible. Iniciando la aplicación."
exec "$@"
