

def logica_retiro(saldo, monto):
        if monto < 0:
             print("Error solo ingrese numeros positivos")
        elif monto > saldo:
            print(f"saldo insuficiente, su saldo es {saldo}, por favor ingrese un retiro valido")
        elif monto <= saldo:
            saldo -= monto
            print(f"proceso exitoso su saldo actual es {saldo}")
            return saldo
        else:
             print("Error, por favor ingrese un numero valido")

