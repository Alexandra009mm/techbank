#Esta es una prueba de autenticación


def autenticar_usuario(pin):
    pin_correcto = 1234
    if pin != pin_correcto:
        print("Autenticación fallida!")
        return False
    
    if pin == pin_correcto:
        print("Autenticación exitosa!")
        return True
        


