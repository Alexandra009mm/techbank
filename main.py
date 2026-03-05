#Este es el codigo main y todo va a estar aqui, es el codigo principal del programa

from techbank_attemp_control import inicio_de_sesion
from balance_management import balance_management
from techbank_withdrawal_logic import logica_retiro
from deposit_logic import deposit_logic     

saldo = float(1000.00)
#Este es el menu
def tech_bank():
    print("\nCajero automático TechBank\n")
    inicio = inicio_de_sesion()
    if inicio == True:
        while True:
            global saldo
            print("Seleccione una opción:") 
            print("1. Ver saldo") 
            print("2. Retirar dinero") 
            print("3. Depositar dinero") 
            print("4. Salir") 
            preguta = input("Ingrese el número de la opción deseada: ") 

            if preguta == "1":
                balance_management(saldo)

            if preguta == "2":
                monto = float(input("Ingresa el monto a retirar: "))
                saldo = logica_retiro(saldo, monto)

            if preguta == "3":
                monto = float(input("Ingresa el monto a depositar: "))
                saldo = deposit_logic(saldo, monto)
            
            if preguta == "4":
                print("Gracias por usar TechBank. ¡Hasta luego!")
                break
    
tech_bank()
