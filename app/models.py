from app.database import get_db_connection

class Reserva:
    def __init__(self, idReserva=None, cantidadPersonas=None, fecha=None, ubicacion=None, ocasionEspecial=None, ocasionEspecialCual=None, emailUsuario=None, telefonoUsuario=None,nombreCompletoUsuario=None):
        self.idReserva = idReserva
        self.cantidadPersonas = cantidadPersonas
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.ocasionEspecial = ocasionEspecial
        self.ocasionEspecialCual = ocasionEspecialCual
        self.emailUsuario = emailUsuario
        self.telefonoUsuario = telefonoUsuario
        self.nombreCompletoUsuario = nombreCompletoUsuario
    def guardar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO reserva (cantidadPersonas, fecha, ubicacion, ocasionEspecial, ocasionEspecialCual, emailUsuario, telefonoUsuario, nombreCompletoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (self.cantidadPersonas, self.fecha, self.ubicacion, self.ocasionEspecial, self.ocasionEspecialCual, self.emailUsuario, self.telefonoUsuario, self.nombreCompletoUsuario)
        )
        db.commit()
        cursor.close()

    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM reserva")
        registros = cur.fetchall()
        reservas = []
        for registro in registros:
            reservas.append(Reserva(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8]))
        cur.close()
        return reservas

    @staticmethod
    def traer_uno(emailUsuario):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reserva WHERE emailUsuario=%s", (emailUsuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(idReserva=row[0], cantidadPersonas=row[1], fecha=row[2], ubicacion=row[3], ocasionEspecial=row[4], ocasionEspecialCual=row[5], idUsuario=row[6], idUsuario=row[7], idUsuario=row[8])
        return None

    def eliminar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reserva WHERE idReserva=%s", (self.emailUsuario,))
        db.commit()
        cursor.close()


    def serialize(self):
        return {
            'idReserva': self.idReserva,
            'cantidadPersonas': self.cantidadPersonas,
            'fecha': self.fecha.isoformat(),  # Formatear la fecha si es necesario
            'ubicacion': self.ubicacion,
            'ocasionEspecial': self.ocasionEspecial,
            'ocasionEspecialCual': self.ocasionEspecialCual,
            'emailUsuario': self.emailUsuario,
            'telefonoUsuario': self.telefonoUsuario,
            'nombreCompletoUsuario': self.nombreCompletoUsuario,
            # Añadir más campos si es necesario
        }