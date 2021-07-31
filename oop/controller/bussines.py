import sqlite3
from sqlite3.dbapi2 import Cursor


class Conexion:
    def __init__(self):
        try:
            self.conexion= sqlite3.connect(".//model//posDB")
            self.cursor = self.conexion.cursor()
        except:
            print("Ups")


    def buscar(self, datos: dict)-> 1 or 0:
        try:
            nombre= datos["Name"]
            password= datos["Pass"]
            query = f"SELECT EXISTS (SELECT 1 FROM usuario WHERE nombre='{nombre}' AND password='{password}');"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            print("Ups buscar")

    def buscarUser(self, name: str) ->1 or 0:
        try:
            query = f"SELECT EXISTS (SELECT 1 FROM usuario WHERE nombre='{name}');"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            print("ups buscar user")

    def registrar(self):
        pass
    
    def updatePass(self):
        pass
    
    def deleteUser(self):
        pass

    def close(self):
        self.conexion.close()

"""
con = Conexion().buscar("shadow_11", "123456")
print(con)
"""
