import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def desconectar(self):
        self.connection.close()

    def ejecutar_query(self, query, values=None):
        self.conectar()
        cursor = self.connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        self.connection.commit()
        self.desconectar()
        return result


class BaseModel:
    def __init__(self, conexion):
        self.conexion = conexion
        self.table_name = ''

    def guardar(self, data):
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.conexion.ejecutar_query(query, values)

    def editar(self, data, where):
        set_values = ', '.join([f"{key}=%s" for key in data.keys()])
        values = tuple(data.values())
        where_clause = ' AND '.join([f"{key}=%s" for key in where.keys()])
        where_values = tuple(where.values())
        query = f"UPDATE {self.table_name} SET {set_values} WHERE {where_clause}"
        self.conexion.ejecutar_query(query, values + where_values)

    def obtener_todos(self):
        query = f"SELECT * FROM {self.table_name}"
        result = self.conexion.ejecutar_query(query)
        return result


class Poblacion(BaseModel):
    def __init__(self, conexion):
        super().__init__(conexion)
        self.table_name = 'poblacion'


class Familia(BaseModel):
    def __init__(self, conexion):
        super().__init__(conexion)
        self.table_name = 'familias'


class Usuario(BaseModel):
    def __init__(self, conexion):
        super().__init__(conexion)
        self.table_name = 'usuarios'


class Camara(BaseModel):
    def __init__(self, conexion):
        super().__init__(conexion)
        self.table_name = 'camaras'


class Proceso(BaseModel):
    def __init__(self, conexion):
        super().__init__(conexion)
        self.table_name = 'procesos'