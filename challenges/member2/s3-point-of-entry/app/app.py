from flask import Flask, request, render_template, redirect, session
import pymysql
import os

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET", "devsecret")

DB_HOST = os.getenv("DB_HOST", "s3-db")
DB_USER = os.getenv("DB_USER", "portal")
DB_PASS = os.getenv("DB_PASS", "portalpass")
DB_NAME = os.getenv("DB_NAME", "portal")


def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        autocommit=True
    )


@app.get("/")
def home():
    return redirect("/login")


@app.get("/login")
def login_form():
    return render_template("login.html")


@app.post("/login")
def login_post():
    u = request.form.get("username", "")
    p = request.form.get("password", "")

    # Intentionally insecure pattern for CTF lab only (do not use in real systems)
    q = f"SELECT id, username, role FROM users WHERE username='{u}' AND password='{p}' LIMIT 1;"

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(q)
            row = cur.fetchone()
    finally:
        conn.close()

    if row:
        session["role"] = row[2]
        return redirect("/admin" if row[2] == "admin" else "/user")

    return render_template("login.html", error="Invalid credentials")


@app.get("/user")
def user_area():
    if "role" not in session:
        return redirect("/login")
    return "<h3>User Area</h3><p>No flag here.</p>"


@app.get("/admin")
def admin_area():
    if session.get("role") != "admin":
        return redirect("/login")

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT flag FROM users WHERE role='admin' LIMIT 1;")
            flag = cur.fetchone()[0]
    finally:
        conn.close()

    return render_template("admin.html", flag=flag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)