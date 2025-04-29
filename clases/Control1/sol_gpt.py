# Listas para almacenar los datos
remitentes = []
destinatarios = []
fechas_envio = []
regiones_origen = []
regiones_destino = []
tipos_envio = []
pagos = []  # Lista de listas, cada elemento será [tipo_envio, monto]

# Función para registrar una encomienda
def registrar_encomienda():
    remitente = input("Nombre completo del remitente: ")
    destinatario = input("Nombre completo del destinatario: ")
    fecha = input("Fecha de envío (dd-mm-aaaa): ")
    
    while True:
        region_origen = input("Región de origen: ")
        region_destino = input("Región de destino: ")
        if region_origen != region_destino:
            break
        else:
            print("La región de origen y destino no pueden ser iguales. Intente nuevamente.")
    
    while True:
        tipo = input("Tipo de envío (Sobre/Caja): ").strip().lower()
        if tipo == "sobre":
            monto = 5000
            break
        elif tipo == "caja":
            monto = 15000
            break
        else:
            print("Tipo de envío no válido. Debe ser 'Sobre' o 'Caja'.")
    
    # Guardar los datos en sus respectivas listas
    remitentes.append(remitente)
    destinatarios.append(destinatario)
    fechas_envio.append(fecha)
    regiones_origen.append(region_origen)
    regiones_destino.append(region_destino)
    tipos_envio.append(tipo)
    pagos.append([tipo, monto])
    print("Encomienda registrada exitosamente.\n")

# Función para mostrar el reporte
def mostrar_reporte():
    if not remitentes:
        print("No hay encomiendas registradas.\n")
        return
    print("\n--- Reporte de Encomiendas ---")
    for i in range(len(remitentes)):
        print(f"\nEncomienda #{i+1}")
        print(f"Remitente: {remitentes[i]}")
        print(f"Destinatario: {destinatarios[i]}")
        print(f"Fecha de Envío: {fechas_envio[i]}")
        print(f"Región Origen: {regiones_origen[i]}")
        print(f"Región Destino: {regiones_destino[i]}")
        print(f"Tipo de Envío: {tipos_envio[i]}")
        print(f"Monto: ${pagos[i][1]}")
    print()

# Función para calcular e imprimir el monto total
def monto_total():
    total = sum(p[1] for p in pagos)
    print(f"\nMonto total de ingresos por encomiendas: ${total}\n")
    
    # Guardar el monto en un archivo
    with open("monto_total.txt", "w") as f:
        f.write(str(total))
    print("Monto guardado en 'monto_total.txt'\n")

# Función principal
def menu():
    while True:
        print("------ Real Flash SPA ------")
        print("1.- Registrar encomiendas")
        print("2.- Reporte de encomiendas")
        print("3.- Monto total de ingresos")
        print("4.- Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_encomienda()
        elif opcion == '2':
            mostrar_reporte()
        elif opcion == '3':
            monto_total()
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

# Ejecutar el programa
menu()