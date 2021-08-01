from tkinter import *
from tkinter.font import Font


class Login(Frame):
    cont = 0

    def __init__(self, parent=None):
        super(Login,self).__init__(parent)
        self.parentIn = parent
        self.__iniciar(self.parentIn, "Iniciando")

    def __iniciar(self, parent: Tk, debuggerMessage: str) -> None:
        """
        Introducimos los widgets a la ventana principal
        """
        print(debuggerMessage)

        self.gap = 8
        self.bg = "#011627"
        self.fg1 = "#003566"
        self.fg2 = "#fff"
        self.fontFam1 = Font(family="Tahoma", size=20, weight="bold")
        self.fontFam2 = Font(family="Arial", size=15)

        parent.configure(bg=self.bg)
        parent.title("Login")

        self.toggleTheme = Button(parent, command=self.cambiarColor)
        self.toggleTheme.grid(column=0, row=0, sticky="W", padx=self.gap, pady=self.gap)

        self.__lfUser = LabelFrame(
            parent, text="Inicio", font=self.fontFam2, fg=self.fg2, bg=self.bg
        )
        self.__lfUser.grid(column=0, row=1, columnspan=2, padx=self.gap, pady=self.gap)

        self.labelUser = Label(
            self.__lfUser, text="Usuario", font=self.fontFam1, fg=self.fg2, bg=self.bg
        )
        self.labelUser.grid(column=0, row=0, padx=self.gap, pady=self.gap)

        self.__txtUser = Entry(
            self.__lfUser, text="Ingrese su usuario", font=self.fontFam1
        )
        self.__txtUser.grid(column=1, row=0, padx=self.gap, pady=self.gap)

        self.labelContra = Label(
            self.__lfUser,
            text="Contraseña",
            font=self.fontFam1,
            fg=self.fg2,
            bg=self.bg,
        )
        self.labelContra.grid(column=0, row=1, padx=self.gap, pady=self.gap)

        self.__txtPass = Entry(self.__lfUser, show="*", font=self.fontFam1)
        self.__txtPass.grid(column=1, row=1, padx=self.gap, pady=self.gap)

        self.labelVerif = Label(
            self.__lfUser, text="", font=self.fontFam1, fg="#bb3e03", bg=self.bg
        )
        self.labelVerif.grid(
            column=0, row=2, columnspan=2, padx=self.gap, pady=self.gap
        )

        self.__btnIngresar = Button(
            parent, text="Ingresar", font=self.fontFam1, fg="white", bg=self.fg1
        )
        self.__btnIngresar.grid(
            column=0, row=2, padx=self.gap, pady=self.gap, sticky="WE"
        )

        self.__btnRegistrar = Button(
            parent,
            text="Nuevo",
            font=self.fontFam1,
            fg="white",
            bg=self.fg1,
            command=self.accionBtnRegistro,
        )
        self.__btnRegistrar.grid(
            column=1, row=2, padx=self.gap, pady=self.gap, sticky="WE"
        )

    @property
    def user(self) -> dict:
        """
        Getter de los datos del usuario
        """
        return {"Name": self.__txtUser.get(), "Pass": self.__txtPass.get()}

    def message(self, text: str) -> None:
        self.labelVerif["text"] = text

    def accionBtnIngreso(self, accion) -> None:
        self.__btnIngresar["command"] = accion

    def accionBtnRegistro(self) -> None:
        self.__lfUser["text"] = "Registro"
        labelContra2 = Label(
            self.__lfUser, text="Confirmar", font=self.fontFam1, fg=self.fg2, bg=self.bg
        )
        labelContra2.grid(column=0, row=2, padx=self.gap, pady=self.gap)

        self.__txtPass2 = Entry(self.__lfUser, show="*", font=self.fontFam1)
        self.__txtPass2.grid(column=1, row=2, padx=self.gap, pady=self.gap)

        self.labelVerif.grid(column=0, row=3)

    def cambiarColor(self) -> None:
        lista = [
            self.parentIn,
            self.labelVerif,
            self.labelUser,
            self.__lfUser,
            self.labelContra,
        ]
        self.cont += 1
        new_bg = "#086375" if self.cont % 2 else self.bg
        self.toogle(lista, new_bg)

    @staticmethod
    def toogle(lista: list, back: str) -> None:
        for e in lista:
            e.configure(bg=back)
