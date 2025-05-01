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
        archivo = open('ordenes.txt','w')  # Se crea el archivo vacio
        archivo.close()
        print("El archivo ordenes.txt fue creado exitosamente.!")
        return ordenes  # Se retorna la lista vacia

    # Si el archivo existe, se abre y se leen todas sus lineas
    archivo = open('ordenes.txt','r')
    contenido = archivo.readlines()
    archivo.close()

    return contenido  # Se retorna la lista de lineas leidas

# Funcion que muestra las opciones del menu segun el horario (1: desayuno, 2: almuerzo, 3: cena)
def opciones_menu(opcion, ordenes_clientes):
    menu = obtener_info_menu()  # Se obtiene el menu completo
    contador_platos = 0  # Contador para saber si hay platos disponibles

    # Se recorre el menu buscando los platos que coincidan con la opcion (horario)
    for plato in menu:
        if plato[-2] == str(opcion):  # Se compara el antepenultimo caracter (identificador de horario)
            contador_platos += 1
            print(plato)  # Se muestra el plato al cliente

    print("----------------")

    # Si hay platos disponibles, se permite seleccionar
    if contador_platos > 0:
        ordenes_clientes = seleccion_plato(ordenes_clientes)
    else:
        print("No hay platos disponibles para el desayuno.")
        print("----------------")
    
    return ordenes_clientes  # Se retorna la lista de ordenes actualizada

# Funcion que obtiene el siguiente numero de orden basado en las ordenes anteriores
def obtener_numero_orden():
    ordenes = obtener_info_ordenes()
    numero_orden = 0

    # Se busca la ultima orden registrada y se extrae su numero
    for orden in ordenes:
        if "Orden" in orden:
            numero_orden = int(orden[-2])  # Se asume que el numero de orden es el penultimo caracter

    return numero_orden + 1  # Se retorna el siguiente numero de orden

# Funcion que permite al cliente seleccionar un plato del menu
def seleccion_plato(ordenes_clientes):
    menu = obtener_info_menu()  # Se obtiene el menu
    plato_seleccionado = int(input("Seleccione el # de plato que desea consumir: "))
    ordenes_clientes.append(menu[plato_seleccionado - 1])  # Se agrega el plato elegido a la orden
    return ordenes_clientes  # Se retorna la lista actualizada

# Funcion que guarda la orden completa en el archivo ordenes.txt
def guardar_orden(ordenes_clientes):
    numero_orden = obtener_numero_orden()  # Se obtiene el numero de orden
    archivo = open('ordenes.txt', 'a')  # Se abre el archivo en modo agregar

    # Se escribe el encabezado de la orden
    archivo.write("Orden #: " + str(numero_orden) + "\n")

    # Se escriben todos los platos seleccionados
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
            ordenes_clientes = opciones_menu(int(opcion_horario), ordenes_clientes)
        else:
            print("Opcion no valida. Por favor, elige una opcion correcta.")
            continue  # Se repite el ciclo para el mismo cliente si la opcion fue invalida

    print(ordenes_clientes)  # Se muestra la lista de platos seleccionados
    guardar_orden(ordenes_clientes)  # Se guarda la orden en el archivo