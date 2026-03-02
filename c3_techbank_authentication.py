#Esta es una prueba de autenticación

def autenticar_usuario(pin, pin_correcto):
    if pin == pin_correcto:
        print("Autenticación exitosa!")
        return True
        
    else:
        print("Autenticación fallida!")
        return False
