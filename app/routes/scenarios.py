"""Rutas con escenarios de SQL Injection: error-based, boolean-based y time-based."""

from flask import Blueprint, render_template, request

from app.db import query_raw

scenarios_bp = Blueprint("scenarios", __name__)


@scenarios_bp.route("/search")
def search():
    """Escenario basado en errores: expone el error SQL real en la respuesta."""
    q = request.args.get("q")

    if q is None:
        return render_template("search.html")

    # Consulta concatenada a propósito (VULNERABLE).
    sql = f"SELECT id, name, price, stock FROM products WHERE name LIKE '%{q}%'"

    error = None
    results = None
    try:
        results = query_raw(sql)
    except Exception as exc:
        error = str(exc)

    return render_template(
        "results.html",
        title="Buscador de productos (error-based)",
        scenario="error-based",
        sql=sql,
        results=results,
        error=error,
    )


@scenarios_bp.route("/product")
def product():
    """Escenario basado en booleano y en tiempo (SLEEP)."""
    pid = request.args.get("id")

    if pid is None:
        return render_template("product.html")

    # Consulta concatenada a propósito (VULNERABLE).
    sql = f"SELECT id, name, price, stock FROM products WHERE id = '{pid}'"

    error = None
    results = None
    try:
        results = query_raw(sql)
    except Exception as exc:
        error = str(exc)

    return render_template(
        "results.html",
        title="Producto por ID (boolean-based / time-based)",
        scenario="boolean-time",
        sql=sql,
        results=results,
        error=error,
    )
