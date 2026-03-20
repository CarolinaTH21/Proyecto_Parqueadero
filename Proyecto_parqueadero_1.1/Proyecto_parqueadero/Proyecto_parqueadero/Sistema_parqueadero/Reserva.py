class Reserva:
    def __init__(self, vehiculo, prioridad=False):

        self.vehiculo = vehiculo
        self.prioridad = prioridad

        vehiculo.prioridad = prioridad