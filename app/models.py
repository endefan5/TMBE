from app.database import get_db_connection
# from mysql.connector import connect  # borrame


class Usuario:
    def __init__(self, id=None, usuario=None, clave=None, nombre=None, apellido=None, email=None, telefono=None):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def guardar(self):
        db = get_db_connection()
        cur = db.cursor()
        if self.id:
            cur.execute("UPDATE usuario SET (clave=%s,nombre=%s,apellido=%s,email=%s,telefono=%s WHERE id=%s",
                        (self.usuario, self.clave, self.nombre, self.apellido, self.email, self.telefono))
        else:
            cur.execute(
                "INSERT INTO usuario (usuario, clave, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)", (self.usuario, self.clave, self.nombre, self.apellido, self.email, self.telefono))

        db.commit()
        cur.close()

    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM usuario")
        registros = cur.fetchall()
        usuarios = list()
        for registro in registros:
            usuarios.append(Usuario(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))

        cur.close()
        return usuarios

    def serialize(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'clave': self.clave,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono
        }


# con = connect(host="localhost", port=3306, user="root",
#               password="", database="proycodoacodo")
# cur = con.cursor()
# tupla = ("PRUEBA", "P123", "DDS", "SFDFG", "odkfod@fdkofd.com", 3597)
# cur.execute("INSERT INTO usuario (usuario, clave, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)", tupla)

# con.commit()
# con.close()
