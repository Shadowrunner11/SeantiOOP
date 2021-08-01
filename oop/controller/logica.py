from bussines import *
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
        
        self.RootLogin = Tk()
        self.__AppLogin = login.Login(parent=self.RootLogin)
        self.__AppLogin.accionBtnIngreso(self.__wrapper)
        self.__AppLogin.accionBtnRegNew(self.___wrapper2)
        self.__AppLogin.mainloop()
        self.__AppLogin.destroy()

    def __wrapper(self) -> None:
        
        mensaje = (
            self.validarBas()
            if self.validarLen(self.__AppLogin.user)
            else "Campos vacios"
        )

        self.__AppLogin.message(mensaje)
        if mensaje =="Ingresando":
            self.RootLogin.destroy()
            Controller2()

    def ___wrapper2(self) -> None:
        dictio = self.__AppLogin.newUser
        mensaje = "Campos incompletos"
        if self.validarLen(dictio):
            mensaje = (
                createUser(dictio["Name"], dictio["Pass"])
                if self.validarNew()
                else "No coinciden las contraseñas"
            )

        self.__AppLogin.message(mensaje)

    def validarBas(self) -> str:
        dictio = self.__AppLogin.user
        return validar(dictio["Name"], dictio["Pass"])

    def validarNew(self) -> bool:
        dictio = self.__AppLogin.newUser
        return dictio["Pass"] == dictio["NPass"]

    @staticmethod
    def validarLen(karg: dict) -> bool:
        flag = True
        for value in karg.values():
            flag = len(value) > 0

        return flag

    @staticmethod
    def encryptarPass(password: str) -> str:
        return pwd_context.encrypt(password)
        
class Controller2:
    def __init__(self):
            
        self.RootLogin = Tk()
        self.__AppLogin = login.PointSale(parent=self.RootLogin)
        self.__AppLogin.mainloop()
        self.__AppLogin.destroy()

controler = Controller()
