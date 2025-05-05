# Se importan las funciones necesarias desde los modulos administracion y clientes
from administracion import sistema_administracion
from clientes import sistema_cliente, obtener_info_ordenes

# Se muestra un mensaje de bienvenida al usuario
print("Bienvenido al restaurante Quiteno libre")

# Se inicia un bucle infinito para mostrar el menu principal hasta que el usuario decida salir
while True:
    # Se imprime el menu de opciones para el usuario
    print("Menu de Opciones: ")
    print("1. Sistema de Administracion: ")
    print("2. Sistema de Clientes: ")
    print("3. Salir: ")

    # Se solicita al usuario que ingrese una opcion
    opcion = input("Ingrese la opcion (1-3): ")

    # Si el usuario elige la opcion 1, se llama al sistema de administracion
    # Se pasa como argumento la informacion de las ordenes obtenida desde la funcion obtener_info_ordenes()
    if opcion == "1":
        sistema_administracion(obtener_info_ordenes())

    # Si el usuario elige la opcion 2, se llama al sistema de clientes
    elif opcion == "2":
        sistema_cliente()

    # Si el usuario elige la opcion 3, se imprime un mensaje de salida y se rompe el bucle para terminar el programa
    elif opcion == "3":
        print("Saliendo del sistema....")
        break