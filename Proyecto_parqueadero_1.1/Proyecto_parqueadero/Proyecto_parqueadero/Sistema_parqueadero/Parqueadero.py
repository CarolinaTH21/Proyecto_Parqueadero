from ListaDobleEnlazada import ListaDobleEnlazada


class Parqueadero:

    def __init__(self, nombre, ubicacion, capacidad):

        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad

        self.vehiculos = ListaDobleEnlazada()

        self.tabla = None


    def hay_espacio(self):

        return len(self.vehiculos.recorrer()) < self.capacidad


    def ingresar_vehiculo(self, reserva):

        if not self.hay_espacio():
            return None

        vehiculo = reserva.vehiculo

        self.vehiculos.insertar(vehiculo, reserva.prioridad)

        self.reorganizar()

        return vehiculo


    def reorganizar(self):

        lista = self.vehiculos.recorrer()

        puesto = 1
        casillero = 1

        for vehiculo in lista:

            vehiculo.puesto = puesto

            if vehiculo.tipo == "Motocicleta" and vehiculo.casco:

                vehiculo.casillero = casillero
                casillero += 1

            else:

                vehiculo.casillero = None

            puesto += 1


    def retirar_vehiculo(self, placa):

        vehiculo = self.vehiculos.eliminar(placa)

        if vehiculo:

            self.reorganizar()

        return vehiculo


    def actualizar_tabla(self):

        if self.tabla is None:
            return

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        lista = self.vehiculos.recorrer()

        for v in lista:

            prioridad = "Sí" if v.prioridad else "No"

            self.tabla.insert(
                "",
                "end",
                values=(
                    v.placa,
                    v.tipo,
                    v.puesto,
                    prioridad
                )
            )

        libres = self.capacidad - len(lista)

        for i in range(libres):

            self.tabla.insert(
                "",
                "end",
                values=(
                    "-",
                    "-",
                    len(lista) + i + 1,
                    "Disponible"
                )
            )