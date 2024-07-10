from flask import Flask, g
from mysql.connector import connect

DB_CONFIG = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "",
    "database": "proycodoacodo"
}

def get_db_connection():
    if "db" not in g:
        g.db = connect(**DB_CONFIG)
    return g.db

def cerrar_base(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def iniciar_app(app: Flask):
    app.teardown_appcontext(cerrar_base)
