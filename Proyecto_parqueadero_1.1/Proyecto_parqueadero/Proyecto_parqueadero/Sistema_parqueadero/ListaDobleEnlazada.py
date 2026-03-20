from Nodo import Nodo


class ListaDobleEnlazada:

    def __init__(self):

        self.cabeza = None


    def insertar(self, dato, prioridad=False):

        nuevo = Nodo(dato)

        # lista vacía
        if self.cabeza is None:

            self.cabeza = nuevo
            return

        # INSERTAR PRIORIDAD
        if prioridad:

            actual = self.cabeza
            ultimo_prioridad = None

            while actual:

                if actual.dato.prioridad:
                    ultimo_prioridad = actual

                actual = actual.siguiente

            # si no hay prioridades aún → insertar al inicio
            if ultimo_prioridad is None:

                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza = nuevo

            # insertar después de la última prioridad
            else:

                nuevo.siguiente = ultimo_prioridad.siguiente
                nuevo.anterior = ultimo_prioridad

                if ultimo_prioridad.siguiente:
                    ultimo_prioridad.siguiente.anterior = nuevo

                ultimo_prioridad.siguiente = nuevo

            return

        # INSERTAR NORMAL (al final)
        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo
        nuevo.anterior = actual


    def eliminar(self, placa):

        actual = self.cabeza

        while actual:

            if actual.dato.placa == placa:

                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                return actual.dato

            actual = actual.siguiente

        return None


    def recorrer(self):

        lista = []

        actual = self.cabeza

        while actual:

            lista.append(actual.dato)

            actual = actual.siguiente

        return lista