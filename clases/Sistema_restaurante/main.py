from administracion import sistema_administracion
from clientes import sistema_cliente

print("Bienvenido al Restaurante Quiteño libre")
opcion = ""
menu = []
while True:
    print("Bienvenido al restaurante")
    print("1. Sistema de Administracion")
    print("2. Sistema de Clientes")
    print("3. Salir")
    opcion = input("Ingresa una opcion (1-3): ")
    if opcion == "1":
        #Sistema de admnistracion
        print("Sistema de administracion...")
    elif opcion == "2":
        print("Sistema de clientes...")
    elif opcion == "3":
        print("Saliendo del sistema. Hasta luego!")
        break
    else:
        print("Opcion no valida. Por favor, elige una opcion correcta.")