from tkinter import *
from tkinter.font import Font


class Login(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        parentIn = parent
        self.__iniciar(parentIn, "Iniciando")

    def __iniciar(self, parent: Tk, debuggerMessage: str) -> None:

        """
        Introducimos los widgets a la ventana principal
        """

        print(debuggerMessage)

        gap = 8
        bg = "#2b2d42"
        fg1 = "#0a9396"
        fg2 = "#94d2bd"
        fontFam1 = Font(family="Tahoma", size=20, weight="bold")
        fontFam2 = Font(family="Arial", size=15)

        parent.configure(bg=bg)
        parent.title("Login")

        lfUser = LabelFrame(parent, text="Inicio", font=fontFam2, fg=fg2, bg=bg)
        lfUser.pack(padx=gap, pady=gap)

        labelUser = Label(lfUser, text="Usuario", font=fontFam1, fg=fg2, bg=bg)
        labelUser.grid(column=0, row=0, padx=gap, pady=gap)

        self.__txtUser = Entry(lfUser, text="Ingrese su usuario", font=fontFam1)
        self.__txtUser.grid(column=1, row=0, padx=gap, pady=gap)

        labelUser = Label(lfUser, text="Contraseña", font=fontFam1, fg=fg2, bg=bg)
        labelUser.grid(column=0, row=1, padx=gap, pady=gap)

        self.__txtPass = Entry(lfUser, show="*", font=fontFam1)
        self.__txtPass.grid(column=1, row=1, padx=gap, pady=gap)

        self.labelVerif = Label(lfUser, text="", font=fontFam1, fg="#bb3e03", bg=bg)
        self.labelVerif.grid(column=0, row=2, columnspan=2, padx=gap, pady=gap)

        self.__btnPrueba = Button(
            parent, text="Ingresar", font=fontFam1, fg="white", bg=fg1
        )
        self.__btnPrueba.pack(padx=gap, pady=gap)

    @property
    def user(self) -> dict:
        """
        Getter de los datos del usuario
        """
        return {"Name": self.__txtUser.get(), "Pass": self.__txtPass.get()}

    def message(self, text: str) -> None:
        self.labelVerif["text"] = text

    def btnPruebaAction(self, accion) -> None:
        self.__btnPrueba["command"] = accion
