from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from typing import ItemsView


class Login(Frame):
    cont = 0

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.parentIn = parent
        self.__iniciar(self.parentIn, "Iniciando")

    def __iniciar(self, parent: Tk, debuggerMessage: str) -> None:
        """
        Introducimos los widgets a la ventana principal
        """
        print(debuggerMessage)

        self.gap = 8
        self.bg = "#101010"
        self.fg1 = "#003566"
        self.fg2 = "#fff"
        self.fontFam1 = Font(family="Tahoma", size=17, weight="bold")
        self.fontFam2 = Font(family="Arial", size=15)

        parent.configure(bg=self.bg)
        parent.title("Login")

        self.toggleTheme = Button(parent, command=self.cambiarColor)
        self.toggleTheme.grid(column=0, row=0, sticky="W", padx=self.gap, pady=self.gap)

        mode = IntVar()

        """
        self.labelSelect = Label(parent, bg=self.bg)
        self.labelSelect.grid(column=1, row=0)

        self.radioVender = Radiobutton(self.labelSelect, variable=mode, value =1, text="Vendedor", bg=self.bg, fg=self.fg2)
        self.radioVender.grid(column=0, row =0)

        self.radioAdmin = Radiobutton(self.labelSelect, variable=mode, value = 2, text= "Admin", bg=self.bg, fg=self.fg2)
        self.radioAdmin.grid(column=1, row= 0)

        """
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

        self.__btnRegisNew = Button(
            parent,
            text="Registrar",
            font=self.fontFam1,
            fg="white",
            bg=self.fg1,
        )
        self.__btnRegresar = Button(
            parent,
            text="Regresar",
            font=self.fontFam1,
            fg="white",
            bg=self.fg1,
            command=self.regresar,
        )
        self.lista = [
            self.parentIn,
            self.labelVerif,
            self.labelUser,
            self.__lfUser,
            self.labelContra,
            
        ]
        self.listabtn = [
            self.__btnRegisNew,
            self.__btnRegistrar,
            self.__btnIngresar,
            self.__btnRegresar,
        ]
        self.listalabel = [
            self.labelContra,
            self.labelUser,
            self.labelUser,
            self.__lfUser,
            
        ]

    @property
    def user(self) -> dict:
        """
        Getter de los datos del usuario
        """
        return {"Name": self.__txtUser.get(), "Pass": self.__txtPass.get()}

    @property
    def newUser(self) -> dict:
        return {
            "Name": self.__txtUser.get(),
            "Pass": self.__txtPass.get(),
            "NPass": self.__txtPass2.get(),
        }

    def message(self, text: str) -> None:
        self.labelVerif["text"] = text

    def accionBtnIngreso(self, accion) -> None:
        self.__btnIngresar["command"] = accion

    def accionBtnRegNew(self, accion) -> None:
        self.__btnRegisNew["command"] = accion

    def accionBtnRegistro(self) -> None:
        self.labelVerif["text"] = ""
        self.__btnIngresar.grid_remove()
        self.__btnRegistrar.grid_remove()
        self.__btnRegisNew.grid(column=0, row=2, sticky="WE", padx=self.gap)
        self.__btnRegresar.grid(column=1, row=2, sticky="WE", padx=self.gap)
        self.__lfUser["text"] = "Registro"
        new_bg = "#f3f3f3" if self.cont % 2 else self.bg
        new_fg = "#12aaff" if self.cont % 2 else self.fg2
        self.labelContra2 = Label(
            self.__lfUser, text="Confirmar", font=self.fontFam1, fg=new_fg, bg=new_bg
        )
        self.labelContra2.grid(column=0, row=2, padx=self.gap, pady=self.gap)
        self.lista.append(self.labelContra2)
        self.listalabel.append(self.labelContra2)

        self.__txtPass2 = Entry(self.__lfUser, show="*", font=self.fontFam1)
        self.__txtPass2.grid(column=1, row=2, padx=self.gap, pady=self.gap)

        self.labelVerif.grid(column=0, row=3)

    def cambiarColor(self) -> None:
        self.labelVerif["text"] = ""
        self.cont += 1
        new_bg = "#f3f3f3" if self.cont % 2 else self.bg
        new_fg = "#12aaff" if self.cont % 2 else self.fg2
        self.toogle(self.lista, new_bg)
        self.toogleFont(self.listalabel, new_fg)
        self.toogleFont(self.listabtn, new_fg)

    @staticmethod
    def toogle(lista: list, back: str) -> None:
        for e in lista:
            e.configure(bg=back)

    @staticmethod
    def toogleFont(lista: list, back: str) -> None:
        for e in lista:
            e.configure(fg=back)

    def regresar(self):
        self.labelVerif["text"] = ""
        self.labelContra2.grid_remove()
        self.__txtPass2.grid_remove()
        self.__btnRegisNew.grid_remove()
        self.__btnRegresar.grid_remove()
        self.__btnIngresar.grid()
        self.__btnRegistrar.grid()

