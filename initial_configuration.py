#configuracion inicial del sistem
saldo = 1000
limite_intentos = 3
intentos = 0
historial = []



#--------- BIENVENIDA DEL PROGRAMA ----------

def configurar_sistema():
   
    mensaje = """
                    --- Bienvenido a TechBank Riwi Digital ---

           Este sistema es una simulación de un cajero automático
                desarrollada con fines educativos.

        Permite practicar operaciones bancarias básicas mediante código.
    """
    print(mensaje)

    
configurar_sistema()