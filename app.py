from flask import Flask
from app.views import *

app = Flask(__name__)

app.route("/", methods={"GET"})(index)

app.route("/crear_usuario", methods={"POST"})(crear_usuario)
app.route("/traer_usuarios", methods={"GET"})(traer_usuarios)

if __name__ == "__main__":
    app.run(debug=True)
