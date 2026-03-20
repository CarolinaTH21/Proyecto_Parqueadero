import tkinter as tk
from Vehiculo import Vehiculo
from Reserva import Reserva


class InterfazUsuario:

    def __init__(self, sistema):

        self.sistema = sistema

        self.ventana = tk.Toplevel()
        self.ventana.title("Registro Usuario")
        self.ventana.geometry("420x520")

        # Canvas para scroll
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

        tk.Label(self.frame, text="Placa").pack()
        self.placa = tk.Entry(self.frame)
        self.placa.pack()

        tk.Label(self.frame, text="Tipo vehículo").pack()

        self.tipo = tk.StringVar(value="Carro")

        tk.Radiobutton(self.frame, text="Carro",
                       variable=self.tipo, value="Carro",
                       command=self.actualizar_tipo).pack()

        tk.Radiobutton(self.frame, text="Motocicleta",
                       variable=self.tipo, value="Motocicleta",
                       command=self.actualizar_tipo).pack()

        self.casco = tk.IntVar()

        self.check_casco = tk.Checkbutton(
            self.frame,
            text="Dejar casco",
            variable=self.casco
        )
        self.check_casco.pack()

        tk.Label(self.frame, text="Nombre").pack()
        self.nombre = tk.Entry(self.frame)
        self.nombre.pack()

        tk.Label(self.frame, text="Identificación").pack()
        self.identificacion = tk.Entry(self.frame)
        self.identificacion.pack()

        tk.Label(self.frame, text="Teléfono").pack()
        self.telefono = tk.Entry(self.frame)
        self.telefono.pack()

        tk.Label(self.frame, text="Ubicación").pack()
        self.ubicacion = tk.Entry(self.frame)
        self.ubicacion.pack()

        self.prioridad = tk.IntVar()

        tk.Checkbutton(self.frame,
                       text="Reserva prioritaria",
                       variable=self.prioridad).pack()

        tk.Button(self.frame,
                  text="Registrar solicitud",
                  command=self.registrar).pack(pady=5)

        self.resultado = tk.Label(self.frame, text="", fg="green")
        self.resultado.pack(pady=10)

        self.opciones_frame = tk.Frame(self.frame)
        self.opciones_frame.pack()

    def limpiar_campos(self):

        self.placa.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.identificacion.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
        self.ubicacion.delete(0, tk.END)

        self.prioridad.set(0)
        self.casco.set(0)

    def limpiar_resultado(self):

        self.resultado.config(text="")

    def actualizar_tipo(self):

        if self.tipo.get() == "Carro":
            self.check_casco.config(state="disabled")
        else:
            self.check_casco.config(state="normal")

    def registrar(self):

        self.vehiculo = Vehiculo(
            self.placa.get(),
            self.tipo.get(),
            self.nombre.get(),
            self.identificacion.get(),
            self.telefono.get(),
            self.casco.get()
        )

        self.reserva = Reserva(self.vehiculo, self.prioridad.get())

        disponibles = self.sistema.buscar_parqueaderos_disponibles(
            self.ubicacion.get())

        if len(disponibles) == 0:

            self.resultado.config(
                text="No hay parqueaderos disponibles")

            self.ventana.after(4000, self.limpiar_resultado)

            return

        if len(disponibles) == 1:

            self.asignar_parqueadero(disponibles[0])

        else:

            self.mostrar_opciones(disponibles)

    def mostrar_opciones(self, parqueaderos):

        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        tk.Label(
            self.opciones_frame,
            text="Parqueadero cercano lleno.\nSeleccione otro disponible:"
        ).pack()

        for p in parqueaderos:

            tk.Button(
                self.opciones_frame,
                text=p.nombre,
                command=lambda parque=p: self.asignar_parqueadero(parque)
            ).pack(pady=2)

        tk.Button(
            self.opciones_frame,
            text="Cancelar solicitud",
            command=self.cancelar
        ).pack(pady=5)

    def asignar_parqueadero(self, parqueadero):

        vehiculo = parqueadero.ingresar_vehiculo(self.reserva)

        texto = f"""
Solicitud registrada

Nombre: {vehiculo.nombre}
Placa: {vehiculo.placa}

Parqueadero: {parqueadero.nombre}
Puesto asignado: {vehiculo.puesto}
"""

        if vehiculo.casillero:
            texto += f"\nCasillero casco: {vehiculo.casillero}"

        self.resultado.config(text=texto)

        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        self.limpiar_campos()

        self.ventana.after(5000, self.limpiar_resultado)

    def cancelar(self):

        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        self.resultado.config(text="Solicitud cancelada")

        self.limpiar_campos()

        self.ventana.after(3000, self.limpiar_resultado)