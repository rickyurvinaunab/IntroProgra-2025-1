def obtener_total_ventas():
    archivo =  open('pedidos.txt','r')
    pedidos =  archivo.readlines()
    total = 0
    for pedido in range(pedidos):
        #pedido = "Ricardo;pastel de choclp;12000\n"
        pedido =  pedido.strip()
        #pedido = "Ricardo;pastel de choclp;12000"
        datos =  pedido.split(';')
        # datos = ['Ricardo','pastel de choclp','12000']
        total = total + float(datos[-1])
    print("El total de las ordenes es:", total)

def agregar_plato():
    print("Funcion para agregar un plato...")
    archivo = open('menu.txt','a')
    nombre = input("Ingresa el nombre del plato: ")
    precio = input("Ingresa el precio del plato: ")
    plato = nombre +";"+precio+"\n"
    archivo.write(plato)
    archivo.close()
    print("Se agrego exitosamente el plato")

def mostrar_menu():
    archivo = open('menu.txt','r')
    contenido = archivo.readlines()
    archivo.close()
    indice_c = 1
    for linea in contenido:
        datos = linea.strip().split(';')
        print(str(indice_c)+"- El producto es "+ datos[0]+" y su precio es "+ datos[1])
        indice_c += 1
    return contenido

def modificar_plato():
    contenido = mostrar_menu()
    opcion = int(input("Ingresa el # de plato a modificar: "))
    plato_modificar = contenido[opcion-1]
    print("El plato a modificar es:", plato_modificar)
    nombre = input("Ingresa el nuevo nombre: ")
    precio = input("Ingresa el nuevo precio: ")
    item = nombre + ";" + precio + "\n"
    contenido[opcion-1] =  item
    archivo = open('menu.txt','w')
    archivo.writelines(contenido)
    archivo.close()
    print("el plato fue modificado exitosamente")

def eliminar_plato():
    contenido = mostrar_menu()
    opcion = int(input("Ingresa el # de plato a eliminar: "))
    plato_eliminar = contenido[opcion-1]
    print("El plato a eliminar es:", plato_eliminar)
    contenido.pop(opcion-1)
    archivo = open('menu.txt','w')
    archivo.writelines(contenido)
    archivo.close()
    print("el plato fue eliminado exitosamente")

def sistema_administracion():
    print("-"*10)
    print("Sistema de administracion de platos")
    print("-"*10)
    opcion  = ""
    while opcion == "":
        print("1. Agregar un plato")
        print("2. Modificar un plato")
        print("3. Eliminar un plato")
        print("4. Mostrar total de ordenes")
        print("5. Salir")
        opcion = input("Selecciona la opcion que deseas (1-2): ")
        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            modificar_plato()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            obtener_total_ventas()
        elif opcion == "5":
            print("Saliendo del sistema de admin")
            break
        
        opcion = ""

sistema_administracion()