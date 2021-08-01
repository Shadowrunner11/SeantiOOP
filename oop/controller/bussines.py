import sqlite3
from sqlite3.dbapi2 import Cursor


class Conexion:
    def __init__(self, query):

        #Aprentemente sqlite3 no cierra la base con el context manager
        """
        with sqlite3.connect(".//model//posDB") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            self.__result = cursor.fetchall()
        """
        try:
            self.conexion = sqlite3.connect(".//model//posDB")
            self.cursor = self.conexion.cursor()
            self.cursor.execute(query)
            self.conexion.commit()
            self.__result = self.cursor.fetchone()
        except:
            print("Ups")
        finally:
            print("finalizando")
            self.conexion.close()
            
            print("la conexion se cerro")
        
    @property        
    def resultado(self):
        return self.__result

    
    



query = "SELECT * FROM usuario"
print(Conexion(query).resultado)

