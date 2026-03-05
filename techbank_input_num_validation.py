#Esta funcion valida que el pin de ingreso contenga solo numeros enteros para dar el acceso

def verificar_numero():
    try:
        pin_ingresado = int(input("Ingrese su numero PIN: "))  
        return pin_ingresado
    except ValueError:
        print("Error: Eso no es un número válido. Intentalo de nuevo")
        return None

def verificacion_en_bucle():
    while True:
        verificador = verificar_numero()
        if verificador is not None:
            return verificador
        print("Intente de nuevo...")
