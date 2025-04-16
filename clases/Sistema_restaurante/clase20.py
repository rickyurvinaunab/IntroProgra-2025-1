
def sistema_administracion(menu):
    print("Sistema de administracion")

    while True:
        print("1. Agregar")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Ver menu")
        print("5. Salir")

        opcion = input("Ingresa la opcion (1-5)")

        if opcion == "1":
            print("Sistema para agregar")
            nombre_plato = input("Ingresa el nombre del plato")
            precio = input("Ingresa el precio del plato")
            tipo = input("Ingresa el menu (1) Desayuno, (2) Almuerzo, (3) Cena: ")
            menu.append([nombre_plato, precio, tipo])
        elif opcion == "2":
            print("Sistema para editar")
            if len(menu)>0:
                mostrar_menu(menu)
                numero_plato = int(input("ingresa el numero de plato a editar: "))
                plato_a_editar = menu[numero_plato]
                print("El plato a editar es: ", plato_a_editar[0])
                plato_a_editar[0] = input("Ingresa el nuevo nombre del plato: ")
                plato_a_editar[1] =  int(input("ingresa el nuevo precio: "))
                plato_a_editar[2] = int(input("ingresa el tipo (1) Desayuno, (2) Almuerzo, (3) Cena "))
                print("Plato", plato_a_editar[0],"editado correctamente...")
                print("-------------")
                print()
        elif opcion == "3":
            print("3. Sistema para eliminar")
            if len(menu)>0:
                mostrar_menu(menu)
                numero_plato = int(input("Ingresa el numero del plato a eliminar: "))

                plato = menu.pop(numero_plato)
                print("El plato", plato[0],"Se elimino correctamente....")

        elif opcion == "4":
            mostrar_menu(menu)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

    return menu

def mostrar_menu(menu):
    print("--------------------")
    print("Mostrando menu...")

    indice = 0
    for plato in menu:
        print('#', indice, 'Nombre: ', plato[0],'Precio: ', plato[1],"Tipo:", plato[2])
        indice += 1

menu = []
sistema_administracion(menu)