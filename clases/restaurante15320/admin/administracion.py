# Toda la logica del administrador
def agregar_plato():
    archivo = open('menu.txt','a')
    nombre = input("ingresa el nombre del plato: ")
    precio = float(input("ingresa el precio del plato: "))
    item = nombre + ";" + str(precio) + "\n"
    # item = pan;1500\n
    archivo.write(item)
    print("Plato agregado exitosamente!!!")
    archivo.close()

def modificar_plato():
    print("Modificando un plato")
    contenido  = mostrar_menu()
    opcion_m = int(input("Ingresa el # de plato que deseas modificar"))
    cantidad_platos = len(contenido)
    if opcion_m > cantidad_platos or opcion_m <= 0:
        print("No existe la opcion!")
    else:
        plato_a_mod = contenido[opcion_m-1]
        print("El plato a modificar es:", plato_a_mod)
        nuevo_nombre = input("Ingresa el nuevo nombre: ")
        nuevo_precio = input("Ingresa el nuevo precio: ")
        plato = nuevo_nombre + ";"+nuevo_precio+"\n"
        contenido[opcion_m-1] = plato
        archivo =  open('menu.txt','w')
        archivo.writelines(contenido)
        archivo.close()
        print("El plato fue modificado exitosamente")

def mostrar_menu():
    archivo = open('menu.txt','r')
    contenido = archivo.readlines()
    indice = 1
    for plato in contenido:
        datos = plato.strip().split(';')
        print("Plato #", indice, "Nombre:", datos[0], "Precio:", datos[1])
        indice =  indice + 1
    
    return contenido

def eliminar_plato():
    print("Eliminando un plato...")
    # abrir el archivo
    contenido = mostrar_menu()
    # preguntar el plato
    plato_eliminar = input("Ingresa el nombre del plato a eliminar: ")
    # verificar si el plato existe
    indice_c = 0
    for plato in contenido:
        datos = plato.strip().split(';')
        #datos = ['pan','1500']
        if datos[0] == plato_eliminar:
            plato_eliminado = contenido.pop(indice_c)
        indice_c += 1
    archivo = open('menu.txt','w')
    archivo.writelines(contenido)
    archivo.close()
    print("El plato eliminado es:", plato_eliminado)


def sistema_administracion():
    print("-"*8)
    print("Sistema de administracion")
    print("-"*8)
    opcion = ""
    while opcion == "":
        print("1. Agregar plato")
        print("2. Modificar plato")
        print("3. Eliminar plato")
        print("4. Salir")
        opcion = input("Administrador ingresa tu opcion (1-3):")
        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            modificar_plato()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            print("Saliendo del sistema de administracion")
            break
        opcion = ""

sistema_administracion()