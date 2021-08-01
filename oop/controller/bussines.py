import sqlite3


class Conexion:
    # Aprentemente si se cierra pero puedo volve ra ejecutar conexion por algun motivo

    def __init__(self):
        self.__result = []

    def start(self, query):
        # try:
        with sqlite3.connect(".//model//posDB") as conexion:
            self.__result = conexion.execute(query).fetchall()
            conexion.commit()
        conexion.close()
        # es necesario?
        del conexion
        return self
        # except:
        # print("ups")

    @property
    def resultado(self):
        return self.__result

    def __del__(self):
        print("Conexion destruida")


def create(tabla: str, first, *arg):
    values = f"'{first}'" if type(first) == str else f"{first}"
    for i in arg:
        if type(i) == str:
            values += f", '{i}'"
        else:
            values += f", {i}"

    query = f"INSERT INTO {tabla} VALUES ({values})"
    Conexion().start(query)


def createUser(name: str, password: str) -> str:
    try:
        create("usuario", name, password)
        return "Creando usuario"
    except:
        return "Usuario ya existe"


def updateUser(name: str, newPass: str):
    query = f"UPDATE usuario SET password='{newPass}' WHERE nombre='{name}';"
    Conexion().start(query)


def delete():
    pass


def read(tabla):
    query = f"SELECT * FROM {tabla}"
    return Conexion().start(query).resultado


def searchUser(name: str) -> 1 or 0:
    query = f"SELECT EXISTS (SELECT 1 FROM usuario WHERE nombre='{name}')"
    return Conexion().start(query).resultado[0][0]


def searchUserPass(name: str, password: str):
    query = f"SELECT EXISTS (SELECT 1 FROM usuario WHERE nombre='{name}' AND password='{password}')"
    return Conexion().start(query).resultado[0][0]


def validar(name: str, password: str) -> str:
    if searchUser(name):
        return (
            "Ingresando" if searchUserPass(name, password) else "Contraseña incorrecta"
        )
    return "No existe este usuario"
