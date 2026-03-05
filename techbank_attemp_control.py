from c3_techbank_authentication import autenticar_usuario
from techbank_input_num_validation import verificacion_en_bucle

def inicio_de_sesion():
    attempts = 0 

    while attempts < 3:
       pin_usuario = verificacion_en_bucle()
       autenticador = autenticar_usuario(pin_usuario)
       
       if autenticador == True:
           print("Bienvenido al TechBank")
           return True
       
       if autenticador == False: 
          print("Intento fallido, por favor intente de nuevo.")
          attempts += 1
          if attempts == 3: 
             print("Limites de intentos alcanzados, intente nuevamente mas tarde")
             return False



