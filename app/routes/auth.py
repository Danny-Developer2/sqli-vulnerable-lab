"""Rutas de autenticación: login vulnerable, login seguro y logout."""

from flask import Blueprint, redirect, render_template, request, session, url_for

from app.db import query_parametrized, query_raw

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login VULNERABLE: concatena la entrada del usuario en la consulta SQL."""
    error = None
    sql = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Consulta concatenada a propósito (NO usar en código real).
        sql = (
            "SELECT id, username, role FROM users "
            f"WHERE username = '{username}' AND password = '{password}'"
        )

        try:
            rows = query_raw(sql)
        except Exception as exc:  # pragma: no cover - el error también es didáctico
            error = f"Error SQL: {exc}"
            return render_template("login.html", error=error, sql=sql)

        if rows:
            session["user_id"] = rows[0]["id"]
            session["username"] = rows[0]["username"]
            session["role"] = rows[0]["role"]
            return redirect(url_for("dashboard.index"))

        error = "Credenciales inválidas."

    return render_template("login.html", error=error, sql=sql)


@auth_bp.route("/secure-login", methods=["GET", "POST"])
def secure_login():
    """Login SEGURO: usa consulta parametrizada con marcadores %s."""
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        sql = "SELECT id, username, role FROM users WHERE username = %s AND password = %s"
        try:
            rows = query_parametrized(sql, (username, password))
        except Exception as exc:  # pragma: no cover
            error = f"Error SQL: {exc}"
            return render_template("secure_login.html", error=error)

        if rows:
            session["user_id"] = rows[0]["id"]
            session["username"] = rows[0]["username"]
            session["role"] = rows[0]["role"]
            return redirect(url_for("dashboard.index"))

        error = "Credenciales inválidas."

    return render_template("secure_login.html", error=error)


@auth_bp.route("/logout")
def logout():
    """Cierra la sesión y vuelve al login."""
    session.clear()
    return redirect(url_for("auth.login"))
