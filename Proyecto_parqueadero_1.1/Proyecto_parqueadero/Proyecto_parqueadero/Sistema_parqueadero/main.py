import SistemaParqueaderos
import InterfazPrincipal

sistema = SistemaParqueaderos.SistemaParqueaderos()

app = InterfazPrincipal.InterfazPrincipal(sistema)

app.ejecutar()