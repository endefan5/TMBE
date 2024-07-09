from flask import Flask, jsonify, request
from app.models import Usuario


def index():
    return jsonify({'message': "Bienvenidos a la API de la Taberna de Moe"})


# def crear_usuario():
#     data = request.json
#     nuevo_usuario = Usuario(
#         None, data['usuario'], data['clave'], data['nombre'], data['apellido'], data['email'], data['telefono'])
#     nuevo_usuario.guardar()
#     return jsonify({"message": "Usuario creado satisfactoriamente"}), 201

def crear_usuario():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    nuevo_usuario = Usuario(None, usuario, clave, nombre,
                            apellido, email, telefono)
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
    usuario = Usuario(Usuario.traer_uno(id))
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
    us = Usuario.traer_uno(id)
    if not us:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    Usuario.eliminar()
    return jsonify({'message': 'Usuario satisfactoriamente eliminaado.'})
