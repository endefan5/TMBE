from flask import Flask
from flask_cors import CORS
from app.database import iniciar_app
from app.views import *

app = Flask(__name__)
iniciar_app(app)
CORS(app)

app.route("/", methods=["GET"])(index)
app.route("/crear_usuario", methods=["POST"])(crear_usuario)
app.route("/traer_usuarios", methods=["GET"])(traer_usuarios)
app.route("/traer_usuario/<int:id>", methods=["GET"])(traer_usuario)
app.route("/actualizar_usuario/<int:id>", methods=["PUT"])(actualizar_usuario)
app.route("/eliminar_usuario/<int:id>", methods=["DELETE"])(eliminar_usuario)
app.route("/crear_reserva", methods=["POST"])(crear_reserva)
app.route("/traer_reservas", methods=["GET"])(traer_reservas)
app.route("/traer_reserva/<int:idReserva>", methods=["GET"])(traer_reserva)
app.route("/actualizar_reserva/<int:idReserva>", methods=["PUT"])(actualizar_reserva)
app.route("/eliminar_reserva/<int:idReserva>", methods=["DELETE"])(eliminar_reserva)

if __name__ == "__main__":
    app.run(debug=True)
