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
            print("Por  favor seleccione el proceso a realizar:") 
            print("1. Ver saldo actual de la cuenta") 
            print("2. Realizar un retiro") 
            print("3. Realizar un retiro") 
            print("4. Salir del cajero") 
            pregunta = input("Ingrese el número de la opción elegida: ") 

            if pregunta == "1":
                balance_management(saldo)

            if pregunta == "2":
                monto = float(input("Ingresa el monto que quieres retirar: "))
                saldo = logica_retiro(saldo, monto)

            if pregunta == "3":
                monto = float(input("Ingresa el monto a depositar: "))
                saldo = deposit_logic(saldo, monto)
            
            if pregunta == "4":
                print("Gracias por usar TechBank. ¡Hasta luego!")
                break
    
tech_bank()
