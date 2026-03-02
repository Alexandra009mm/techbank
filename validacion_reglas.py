### importe el archivo.
limite_diario_retiro = 5000
demoninacion_minima = 10
saldo_minimo_permanencia = 5.0

### definí la funcion
def validar_reglas_retiro(saldo_actual, monto):

### Usé condicional if.

    if monto % demoninacion_minima != 0:
        return False, f"Error: Solo se pueden retirar múltiplos de ${demoninacion_minima}."
    
    if monto > limite_diario_retiro:
        return False, f"Error: El límite máximo por retiro es ${limite_diario_retiro}."
    
    if monto > saldo_actual:
        return False, "Error: Fondos insuficientes para completar esta operación."
 
    if (saldo_actual - monto) < saldo_minimo_permanencia:
        return False, f"Error: La cuenta debe mantener un saldo mínimo de ${saldo_minimo_permanencia}."
    
    if monto <= 0:
        return False, "Error: El monto solicitado debe ser mayor a cero."

    return True, "Validación exitosa. Procediendo al despacho de efectivo."

def validar_estado_cuenta(estado_usuario):

    if estado_usuario.lower() != "activo":
        return False, f"Operación bloqueada. Estado de cuenta: {estado_usuario}."
    return True, "Cuenta activa."