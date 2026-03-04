#Implemento código de validación de relas de negocios

limite_diario = 5000
billete_minimo = 10
saldo_minimo_cuenta = 5.0

# Se hace la definición de validacion de retiros.

def validar_reglas_retiro(saldo_actual, monto):

    if monto % billete_minimo != 0:
        return False, f"Error: Solo se entregan billetes de {billete_minimo}, ejemplo múltiplos de 10"
    
    if monto > limite_diario:
        return False, f"Error: El limite de retiro diario es {limite_diario}"
    
    if monto > saldo_actual:
        return False, "Error: Fondos insuficientes"
 
    if (saldo_actual - monto) < saldo_minimo_cuenta:
        return False, f"Error: El saldo minimo restante debe ser {saldo_minimo_cuenta}"
    
    if monto <= 0:
        return False, "Error: Ingrese un monto mayor a cero"

    return True, "Validacion exitosa"

# Hago condicionales para verificar cada movimiento, también coloco try para prueba.
saldo_usuario = 1000.00
print("Saldo en cuenta:", saldo_usuario)

try:
    monto_solicitado = float(input("Monto a retirar: "))

    permitido, mensaje = validar_reglas_retiro(saldo_usuario, monto_solicitado)

    if permitido:
        saldo_usuario -= monto_solicitado
        print(mensaje)
        print("Retiro completado. Nuevo saldo:", saldo_usuario)
    else:
        print("Transaccion rechazada:", mensaje)

except ValueError:
    print("Error: Ingrese un valor numerico")