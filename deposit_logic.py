def deposit_logic(saldo, monto):
        
        if monto > 0:
            saldo += monto
            print(f"Deposito exitoso! Su nuevo saldo es: {saldo}")
            return saldo
        else:
            print("Monto invalido. Porfavor ingresa un valor positivo.")

    
