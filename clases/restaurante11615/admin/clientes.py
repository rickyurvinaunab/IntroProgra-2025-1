from administracion import mostrar_menu

def ordenar():
    #mostrar el menu
    contenido = mostrar_menu()
    nombre = input("Ingresa tu nombre: ")
    opcion = int(input("Ingresa el # de plato que deseas solicitar: "))
    #mostrar al usuario
    plato_seleccionado = contenido[opcion-1]
    print("El plato seleccionado es:", plato_seleccionado)
    archivo = open('pedidos.txt','a')
    item = nombre +";"+plato_seleccionado
    #item =  "Ricardo;pan;1500\n"
    archivo.write(item)
    archivo.close()
    print("Orden realizada!!!")


def sistema_clientes():

    print("-"*10)
    print("Sistema de administracion de clientes")
    print("-"*10)
    opcion  = ""
    while opcion == "":
        print("1. Ordenar un plato")
        print("2. Salir")
        opcion = input("Selecciona la opcion que deseas (1-2): ")
        if opcion == "1":
            ordenar()
        elif opcion == "4":
            print("Saliendo del sistema de admin")
            break
        opcion = ""


sistema_clientes()