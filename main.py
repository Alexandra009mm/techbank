from initial_configuration import configurar_sistema
from techbank_attemp_control import limites_intentos
from techbank_withdrawal_logic import retiro 
from validacion_reglas import validar_reglas_retiro
from deposit_logic import deposit_logic as dl
from c3_techbank_authentication import autenticar_usuario
from balance_management import balance_management as consultar

saldo = 1000
pin = "1234"
limite_intentos = 3
intentos = 0

def menu():
    print("\nMenu ")
    print("1. Consultar saldo")
    print("2. Retirar")
    print("3. Depositar")
    print("4. Historial")
    print("5. Salir")
    
    opcion= input("Seleccione una opción: ")
    return opcion
 
opcion_seleccionada =  menu()

if (opcion_seleccionada == 1):
    consultar(saldo)
elif (opcion_seleccionada == 2):
   saldo = retiro (saldo)
    

#balance = 0.0

#user_input = input("Enter 'deposit' to make a deposit: ")
#if user_input == "deposit":
#test = True

#if test:
#   dl(balance)

