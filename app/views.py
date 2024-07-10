from flask import jsonify, request, redirect, url_for, render_template, app
from app.models import Reserva, Usuario

def index():
    return jsonify({'message': "Bienvenidos a la API de la Taberna de Moe"})

def crear_usuario():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    nuevo_usuario = Usuario(None, usuario, clave, nombre, apellido, email, telefono)
    nuevo_usuario.guardar()
    # Redirigir a la página de reservas después de crear el usuario
    return redirect(url_for('reservas'))

def reservas():
    return render_template('Reserva.html')

def traer_usuarios():
    usuarios = Usuario.traer_todos()
    return jsonify([usuario.serialize() for usuario in usuarios])

def traer_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    return jsonify(usuario.serialize())

def actualizar_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    usuario.usuario = data['usuario']
    usuario.clave = data['clave']
    usuario.nombre = data['nombre']
    usuario.apellido = data['apellido']
    usuario.email = data['email']
    usuario.telefono = data['telefono']
    usuario.guardar()
    return jsonify({'message': 'Usuario actualizado.'})

def eliminar_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    usuario.eliminar()
    return jsonify({'message': 'Usuario eliminado satisfactoriamente.'})

def crear_reserva():
    cantidadPersonas = request.form.get("cantidadPersonas")
    fecha = request.form.get("fecha")
    ubicacion = request.form.get("ubicacion")
    ocasionEspecial = request.form.get("ocasionEspecial")
    ocasionEspecialCual = request.form.get("ocasionEspecialCual")
    emailUsuario = request.form.get("emailUsuario")
    telefonoUsuario = request.form.get("telefonoUsuario")
    nombreCompletoUsuario = request.form.get("nombreCompletoUsuario")

    # Validación de los datos, asegurándote de que los tipos de datos sean correctos y que los valores estén dentro de los rangos esperados

    nueva_reserva = Reserva(
        cantidadPersonas=cantidadPersonas,
        fecha=fecha,
        ubicacion=ubicacion,
        ocasionEspecial=ocasionEspecial,
        ocasionEspecialCual=ocasionEspecialCual,
        emailUsuario=emailUsuario,
        telefonoUsuario=telefonoUsuario,
        nombreCompletoUsuario=nombreCompletoUsuario
    )
    nueva_reserva.guardar()

    return jsonify({"message": "Reserva creada satisfactoriamente"}), 201

def traer_reservas():
    reservas = Reserva.traer_todos()
    return jsonify([reserva.serialize() for reserva in reservas]), 200

@app.route("/traer_reserva/<string:emailUsuario>", methods=["GET"])
def traer_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    reserva_data = {
        'idReserva': reserva.idReserva,
        'cantidadPersonas': reserva.cantidadPersonas,
        'fecha': reserva.fecha.strftime('%Y-%m-%d'),
        'ubicacion': reserva.ubicacion,
        'ocasionEspecial': reserva.ocasionEspecial,
        'emailUsuario': reserva.emailUsuario,
        'telefonoUsuario': reserva.telefonoUsuario,
        'nombreCompletoUsuario': reserva.nombreCompletoUsuario
    }

    return jsonify(reserva_data)


def actualizar_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrado'}), 404

    data = request.json
    reserva.cantidadPersonas = data['cantidadPersonas']
    reserva.fecha = data['fecha']
    reserva.ubicacion = data['ubicacion']
    reserva.ocasionEspecial = data['ocasionEspecial']
    reserva.ocasionEspecialCual = data['ocasionEspecialCual']
    reserva.idUsuario = data['idUsuario']
    reserva.guardar()
    return jsonify({'message': 'Reserva actualizada.'})

def eliminar_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    reserva.eliminar()
    return jsonify({'message': 'Reserva eliminada satisfactoriamente.'})
