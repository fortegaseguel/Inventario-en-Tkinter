from .connect import ConnectDB
from tkinter import messagebox


# CREAR TABLA EN LA BASE DE DATOS
def crear_tabla():
    connect = ConnectDB()

    sql = """
    CREATE TABLE productos(
        id INTEGER, 
        nombre VARCHAR(100),
        cantidad VARCHAR(10),
        categoria VARCHAR(100),
        PRIMARY KEY(id AUTOINCREMENT)
    )
    """

    try:
        connect.cursor.execute(sql)
        connect.close()

        titulo = 'Creacion de Base de Datos'
        msg = 'Base de datos creada correctamente'
        messagebox.showinfo(titulo, msg)

    except:
        titulo = 'Creacion de Base de Datos'
        msg = 'La base de datos ya ha sido creada'
        messagebox.showwarning(titulo, msg)

# BORRAR TABLA DE LA BASE DE DATOS
def borrar_tabla():
    connect = ConnectDB()

    sql = """
    DROP TABLE productos
    """

    try:
        connect.cursor.execute(sql)
        connect.close()

        titulo = 'Borrar Base de Datos'
        msg = 'Base de datos se ha eliminado correctamente'
        messagebox.showinfo(titulo, msg)

    except:
        titulo = 'Borrar Base de Datos'
        msg = 'La base de datos no existe'
        messagebox.showerror(titulo, msg)


# Clase con el mismo nombre de la tabla creada. Esta parte es para crear registros desde la aplicacion
class Table:
    def __init__(self, nombre, duracion, genero):
        self.id = None
        self.nombre = nombre
        self.cantidad = duracion
        self.categoria = genero
    
    def __str__(self):
        return f'Tabla[{self.nombre}, {self.cantidad}, {self.categoria}]'


#Guardar registros en la base de datos
def guardar(registro):
    connect = ConnectDB()

    sql = f"""
    INSERT INTO productos(nombre, cantidad, categoria)
    VALUES('{registro.nombre}', '{registro.cantidad}', '{registro.categoria}')
    """

    try:
        connect.cursor.execute(sql)
        connect.close()

        titulo = 'Agregar nuevo registro'
        msg = 'El dato se ha guardado correctamente'
        messagebox.showinfo(titulo, msg)

    except:
        titulo = 'Borrar Registro'
        msg = 'La base de datos no existe'
        messagebox.showerror(titulo, msg)


# MOTRAR DATOS DE LA BASE DE DATOS
def listar():
    connect = ConnectDB()

    lista = []

    sql = """
    SELECT * FROM productos
    """

    try:
        connect.cursor.execute(sql)
        lista = connect.cursor.fetchall()
        connect.close()

    except:
        titulo = 'Conexion al Registro'
        msg = 'La base de datos no existe'
        messagebox.showwarning(titulo, msg)

    return lista


# EDITAR/UPDATE EN LA BASE DE DATOS
def editar(registro, id):
    connect = ConnectDB()

    sql = f"""
    UPDATE productos
    SET nombre = '{registro.nombre}',
    cantidad = '{registro.cantidad}',
    categoria = '{registro.categoria}'
    WHERE id = {id}
    """

    try:
        connect.cursor.execute(sql)
        connect.close()

    except:
        titulo = 'Edicion de Registros'
        msg = 'No se ha podido editar el registro'
        messagebox.showerror(titulo, msg)

# ELIMINAR REGISTRO
def eliminar(id):
    connect = ConnectDB()

    sql = f"""
    DELETE FROM productos
    WHERE id = {id}
    """

    try:
        connect.cursor.execute(sql)
        connect.close()

    except:
        titulo = 'Eliminar Registros'
        msg = 'No se ha podido eliminar el registro'
        messagebox.showerror(titulo, msg)