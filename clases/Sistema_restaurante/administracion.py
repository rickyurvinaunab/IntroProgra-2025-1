def sistema_administracion(menu):
    print("Bienvenido al sistema de administracion del restaurante.")
    print("Por favor, ingresa la informacion de los platos.")
    while True:
        print("Menu de administracion:")
        print("1. Gestionar platos")
        print("2. Mostrar menu")
        print("3. Salir")
        opcion = input("Selecciona una opcion (1-3): ")

        if opcion == "1":
            gestionar_platos(menu)
        elif opcion == "2":
            mostrar_menu(menu)
        elif opcion == "3":
            print("Saliendo del sistema de administracion.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

    return menu


def gestionar_platos(menu):
    while True:
        print("Menu de administracion:")
        print("1. Agregar plato")
        print("2. Editar plato")
        print("3. Eliminar plato")
        print("4. Mostrar menu")
        print("5. Salir")
        opcion = input("Selecciona una opcion (1-5): ")

        if opcion == "1":
            # Agregar plato
            nombre_plato = input("Ingrese el nombre del plato: ")
            precio = float(input("Ingrese el precio del plato: "))
            horario = input("Ingrese el horario (Desayuno (1), Almuerzo(2), Cena(3)): ")
            menu.append([nombre_plato, precio, horario])
            print(f"Plato '{nombre_plato}' agregado al menu {horario}.")
            print("----------------")
            print("----------------")
            print("----------------")

        elif opcion == "2":
            # Editar plato
            mostrar_menu(menu)
            numero_plato = int(input("Ingrese el numero del plato a editar: "))
            if numero_plato< len(menu) or numero_plato>0:
                plato = menu[int(numero_plato)]
                print(f"Plato a editar: '{plato[0]}' precio {plato[1]} menu {plato[2]}.")
                menu[numero_plato][0] = input("Ingrese el nuevo nombre del plato: ")
                menu[numero_plato][1] = float(input("Ingrese el nuevo precio del plato: "))
                menu[numero_plato][2] = input("Ingrese el nuevo horario (Desayuno (1), Almuerzo(2), Cena(3)): ")
                print(f"Plato '{menu[numero_plato][0]}' editado.")
                print("----------------")
                print("----------------")
                print("----------------")
                break
            else:
                print(f"Plato '{numero_plato}' no encontrado.")
                print("----------------")
                print("----------------")
                print("----------------")

        elif opcion == "3":
            # Eliminar plato
            mostrar_menu(menu)
            nombre_plato = input("Ingrese el nombre del plato a eliminar: ")
            encontrado = False
            for plato in menu:
                if plato[0] == nombre_plato:
                    menu.remove(plato)
                    print(f"Plato '{nombre_plato}' eliminado del menu.")
                    print("----------------")
                    print("----------------")
                    print("----------------")
                    encontrado = True
                    break
            if encontrado == False:
                print(f"Plato '{nombre_plato}' no encontrado.")
                print("----------------")
                print("----------------")
                print("----------------")

        elif opcion == "4":
            # Mostrar menu
            mostrar_menu(menu)

        elif opcion == "5":
            # Salir
            print("Saliendo del sistema de administracion.")
            break

def mostrar_menu(menu):
    if not menu:
        print("El menu esta vacio.")
    else:
        print("--- Menu ---")
        indice = 0
        for plato in menu:
            print(f"# {indice} Nombre: {plato[0]}, Precio: {plato[1]}, Horario: {plato[2]}")
            indice += 1

        print("----------------")
        print("----------------")
        print("----------------")


