def registrar_operacion(tipo, monto, saldo_actual):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if monto is None:
        mensaje = f"[{fecha}] {tipo} - Saldo actual: ${saldo_actual}"
    else:
        mensaje = f"[{fecha}] {tipo} - ${monto} - Saldo actual: ${saldo_actual}"

    try:
        with open(ARCHIVO_HISTORIAL, "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)
    except:
        pass

def mostrar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("No hay movimientos registrados.")
            else:
                print("--- Historial de Operaciones ---")
                print(contenido)
    except:
        print("No hay historial disponible.")
