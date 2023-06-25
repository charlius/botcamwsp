import mysql.connector

class Connection:
    def __init__(self):
        self.host = 'localhost'
        self.database = "hogarcam"
        self.user = "root"
        self.password = "Cadu@1894"
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def close(self):
        if self.connection:
            self.connection.close()

    def get_connection(self):
        return self.connection

class Comuna:
    def __init__(self, connection):
        self.connection = connection.get_connection()

    def insert(self, nombre_comuna, status):
        query = "INSERT INTO comuna (nombre_comuna, status) VALUES (%s, %s)"
        values = (nombre_comuna, status)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def update(self, id_comuna, nombre_comuna, status):
        query = "UPDATE comuna SET nombre_comuna = %s, status = %s WHERE id_comuna = %s"
        values = (nombre_comuna, status, id_comuna)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all(self):
        query = "SELECT * FROM comuna"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id_comuna):
        query = "SELECT * FROM comuna WHERE id_comuna = %s"
        values = (id_comuna,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()

    def get_by_status(self, status):
        query = "SELECT * FROM comuna WHERE status = %s"
        values = (status,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()


class Poblacion:
    def __init__(self, connection):
        self.connection = connection.get_connection()

    def insert(self, nombre_poblacion, id_comuna, status):
        query = "INSERT INTO poblacion (nombre_poblacion, id_comuna, status) VALUES (%s, %s, %s)"
        values = (nombre_poblacion, id_comuna, status)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def update(self, id_poblacion, nombre_poblacion, id_comuna, status):
        query = "UPDATE poblacion SET nombre_poblacion = %s, id_comuna = %s, status = %s WHERE id_poblacion = %s"
        values = (nombre_poblacion, id_comuna, status, id_poblacion)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all(self):
        query = "SELECT * FROM poblacion"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id_poblacion):
        query = "SELECT * FROM poblacion WHERE id_poblacion = %s"
        values = (id_poblacion,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()

    def get_by_status(self, status):
        query = "SELECT * FROM poblacion WHERE status = %s"
        values = (status,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()


class Familias:
    def __init__(self, connection):
        self.connection = connection.get_connection()

    def insert(self, nombre_familia, direccion, id_poblacion, status):
        query = "INSERT INTO familias (nombre_familia, direccion, id_poblacion, status) VALUES (%s, %s, %s, %s)"
        values = (nombre_familia, direccion, id_poblacion, status)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def update(self, id_familia, nombre_familia, direccion, id_poblacion, status):
        query = "UPDATE familias SET nombre_familia = %s, direccion = %s, id_poblacion = %s, status = %s WHERE id_familia = %s"
        values = (nombre_familia, direccion, id_poblacion, status, id_familia)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all(self):
        query = "SELECT * FROM familias"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id_familia):
        query = "SELECT * FROM familias WHERE id_familia = %s"
        values = (id_familia,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()

    def get_by_status(self, status):
        query = "SELECT * FROM familias WHERE status = %s"
        values = (status,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()


class Integrantes:
    def __init__(self, connection):
        self.connection = connection.get_connection()

    def insert(self, nombre_integrante, telefono, rol, id_familia, status):
        query = "INSERT INTO integrantes (nombre_integrante, telefono, rol, id_familia, status) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre_integrante, telefono, rol, id_familia, status)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def update(self, id_integrante, nombre_integrante, telefono, rol, id_familia, status):
        query = "UPDATE integrantes SET nombre_integrante = %s, telefono = %s, rol = %s, id_familia = %s, status = %s WHERE id_integrante = %s"
        values = (nombre_integrante, telefono, rol, id_familia, status, id_integrante)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all(self):
        query = "SELECT * FROM integrantes"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id_integrante):
        query = "SELECT * FROM integrantes WHERE id_integrante = %s"
        values = (id_integrante,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()

    def get_by_telefono(self, telefono):
        query = "SELECT * FROM integrantes WHERE telefono = %s"
        values = (telefono,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()


class Camaras:
    def __init__(self, connection):
        self.connection = connection.get_connection()

    def insert(self, nombre_camara, url, id_familia, status):
        query = "INSERT INTO camaras (nombre_camara, url, id_familia, status) VALUES (%s, %s, %s, %s)"
        values = (nombre_camara, url, id_familia, status)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def update(self, id_camara, nombre_camara, url, id_familia, status):
        query = "UPDATE camaras SET nombre_camara = %s, url = %s, id_familia = %s, status = %s WHERE id_camara = %s"
        values = (nombre_camara, url, id_familia, status, id_camara)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
        self.connection.commit()

    def get_all(self):
        query = "SELECT * FROM camaras"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, id_camara):
        query = "SELECT * FROM camaras WHERE id_camara = %s"
        values = (id_camara,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()

    def get_by_status(self, status):
        query = "SELECT * FROM camaras WHERE status = %s"
        values = (status,)
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchall()

class ConsultaFamilia:
    def __init__(self, connection):
        self.connection = connection

    def obtener_cameras_por_telefono(self, telefono):
        query = f"""
            SELECT f.nombre_familia, c.nombre_camara, c.url, c.url_video
            FROM familias f
            JOIN camaras c ON f.id_familia = c.id_familia
            JOIN integrantes i ON f.id_familia = i.id_familia
            WHERE i.telefono = '{telefono}'
        """
        self.connection.connect()
        cursor = self.connection.get_connection().cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        self.connection.close()
        # Transformar los resultados a un diccionario
        columnas = ['nombre_familia', 'nombre_camara', 'url', "url_video"]
        resultado_diccionario = []
        for fila in resultados:
            resultado_diccionario.append(dict(zip(columnas, fila)))

        return resultado_diccionario

    def obtener_integrantes_por_telefono(self, telefono):
        query = f"""
            SELECT i.nombre_integrante, i.telefono
            FROM integrantes i
            JOIN familias f ON i.id_familia = f.id_familia
            WHERE f.id_familia = (
                SELECT id_familia
                FROM integrantes
                WHERE telefono = '{telefono}'
            )
        """
        self.connection.connect()
        cursor = self.connection.get_connection().cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        self.connection.close()
        columnas = ['nombre_integrante', 'telefono']
        resultado_diccionario = []
        for fila in resultados:
            resultado_diccionario.append(dict(zip(columnas, fila)))

        return resultado_diccionario


# Uso de las clases

# Crear una instancia de la clase Connection y conectar

# connection = Connection()
# connection.connect()

# consulta = ConsultaFamilia(connection)
# resultado_cameras = consulta.obtener_cameras_por_telefono("56961720045")
# print(resultado_cameras)
# for resultado in resultado_cameras:
#     print(resultado)
# print("\n\n")
# resultado_integrantes = consulta.obtener_integrantes_por_telefono("56961720045")
# for resultado in resultado_integrantes:
#     print(resultado)

# Crear una instancia de la clase Comuna y utilizar los métodos
# comuna = Comuna(connection)
# comuna.insert("lota", "t")
# all_comunas = comuna.get_all()
# for comuna in all_comunas:
#     print(comuna)

# poblacion = Poblacion(connection)
# poblacion.insert("agua fria",1,"t")
# all_poblacions = poblacion.get_all()
# for poblacion in all_poblacions:
#     print(poblacion)

# familias = Familias(connection)
# familias.insert("duran", "viejo a panimavida 25", 1, "t")
# all_familiass = familias.get_all()
# for familias in all_familiass:
#     print(familias)

# integrantes = Integrantes(connection)
# integrantes.insert("carlos", "56961720045", "jefe", 1, "t")
# integrantes.insert("janet", "56998706178", "integrante", 1, "t")
# all_integrantess = integrantes.get_all()
# for integrantes in all_integrantess:
#     print(integrantes)

# camara = Camaras(connection)
# camara.insert( "entrada", "https://rtsp.me/embed/f8RYNNr6/", 1, "t")
# camara.insert( "living", "https://rtsp.me/embed/f8RYNNr6/", 1, "t")
# camara.insert( "patio", "https://rtsp.me/embed/f8RYNNr6/", 1, "t")
# camara.insert( "terraza", "https://rtsp.me/embed/f8RYNNr6/", 1, "t")
# all_camaras = camara.get_all()
# for camara in all_camaras:
#     print(camara)

# connection.close()
