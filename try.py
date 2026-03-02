from falso_autenticador import autenticador

def limites_intentos():
    attempts = 0 

    while attempts < 3:
        PIN = int(input("Ingresa pin: "))
        autenticador_1 = autenticador(PIN)

        if autenticador_1 == True:
           print("Bienvenido al TechBank")
           break

        else:
            print("Intento fallido, por favor intente de nuevo.")
            attempts += 1 
            if attempts == 3: 
                print("Limite de intentos alcanzados.")
                break



limites_intentos()