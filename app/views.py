from flask import request, jsonify, session, abort

from app.models import Reserva
from app.models import Usuario

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
    return jsonify({"message": "Usuario creado satisfactoriamente"}), 201

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

def login(emailUsuario, clave):
    
    if chequearInicioDeSesion():
        return jsonify({'message': 'Ya se encuentra logueado'}), 401
    else:
        usuario = Usuario.buscar_por_email(emailUsuario)
        if usuario and usuario.verificar_contrasena(clave):
            session['idUsuario'] = emailUsuario
            session.modified = True  # Asegura que la sesión se almacene correctamente
            message = f'Login exitoso. idUsuario: {session.get("idUsuario")}'
            return jsonify({'message': message}), 200
        else:
            message = f'Credenciales inválidas. idUsuario: {session.get("idUsuario")}'
            return jsonify({'message': message}), 200
            #return jsonify({'message': 'Credenciales inválidas'}), 401


def logout():
    session.clear()
    message = f'Credenciales inválidas. idUsuario: {session.get("idUsuario")}'
    return jsonify({'message': message}), 200
    #return jsonify({'message': 'Logout exitoso'}), 200

def crear_reserva():
    if 'idUsuario' in session:
        cantidadPersonas = request.form.get("cantidadPersonas")
        fecha = request.form.get("fecha")
        ubicacion = request.form.get("ubicacion")
        ocasionEspecial = request.form.get("ocasionEspecial")
        ocasionEspecialCual = request.form.get("ocasionEspecialCual")
        idUsuario = session['idUsuario']  # Usar el idUsuario almacenado en la sesión

        nueva_reserva = Reserva(
            cantidadPersonas=cantidadPersonas,
            fecha=fecha,
            ubicacion=ubicacion,
            ocasionEspecial=ocasionEspecial,
            ocasionEspecialCual=ocasionEspecialCual,
            idUsuario=idUsuario
        )
        nueva_reserva.guardar()

        return jsonify({"message": "Reserva creada satisfactoriamente"}), 201
    else:
        return jsonify({'message': 'Debes iniciar sesión para realizar esta acción'}), 401


def traer_reservas():
    if chequearInicioDeSesion:
        idUsuario = session.get('idUsuario')  # Obtenemos el idUsuario de la sesión
        reservas = Reserva.traer_todos_por_usuario(idUsuario)
        return jsonify([reserva.serialize() for reserva in reservas]), 200

def traer_reserva(idReserva):
    if chequearInicioDeSesion:
        idUsuario = session.get('idUsuario')  # Obtenemos el idUsuario de la sesión
        reserva = Reserva.traer_uno_por_usuario(idReserva, idUsuario)
        if not reserva:
            return jsonify({'message': 'Reserva no encontrada'}), 404
        return jsonify(reserva.serialize())

def actualizar_reserva(idReserva):
    if chequearInicioDeSesion:
        idUsuario = session.get('idUsuario')  # Obtenemos el idUsuario de la sesión
        reserva = Reserva.traer_uno_por_usuario(idReserva, idUsuario)
        if not reserva:
            return jsonify({'message': 'Reserva no encontrado o no autorizado para modificar'}), 404

    data = request.json
    reserva.cantidadPersonas = data['cantidadPersonas']
    reserva.fecha = data['fecha']
    reserva.ubicacion = data['ubicacion']
    reserva.ocasionEspecial = data['ocasionEspecial']
    reserva.ocasionEspecialCual = data['ocasionEspecialCual']
    reserva.actualizar()
    return jsonify({'message': 'Reserva actualizada.'})

def eliminar_reserva(idReserva):
    if chequearInicioDeSesion:
        idUsuario = session.get('idUsuario')  # Obtenemos el idUsuario de la sesión
        reserva = Reserva.traer_uno_por_usuario(idReserva, idUsuario)
        if not reserva:
            return jsonify({'message': 'Reserva no encontrado o no autorizado para eliminar'}), 404

        reserva.eliminar()
        return jsonify({'message': 'Reserva eliminada satisfactoriamente.'})

def consultaridAlmacenadaEnSesion():
    return 'idUsuario' in session

def chequearInicioDeSesion():
    if session.get("idUsuario") is None:
        resultado = True
    else:
        resultado = False

    return resultado
