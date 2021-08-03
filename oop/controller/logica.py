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
        print("Inicio")

    def start(self):
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
        if mensaje == "Ingresando":
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
        self.listaId = []
        self.datos = []
        self.RootLogin = Tk()
        self.__AppLogin = login.PointSale(parent=self.RootLogin)
        self.__tabla = self.__AppLogin.treeCatalogo
        self.__boleta = self.__AppLogin.treeBoleta
        self.__AppLogin.actualizar(readProductos(), self.__tabla)
        text = self.__AppLogin.textProduct
        text.trace("w", lambda x, y, z: self.search(text.get()))
        self.__AppLogin.addCommandAdd(self.add)
        self.__AppLogin.addCommandCancel(self.cancel)
        self.__AppLogin.addCommandNuevo(self.addProdAlmacen)
        self.__AppLogin.addCommandVenta(self.wrapperLogis)
        self.__AppLogin.addCommandAlm(self.wrapperLogis2)
        self.__Admin = self.__AppLogin.login
        self.__Admin.accionBtnIngreso(self.permiso)
        self.__Admin.accionBtnBloq(self.bloquear)
        self.__AppLogin.mainloop()
        self.__AppLogin.destroy()

    def wrapperLogis(self):
        self.logistica("-")
        self.cancel()

    def wrapperLogis2(self):
        self.logistica("+")
        self.cancel()

    def search(self, value):

        self.__AppLogin.borrar(self.__tabla)
        self.__AppLogin.actualizar(searchProducto(value), self.__tabla)

    def add(self):

        cant = self.__AppLogin.cantidad.get()
        if cant < 0:
            raise Exception
        for index in self.__AppLogin.getTablaSeleccion(self.__tabla):
            self.datos.append(
                [
                    self.__tabla.item(index)["values"][0],
                    cant,
                    cant * float(self.__tabla.item(index)["values"][1]),
                ]
            )
            self.listaId.append([self.__tabla.item(index)["text"], cant])

        self.__AppLogin.borrar(self.__boleta)
        self.__AppLogin.actualizar(self.datos, self.__boleta)

    def cancel(self):
        self.__AppLogin.borrar(self.__boleta)
        self.listaId = []
        self.datos = []

    def logistica(self, mode: str = "+"):
        for item in self.listaId:
            updateCant(item[0], item[1], mode)
        self.search("")

    def permiso(self):
        mensaje = (
            self.validarBas()
            if Controller().validarLen(self.__Admin.user)
            else "Campos vacios"
        )
        self.__Admin.message(mensaje)
        if mensaje == "Ingresando":
            modif = [
                self.__AppLogin.btnAlm,
                self.__AppLogin.btnDevol,
                self.__AppLogin.btnAlm,
                self.__AppLogin.txtCantidadProd,
                self.__AppLogin.txtNombreProd,
                self.__AppLogin.txtDesProd,
                self.__AppLogin.txtPrecioProd,
                self.__Admin.btnBloquear,
                self.__AppLogin.btnNuevo,
            ]

            for item in modif:
                item.configure(state="normal")

            self.__Admin.txtUser["text"] = ""
        self.__Admin.txtPass["text"] = ""

    def bloquear(self):
        modif = [
            self.__AppLogin.btnAlm,
            self.__AppLogin.btnDevol,
            self.__AppLogin.btnAlm,
            self.__AppLogin.txtCantidadProd,
            self.__AppLogin.txtNombreProd,
            self.__AppLogin.txtDesProd,
            self.__AppLogin.txtPrecioProd,
            self.__Admin.btnBloquear,
            self.__AppLogin.btnNuevo,
        ]

        for item in modif:
            item.configure(state="disabled")
        self.__Admin.labelVerif["text"] = ""

    def validarBas(self):
        dictio = self.__Admin.user
        return validar(dictio["Name"], dictio["Pass"], 1)

    def addProdAlmacen(self):
        try:
            cantidad = self.__AppLogin.cantidadProd.get()
            des = self.__AppLogin.desProd.get()
            precio = self.__AppLogin.precioProd.get()
            nombre = self.__AppLogin.nombreProd.get()

            creatProduct(nombre, precio, cantidad, des)

        except:
            print("No se registro prodcuto")
        self.search("")

if __name__=="__main__":
    controler = Controller().start()
