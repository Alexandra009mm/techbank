
import initial_configuration

def logica_retiro():
    while True:
        try:
            monto = int(input("ingrese cuanto desea retirar: "))
            if monto < 0:
                 print("Error solo ingrese numeros positivos")
            elif monto > initial_configuration.saldo:
                print(f"saldo insuficiente, su saldo es {initial_configuration.saldo}, por favor ingrese un retiro valido")
            else:
                initial_configuration.saldo -= monto
                print(f"proceso exitoso su saldo actual es {initial_configuration.saldo}")
                movimiento = f"retiro {monto} / saldo restante: {initial_configuration.saldo}"
                initial_configuration.historial.append(movimiento)
                break
            

        except ValueError:
            print("Error")
