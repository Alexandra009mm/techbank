#
def mostrar_menu():
    print("\n1. Consultar saldo")
    print("2. Retirar")
    print("3. Depositar")
    print("4. Historial")
    print("5. Salir")
    
    # Aquí se pregunta qué operación desea realizar el usuario
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Aquí se llama la función consultar_saldo()
        pass
    elif opcion == "2":
        # Aquí se llama la función retirar()
        pass
    elif opcion == "3":
        # Aquí se llama la función depositar()
        pass
    elif opcion == "4":
        # Aquí se llama la función historial()
        pass
    elif opcion == "5":
        # Aquí se llama la función salir() o se termina el programa
        pass
    else:
        print("Opción inválida. Intente nuevamente.")

    return opcion