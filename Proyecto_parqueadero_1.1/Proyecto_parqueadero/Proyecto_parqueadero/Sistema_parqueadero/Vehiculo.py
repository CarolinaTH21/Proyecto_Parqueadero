class Vehiculo:

    def __init__(self, placa, tipo, nombre, identificacion, telefono, casco=False):

        self.placa = placa
        self.tipo = tipo
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono
        self.casco = casco

        self.prioridad = False

        self.puesto = None
        self.casillero = None