import tkinter as tk
from InterfazUsuario import InterfazUsuario
from InterfazAdministrador import InterfazAdministrador


class InterfazPrincipal:

    def __init__(self, sistema):

        self.sistema = sistema

        self.ventana = tk.Tk()

        self.ventana.title("Sistema de Parqueaderos")

        self.ventana.geometry("500x350")

        titulo = tk.Label(
            self.ventana,
            text="Sistema de Gestión de Parqueaderos",
            font=("Arial", 16)
        )

        titulo.pack(pady=30)

        boton_usuario = tk.Button(
            self.ventana,
            text="Usuario",
            width=20,
            height=2,
            command=self.usuario
        )

        boton_usuario.pack(pady=10)

        boton_admin = tk.Button(
            self.ventana,
            text="Administrador",
            width=20,
            height=2,
            command=self.admin
        )

        boton_admin.pack(pady=10)

    def usuario(self):

        InterfazUsuario(self.sistema)

    def admin(self):

        InterfazAdministrador(self.sistema)

    def ejecutar(self):

        self.ventana.mainloop()