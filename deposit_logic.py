import initial_configuration

def deposit_logic():
        while True:
            try:
                monto = float(input("Ingresa el monto a depositar: "))
        
                if monto > 0:
                    initial_configuration.saldo += monto
                    print(f"Deposito exitoso! Su nuevo saldo es: {initial_configuration.saldo}")
                    movimiento = f"deposito {monto} / saldo restante: {initial_configuration.saldo}"
                    initial_configuration.historial.append(movimiento)
                    return False
                else:
                    print("Monto invalido. Porfavor ingresa un valor positivo.")
            except ValueError:
                print("Error")
deposit_logic()