"""Capa de acceso a la base de datos con PyMySQL.

Incluye dos variantes deliberadamente diferenciadas:

* ``query_raw``: ejecuta una consulta SQL ya concatenada (VULNERABLE).
* ``query_parametrized``: usa marcadores ``%s`` y parámetros (SEGURO).
"""

import os

import pymysql
from flask import current_app


def _config():
    """Devuelve la configuración activa (dentro o fuera de contexto Flask)."""
    try:
        return current_app.config
    except RuntimeError:
        return {
            "DB_HOST": os.environ.get("DB_HOST", "db"),
            "DB_PORT": int(os.environ.get("DB_PORT", "3306")),
            "DB_NAME": os.environ.get("DB_NAME", "sqli_lab"),
            "DB_USER": os.environ.get("DB_USER", "lab_user"),
            "DB_PASSWORD": os.environ.get("DB_PASSWORD", "lab_pass_ficticio_cambiar"),
        }


def get_connection():
    """Abre una conexión PyMySQL con la configuración de la aplicación."""
    cfg = _config()
    return pymysql.connect(
        host=cfg["DB_HOST"],
        port=int(cfg["DB_PORT"]),
        user=cfg["DB_USER"],
        password=cfg["DB_PASSWORD"],
        database=cfg["DB_NAME"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        connect_timeout=10,
    )


def query_raw(sql):
    """Ejecuta SQL concatenado tal cual. VULNERABLE a inyección SQL."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()


def query_parametrized(sql, params):
    """Ejecuta SQL con marcadores ``%s`` y parámetros. Vía segura."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()
    finally:
        conn.close()
