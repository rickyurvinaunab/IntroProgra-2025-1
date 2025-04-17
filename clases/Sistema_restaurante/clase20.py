# clase 20
print("Bienvenido al restaurante Quiteno libre")
def mostrar_menu(menu):
    print("Mostrando el menu....")
    indice = 0
    for plato in menu:
        print("#", indice,"Nombre: ", plato[0],"Precio:", plato[1],"Tipo de menu:", plato[2])
        indice += 1
    print("------------------")


while True:
    print("Menu de Opciones: ")
    print("1. Sistema de Administracion: ")
    print("2. Sistema de Clientes: ")
    print("3. Salir: ")

    opcion = input("Ingrese la opcion (1-3): ")
    menu = []

    if opcion == "1":
        print("Sistema de administracion...")
        
        while True:
            print("1. Agregar platos...")
            print("2. Modificar un plato...")
            print("3. Eliminar un plato...")
            print("4. Ver el menu...")
            print("5. Salir...")
            opcion_adm = input("Ingrese la opcion (1-5)")

            if opcion_adm == "1":
                nombre_plato = input("Ingresa el nombre del plato: ")
                precio = input("Ingresa el prefcio del plato: ")
                tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena ")
                plato = [nombre_plato, precio, tipo_menu]
                menu.append(plato)
                print("Se agrego exitosamente al menu el plato", nombre_plato)
            elif  opcion_adm =="2":
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
            elif opcion_adm == "3":
                print("Eliminando un plato...")
                if len(menu)>0:
                    mostrar_menu(menu)
                    numero_plato = int(input("Ingresa el numero de plato a eliminar: "))
                    if numero_plato < len(menu) and numero_plato >= 0:
                        plato_eliminado = menu.pop(numero_plato)
                        print("El plato eliminado es:" , plato_eliminado[0])
            elif opcion_adm == "4":
                mostrar_menu(menu)
            elif opcion_adm == "5":
                print("Saliendo del sistema de adminsitracion")
                break
    elif opcion == "2":
        print("Sistema de clientes")
    elif opcion == "3":
        print("Saliendo del sistema....")
        break

    elif opcion == "3":
        print("Saliendo del sistema")
        break


            




















