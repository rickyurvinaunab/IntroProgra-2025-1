def mostrar_menu(menu):
    print("---------------------")
    print("Mostrando el menu....")
    indice = 0
    for plato in menu:
        print("#", indice,"Nombre: ", plato[0],"Precio:", plato[1],"Tipo de menu:", plato[2])
        indice += 1
    print("------------------")

def agregar_plato(menu):
        nombre_plato = input("Ingresa el nombre del plato: ")
        encontrado = False
        for pl in menu:
            if pl[0] ==  nombre_plato:
                print("El plato", nombre_plato,"ya existe en el menu.")
                encontrado =  True
                break
        if encontrado ==  False:
            precio = input("Ingresa el precio del plato: ")
            tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena ")
            plato = [nombre_plato, precio, tipo_menu]
            menu.append(plato)
            print("Se agrego exitosamente al menu el plato", nombre_plato)
        
        return menu

def modificar_plato(menu):
        print("Modificando un plato...")
        if len(menu)>0:
            mostrar_menu(menu)
            numero_plato = int(input("Ingresa el numero de plato a editar: "))
            if numero_plato < len(menu) and numero_plato >= 0:
                print("El plato a modificar es: ", menu[numero_plato][0], "el precio es:", menu[numero_plato][1])
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                nuevo_precio = input("Ingresa el nuevo precio: ")
                nuevo_tipo = input("Ingresa el nuevo tipo (1) Desayuno, (2) Almuerzo, (3) Cena: ")
                menu[numero_plato][0] = nuevo_nombre
                menu[numero_plato][1] = nuevo_precio
                menu[numero_plato][2] = nuevo_tipo
                print("El plato:", nuevo_nombre,"se modifico exitosamente...")
            else:
                print("El plato", numero_plato,"no existe en el menu")
        else:
            print("El menu esta vacio.")
        
        return menu

def eliminar_plato(menu):
    print("Eliminando un plato...")
    if len(menu)>0:
        mostrar_menu(menu)
        numero_plato = int(input("Ingresa el numero de plato a eliminar: "))
        if numero_plato < len(menu) and numero_plato >= 0:
            plato_eliminado = menu.pop(numero_plato)
            print("El plato eliminado es:" , plato_eliminado[0])
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")
    
    return menu


def sistema_administracion(menu):
    while True:
        print("1. Agregar platos...")
        print("2. Modificar un plato...")
        print("3. Eliminar un plato...")
        print("4. Ver el menu...")
        print("5. Salir...")
        opcion_adm = input("Ingrese la opcion (1-5)")

        if opcion_adm == "1":
            menu = agregar_plato(menu)
        elif opcion_adm =="2":
            menu =  modificar_plato(menu)
        elif opcion_adm == "3":
            menu = eliminar_plato(menu)
        elif opcion_adm == "4":
            mostrar_menu(menu)
        elif opcion_adm == "5":
            print("Saliendo del sistema de adminsitracion")
            break
    
    return menu