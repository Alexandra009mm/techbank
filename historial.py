from datetime import datetime

historial = []

def registrar_operacion(tipo, monto, saldo):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if monto is None:
        mensaje = f"[{fecha}] {tipo} - Saldo actual: ${saldo}"
    else:
        mensaje = f"[{fecha}] {tipo} - ${monto} - Saldo actual: ${saldo}"
    
    historial.append(mensaje)

def mostrar_historial():
    if not historial:
        print("No hay operaciones registradas.")
        return
    
    print("--- Historial de Operaciones ---")
    for i, operacion in enumerate(historial, 1):
        print(f"{i}. {operacion}")