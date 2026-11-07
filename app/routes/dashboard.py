"""Rutas del dashboard protegido por sesión."""

from flask import Blueprint, redirect, render_template, session, url_for

from app.db import query_raw

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def index():
    """Panel principal: lista usuarios y actividad ficticia."""
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    users = query_raw(
        "SELECT id, username, email, role FROM users ORDER BY id"
    )
    logs = query_raw(
        "SELECT a.id, u.username, a.action, a.created_at "
        "FROM activity_logs a LEFT JOIN users u ON u.id = a.user_id "
        "ORDER BY a.created_at DESC LIMIT 20"
    )

    return render_template("dashboard.html", users=users, logs=logs)
