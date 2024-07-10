from flask import Flask
from flask_cors import CORS
from app.views import *

app = Flask(__name__)
CORS(app)

# Rutas existentes
app.route("/", methods=["GET"])(index)
app.route("/crear_usuario", methods=["POST"])(crear_usuario)
app.route("/traer_usuarios", methods=["GET"])(traer_usuarios)
app.route("/traer_usuario/<int:id>", methods=["GET"])(traer_usuario)
app.route("/actualizar_usuario/<int:id>", methods=["PUT"])(actualizar_usuario)
app.route("/eliminar_usuario/<int:id>", methods=["DELETE"])(eliminar_usuario)
app.route("/reservas", methods=["GET"])(reservas)
app.route("/crear_reserva", methods=["POST"])(crear_reserva)
app.route("/traer_reservas", methods=["GET"])(traer_reservas)
app.route("/traer_reserva/<string:emailUsuario>", methods=["GET"])(traer_reserva)
app.route("/actualizar_reserva/<string:emailUsuario>", methods=["PUT"])(actualizar_reserva)
app.route("/eliminar_reserva/<string:emailUsuario>", methods=["DELETE"])(eliminar_reserva)

if __name__ == "__main__":
    app.run(debug=True)
