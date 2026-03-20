class SistemaParqueaderos:

    def __init__(self):

        self.parqueaderos = []


    def agregar_parqueadero(self, parqueadero):

        self.parqueaderos.append(parqueadero)


    def buscar_parqueaderos_disponibles(self, ubicacion):

        ubicacion = ubicacion.lower()

        disponibles = []

        for p in self.parqueaderos:

            if ubicacion in p.ubicacion.lower() and p.hay_espacio():

                disponibles.append(p)

        # si no hay en esa ubicación buscar cualquiera disponible
        if len(disponibles) == 0:

            for p in self.parqueaderos:

                if p.hay_espacio():

                    disponibles.append(p)

        return disponibles