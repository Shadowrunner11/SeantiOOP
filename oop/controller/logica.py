from bussines import Conexion
from passlib.context import CryptContext
from tkinter import Tk
from view import login

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)


class Controller:
    def __init__(self):
        RootLogin = Tk()
        self.__AppLogin = login.Login(parent=RootLogin)
        self.__AppLogin.accionBtnIngreso(self.__wrapper)
        self.__AppLogin.mainloop()
        self.__AppLogin.destroy()

    def __wrapper(self) -> None:
        mensaje = (
            self.validarBas()
            if self.validarLen(self.__AppLogin.user)
            else "Campos vacios"
        )

        self.__AppLogin.message(mensaje)

    def validarBas(self) -> str:
        con = Conexion()
        dictio = self.__AppLogin.user

        flag1 = con.buscarUser(dictio["Name"])

        if flag1:
            flag2 = con.buscar(dictio)
            con.close()
            return "Bienvenido" if flag2 else "Cotraseña incorrecta"

        con.close()
        return "No existe el usuario"

    @staticmethod
    def validarLen(data: dict) -> bool:

        return len(data["Name"]) and len(data["Pass"])

    @staticmethod
    def encryptarPass(password: str) -> str:
        return pwd_context.encrypt(password)


controler = Controller()
