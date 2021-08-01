import sqlite3


class Conexion:
    # Aprentemente si se cierra pero puedo volve ra ejecutar conexion por algun motivo

    def __init__(self):
        self.__result = []
        

    def start(self, query):
       #try:
        with sqlite3.connect(".//model//posDB") as conexion:
            self.__result = conexion.execute(query).fetchall()
            conexion.commit()
        conexion.close()
        #es necesario?
        del conexion
        return self
        #except:
            #print("ups") 

    @property
    def resultado(self):
        return self.__result
    
    def __del__(self):
        print("Conexion destruida")


def create(tabla: str, first, *arg):    
    values = f"'{first}'" if type(first)==str else f"{first}"
    for i in arg:
        if type(i)==str:
            values +=f", '{i}'"
        else:
            values +=f", {i}"

    query = f"INSERT INTO {tabla} VALUES ({values})"
    print (query)
    Conexion().start(query)


def createUser(name: str, password:str):
    create("usuario", name, password)

def updateUser(name: str, newPass: str):
    query = f"UPDATE usuario SET password='{newPass}' WHERE nombre='{name}';"
    Conexion().start(query)


def delete():
    pass


def read(tabla):
    query = f"SELECT * FROM {tabla}"
    return Conexion().start(query).resultado


def searchUser(name : str)-> 1 or 0:
    query = f"SELECT * FROM usuario WHERE EXISTS (SELECT 1  FROM usuario WHERE nombre='{name}')"
    return Conexion().start(query).resultado


def searchUserPass():
    pass


query = "SELECT * FROM usuario"
query2 = "INSERT INTO usuario VALUES ('usuario7', 'clave7')"
#createUser("prueba", "prueba")
#updateUser("prueba", "clavetest")
searchUser("shadow_11")
