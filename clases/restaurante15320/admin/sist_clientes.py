from administracion import mostrar_menu

def realizar_pedido():
    contenido = mostrar_menu()
    nombre = input("Ingresa tu nombre: ")
    plato = int(input("Ingresa el # de plato que deseas?: "))
    # print(contenido)
    plato_seleccionado = contenido[plato-1]
    item = nombre+";"+plato_seleccionado
    archivo = open('pedidos.txt','a')
    archivo.write(item)
    archivo.close()
    print("El pedido se realizo exitosamente")


def sistema_clientes():
    print("-"*8)
    print("Sistema de clientes")
    print("-"*8)
    opcion = ""
    while opcion == "":
        print("1. Realizar un pedido")
        print("2. Salir")
        opcion = input("Cliente ingresa tu opcion (1-3):")
        if opcion == "1":
            #realizar el pedido
            realizar_pedido()
        elif opcion == "2":
            print("Saliendo del sistema de clientes")
            break
        opcion = ""

sistema_clientes()