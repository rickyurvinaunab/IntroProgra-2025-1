# Se importa el modulo os para manejar rutas de archivos de forma compatible con cualquier sistema operativo
import os

# Se importa la funcion obtener_info_menu desde el modulo administracion
from administracion import obtener_info_menu

# Funcion que obtiene las ordenes guardadas en el archivo ordenes.txt
def obtener_info_ordenes():
    ordenes = []  # Lista vacia para guardar las ordenes
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'ordenes.txt')  # Se define la ruta del archivo

    # Si el archivo no existe, se informa al usuario y se crea
    if not os.path.isfile(ruta_archivo):
        print("El archivo ordenes.txt no existe.")
        archivo = open(ruta_archivo,'w')  # Se crea el archivo vacio
        contenido = archivo.readlines()  # Se lee el contenido
        archivo.close()
        print("El archivo ordenes.txt fue creado exitosamente.!")
        return contenido  # Se retorna la lista vacia

    # Si el archivo existe, se abre y se lee su contenido como una lista separada por punto y coma
    archivo = open(ruta_archivo,'r')
    contenido = archivo.readlines()
    archivo.close()

    return contenido  # Se retorna la lista de ordenes

# Funcion que muestra las opciones del menu segun el horario (1: desayuno, 2: almuerzo, 3: cena)
def opciones_menu(opcion, ordenes_clientes, numero_orden):
    menu = obtener_info_menu()  # Se obtiene el menu completo
    contador_platos = 1  # Contador para saber si hay platos disponibles

    lista_tipos_menu = ["Desayuno", "Almuerzo", "Cena"]  # Lista de tipos de menu
    # Se recorre el menu buscando los platos que coincidan con la opcion (horario)
    for plato in menu:
        partes = plato.strip().split(";")
        tipo = partes[2].strip()
        if tipo == lista_tipos_menu[opcion - 1]:  # Se compara el tipo de plato con la opcion seleccionada
            print(f"{contador_platos}. {partes[0]} - ${partes[1]}") # Se muestra el plato al cliente con formato
        contador_platos += 1

    print("----------------")

    # Si hay platos disponibles, se permite seleccionar
    if contador_platos > 0:
        nuevo_plato = seleccion_plato(numero_orden)
        ordenes_clientes.append(nuevo_plato)
    else:
        print("No hay platos disponibles para el desayuno.")
        print("----------------")

    return ordenes_clientes  # Se retorna la lista de ordenes actualizada

# Funcion que obtiene el siguiente numero de orden basado en las ordenes anteriores
def obtener_numero_orden():
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'ordenes.txt')
    if not os.path.isfile(ruta_archivo):
        return 1

    archivo = open(ruta_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()

    max_numero_orden = 0
    for linea in lineas:
        partes = linea.strip().split(";")
        numero = int(partes[0])
        if numero > max_numero_orden:
            max_numero_orden = numero

    return max_numero_orden + 1  # Se retorna el siguiente numero de orden

# Funcion que permite al cliente seleccionar un plato del menu
def seleccion_plato(numero_orden):
    menu = obtener_info_menu()  # Se obtiene el menu
    plato_seleccionado = int(input("Seleccione el # de plato que desea consumir: "))
    partes = menu[plato_seleccionado - 1].strip().split(";")
    if len(partes) >= 3:
        nombre = partes[0].strip()
        precio = partes[1].strip()
        tipo = partes[2].strip()
        linea = f"{numero_orden};{nombre};{precio};{tipo}\n"
        return linea
    return ""

# Funcion que guarda la orden completa en el archivo ordenes.txt
def guardar_orden(ordenes_clientes):
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'ordenes.txt')
    archivo = open(ruta_archivo, 'a')  # Se abre el archivo en modo agregar

    # Se escriben todos los platos seleccionados sin encabezado
    archivo.writelines(ordenes_clientes)

    archivo.close()

# Funcion principal del sistema cliente
def sistema_cliente():
    # Lista con los nombres de los horarios disponibles
    opciones_menu_nombres = [
        "Desayuno",
        "Almuerzo",
        "Cena"
    ]

    # Se solicita la cantidad de clientes que van a ordenar
    cantidad_clientes = int(input("Ingrese la cantidad de clientes que van a consumir: "))
    ordenes_clientes = []  # Lista vacia para guardar las ordenes

    numero_orden = obtener_numero_orden()

    # Se repite el proceso por cada cliente
    for cliente in range(1, cantidad_clientes + 1):
        print("--- Cliente", cliente, "---")
        opcion_horario = ""

        # Se valida que el cliente elija una opcion valida
        while opcion_horario not in ["1", "2", "3"]:
            print("Que horario deseas?")
            print("1. Desayuno")
            print("2. Almuerzo")
            print("3. Cena")
            opcion_horario = input("Ingresa una opcion (1-3): ")

        # Se muestra el menu segun la opcion seleccionada
        if opcion_horario in ["1", "2", "3"]:
            print("Menu", opciones_menu_nombres[int(opcion_horario) - 1])
            ordenes_clientes = opciones_menu(int(opcion_horario), ordenes_clientes, numero_orden)
        else:
            print("Opcion no valida. Por favor, elige una opcion correcta.")
            continue  # Se repite el ciclo para el mismo cliente si la opcion fue invalida

    print(ordenes_clientes)  # Se muestra la lista de platos seleccionados
    guardar_orden(ordenes_clientes)  # Se guarda la orden en el archivo