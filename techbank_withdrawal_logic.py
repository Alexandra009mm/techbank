def logica_retiro(saldo):
    try:
        while True:
            monto = int(input("ingrese cuanto desea retirar: "))
            if monto < 0:
                 print("Error solo ingrese numeros positivos")
            elif monto > saldo:
                print(f"saldo insuficiente, su saldo es {saldo}, por favor ingrese un retiro valido")
            else:
                saldo -= monto
                print(f"proceso exitoso su saldo actual es {saldo}")
                break

    except ValueError:
      print("Error")

logica_retiro(saldo)