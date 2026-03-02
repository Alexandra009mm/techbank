#Esta es una prueba de autenticación

def autenticar_usuario(PIN):
    if PIN == 12345678:
        print("Autenticación exitosa!")
        return True
        
    else:
        print("Autenticación fallida!")
        return False
