from admin.administracion import sistema_administracion
print("Bienvenido al Restaurante!")


opcion  =""
while opcion == "":
    print("1. Administracion menu")
    print("2. Administracion clientes")
    print("3. Salir")
    opcion = input("Selecciona la opcion que deseas (1-2): ")
    if opcion == "1":
        sistema_administracion()
    elif opcion == "2":
        print("Bienvenido al sistema de administracion de clientes")
    elif opcion == "3":
        print("Saliendo del sistema")
        break
    
    opcion = ""

print("Fin del programa")