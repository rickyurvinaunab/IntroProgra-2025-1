def agregar_plato():
    print("Funcion para agregar un plato...")
    archivo = open('menu.txt','a')
    nombre = input("Ingresa el nombre del plato: ")
    precio = input("Ingresa el precio del plato: ")
    plato = nombre +";"+precio+"\n"
    archivo.write(plato)
    archivo.close()
    print("Se agrego exitosamente el plato")

def sistema_administracion():
    print("-"*10)
    print("Sistema de administracion de platos")
    print("-"*10)
    opcion  = ""
    while opcion == "":
        print("1. Agregar un plato")
        print("2. Salir")
        opcion = input("Selecciona la opcion que deseas (1-2): ")

        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            print("Saliendo del sistema de admin")
            break
        
        opcion = ""
