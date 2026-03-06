
import initial_configuration

def gestion_historial():

    historial = initial_configuration.historial

    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        print("-----HISTORIAL DE OPERACIONES-----")

        for movimiento in historial:
            print(movimiento)

            print("----------------------------------")
