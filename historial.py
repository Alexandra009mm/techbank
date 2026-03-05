
import initial_configuration

def gestion_historial():
    if len(initial_configuration.historial) == 0:
        print("No hay movimientos registrados.")
    else:
        print("HISTORIAL")
        for movimiento in initial_configuration.historial:
            print(movimiento)