class PointSale(Frame):
    def __init__(self, parent=None):
        super(PointSale, self).__init__(parent)
        self.parentIn = parent
        self.__iniciar(self.parentIn, "Iniciando")

    def __iniciar(self, parent: Tk, debuggerMessage: str) -> None:
        """
        Introducimos los widgets a la ventana principal
        """
        print(debuggerMessage)
        self.gap = 8
        self.bg = "#101010"
        self.fg1 = "#003566"
        self.fg2 = "#fff"
        self.fontFam1 = Font(family="Tahoma", size=17, weight="bold")
        self.fontFam2 = Font(family="Arial", size=15)

        #parent.configure(bg=self.bg)
        parent.title("Teletubies SAC")

        self.frVender = Frame(parent)
        self.frVender.pack(side="left", fill=BOTH)

        self.lblFrBuscar = LabelFrame(self.frVender, text="Buscar")
        self.lblFrBuscar.pack()
        
        
        self.lblFiltro =Label(self.lblFrBuscar, text="Filtrar")
        self.lblFiltro.grid(column=0,row=0, sticky="w")
        
        self.filtro =IntVar()
        self.radioNombre = Radiobutton(self.lblFrBuscar, text ="Nombre", variable=self.filtro, value = 1)
        self.radioNombre.grid(column=0, row=1, sticky="w")

        self.radioId = Radiobutton(self.lblFrBuscar, text="Codigo", variable=self.filtro, value=2)
        self.radioId.grid(column=1, row=1)
       
        
        #self.lblProduct = Label(self.lblFrBuscar, text="Producto")
        #self.lblProduct.grid(column=0, row=0)

        self.txtProduct = Entry(self.lblFrBuscar)
        self.txtProduct.grid(column=0, row=2, columnspan=2, sticky="we")

        self.btnSearch = Button(self.lblFrBuscar)
        self.btnSearch.grid(column=2, row =2)

        self.frAdd = LabelFrame(self.frVender, text="cantidad")
        self.frAdd.pack(expand=1)

        self.txtAdd = Entry(self.frAdd)
        self.txtAdd.grid(column=0, row=0)

        self.btnAdd =Button(self.frAdd)
        self.btnAdd.grid(column=1, row=0)

        self.treeBoleta = ttk.Treeview(self.frVender)
        self.treeBoleta.pack(fill=BOTH)

        self.frOpciones = Frame(self.frVender)
        self.frOpciones.pack(expand=1)

        self.btnAceptar = Button(self.frOpciones, text="ACEPTAR")
        self.btnAceptar.grid(column=0, row =0, sticky=W+E)

        self.btnCancel = Button(self.frOpciones, text="CANCELAR")
        self.btnCancel.grid(column=1, row =0, sticky=W+E)

        self.treeCatalogo = ttk.Treeview(parent, columns=["0", "1", "2", "3"])
        self.treeCatalogo.pack(expand=1, fill=BOTH)
        
    def actualizar(self, datos):
        cant = len(datos)
        for i in range(cant):
            item=self.treeCatalogo.insert("",i,text=datos[i][0])
            for j in range(4):
                self.treeCatalogo.set(item, f"{j}", f"{datos[i][j+1]}")
        

        