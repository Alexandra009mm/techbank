#configuracion inicial del sistema
def configurar_sistema():
    saldo = 1000
    pin = "1234"
    limite_intentos = 3
    intentos = 0
    historial = []

    print("Bienvenido a TechBank Riwi Digital")

    return saldo, pin, limite_intentos, intentos, historial


#solo llama la funcion para saber si esta funcionando correctamente. el objetivo es poder inicializar el sistema con los valores predeterminados.
configurar_sistema()