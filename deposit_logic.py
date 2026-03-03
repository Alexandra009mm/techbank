def deposit_logic(saldo):
    
        monto = float(input("Ingresa el monto a depositar: "))
        
        if monto > 0:
            saldo += monto
            print(f"Deposito exitoso! Su nuevo saldo es: {saldo}")
        else:
            print("Monto invalido. Porfavor ingresa un valor positivo.")

    