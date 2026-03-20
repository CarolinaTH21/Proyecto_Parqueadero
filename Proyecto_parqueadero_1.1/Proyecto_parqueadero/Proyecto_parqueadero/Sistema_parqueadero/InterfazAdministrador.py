import tkinter as tk
from tkinter import ttk
from Parqueadero import Parqueadero


class InterfazAdministrador:

    def __init__(self, sistema):

        self.sistema = sistema

        self.ventana = tk.Toplevel()
        self.ventana.title("Panel Administrador")
        self.ventana.geometry("600x600")

        canvas = tk.Canvas(self.ventana)
        scrollbar = tk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)

        self.frame = tk.Frame(canvas)

        self.frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(self.frame, text="Nombre Parqueadero").pack()
        self.nombre = tk.Entry(self.frame)
        self.nombre.pack()

        tk.Label(self.frame, text="Ubicación").pack()
        self.ubicacion = tk.Entry(self.frame)
        self.ubicacion.pack()

        tk.Label(self.frame, text="Capacidad").pack()
        self.capacidad = tk.Entry(self.frame)
        self.capacidad.pack()

        tk.Button(self.frame, text="Crear parqueadero",
                  command=self.crear).pack()

        tk.Button(self.frame, text="Modificar parqueadero",
                  command=self.modificar).pack()

        tk.Label(self.frame, text="Placa salida").pack()
        self.placa = tk.Entry(self.frame)
        self.placa.pack()

        tk.Button(self.frame, text="Registrar salida",
                  command=self.salida).pack()

        tk.Button(self.frame, text="Actualizar tablas",
                  command=self.actualizar).pack(pady=10)

        self.mensaje = tk.Label(self.frame, text="", fg="blue")
        self.mensaje.pack()

        self.tablas_frame = tk.Frame(self.frame)
        self.tablas_frame.pack()

    def limpiar(self):

        self.nombre.delete(0, tk.END)
        self.ubicacion.delete(0, tk.END)
        self.capacidad.delete(0, tk.END)

    def crear(self):

        p = Parqueadero(
            self.nombre.get(),
            self.ubicacion.get(),
            int(self.capacidad.get())
        )

        self.sistema.agregar_parqueadero(p)

        frame = tk.LabelFrame(self.tablas_frame, text=p.nombre)
        frame.pack(pady=10)

        tabla = ttk.Treeview(frame)

        tabla["columns"] = ("placa", "tipo", "puesto", "prioridad")

        for col in tabla["columns"]:
            tabla.heading(col, text=col)

        tabla.pack()

        p.tabla = tabla

        p.actualizar_tabla()

        self.mensaje.config(text="Parqueadero creado correctamente")

        self.limpiar()

    def modificar(self):

        nombre = self.nombre.get()

        for p in self.sistema.parqueaderos:

            if p.nombre == nombre:

                p.ubicacion = self.ubicacion.get()
                p.capacidad = int(self.capacidad.get())

                self.mensaje.config(
                    text="Parqueadero modificado correctamente")

        self.limpiar()

    def salida(self):

        placa = self.placa.get()

        for p in self.sistema.parqueaderos:

            vehiculo = p.retirar_vehiculo(placa)

            if vehiculo:

                self.mensaje.config(
                    text="Vehículo eliminado. Presione ACTUALIZAR TABLAS")

                self.placa.delete(0, tk.END)

                return

        self.mensaje.config(text="No se encontró esa placa")

        self.placa.delete(0, tk.END)

    def actualizar(self):

        for p in self.sistema.parqueaderos:
            p.actualizar_tabla()

        self.mensaje.config(text="Tablas actualizadas")