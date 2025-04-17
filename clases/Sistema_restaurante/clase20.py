# clase 20
from administracion import sistema_administracion


print("Bienvenido al restaurante Quiteno libre")

menu = []

while True:
    print("Menu de Opciones: ")
    print("1. Sistema de Administracion: ")
    print("2. Sistema de Clientes: ")
    print("3. Salir: ")

    opcion = input("Ingrese la opcion (1-3): ")

    if opcion == "1":
        print("Sistema de administracion...")
        menu = sistema_administracion(menu)
    elif opcion == "2":
        print("Sistema de clientes")
    elif opcion == "3":
        print("Saliendo del sistema....")
        break

    elif opcion == "3":
        print("Saliendo del sistema")
        break


            




















