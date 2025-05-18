# import admin.administracion
# import admin.administracion # importo todo el archivo
from admin.administracion import sistema_administracion as sa
print("Bienvenido al restuarante!!!")

opcion = ""
while opcion == "":
    print("Menu del sistema")
    print("1. Sistema de Administracion")
    print("2. Sistema de Clientes")
    print("3. Salir")
    opcion = input("Ingresa la opcion (1-3):")
    if opcion == "1":
        sa()
        # sistema_administracion()
    elif opcion == "2":
        print("Has elegido la opcion de clientes")
    elif opcion == "3":
        print("Saliendo del sistema")
        break
    
    opcion = ""

print("Fin del programa")