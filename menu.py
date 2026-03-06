from balance_management import balance_management as bl
from techbank_withdrawal_logic import logica_retiro as ret
from deposit_logic import deposit_logic as dep
from historial import gestion_historial as his
import initial_configuration


def mostrar_menu():
    while True:
        print("OPCIONES")
        print("\n1. Consultar saldo")
        print("2. Retirar")
        print("3. Depositar")
        print("4. Historial")
        print("5. Salir")
    
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            bl()
            
        elif opcion == "2":
            ret()
            
        elif opcion == "3":
            dep()
            
        elif opcion == "4":
            his()
            
        elif opcion == "5":
            break
            
        else:
            print("opcion invalida.")
