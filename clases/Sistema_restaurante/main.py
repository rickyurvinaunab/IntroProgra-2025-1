from administracion import sistema_administracion
from clientes import sistema_cliente

print("Bienvenido al Restaurante Quiteño libre")
opcion = ""
menu = []
while opcion != "1" and opcion != "2" and opcion != "3":
    print("Bienvenido al restaurante")
    print("1. Sistema de Administracion")
    print("2. Sistema de Clientes")
    print("3. Salir")
    opcion = input("Ingresa una opcion (1-3): ")
    if opcion == "1":
        menu = sistema_administracion(menu)
        print(menu)
    elif opcion == "2":
        print(menu)
        if len(menu)>0:
            sistema_cliente(menu)
        else:
            print("Primero debes configurar el menu en el sistema de administracion.")
    elif opcion == "3":
        print("Saliendo del sistema. Hasta luego!")
        break
    else:
        print("Opcion no valida. Por favor, elige una opcion correcta.")

    opcion = ""

