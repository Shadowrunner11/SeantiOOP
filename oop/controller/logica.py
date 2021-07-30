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
        self.__AppLogin.btnPruebaAction(self.__wrapper)
        self.__AppLogin.mainloop()
        self.__AppLogin.destroy()

    def __wrapper(self) -> None:
        self.__AppLogin.message(self.validarLen(self.__AppLogin.user))

    @staticmethod
    def validarLen(data: dict) -> str:
        bool_val = len(data["Name"]) and len(data["Pass"])
        return "Ingresando" if bool_val else "Datos incorrectos"

    @staticmethod
    def encryptarPass(password: str) -> str:
        return pwd_context.encrypt(password)


controler = Controller()
