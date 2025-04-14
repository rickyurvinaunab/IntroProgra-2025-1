def sistema_cliente(menu):
    platos_elegidos = []
    cantidad_clientes = int(input("Ingrese la cantidad de clientes que van a consumir: "))

    for cliente in range(1, cantidad_clientes + 1):
        print("--- Cliente", cliente, "---")

        opcion_horario = ""
        while opcion_horario != "1" and opcion_horario != "2" and opcion_horario != "3":
            print("Que horario deseas?")
            print("1. Desayuno")
            print("2. Almuerzo")
            print("3. Cena")
            opcion_horario = input("Ingresa una opcion (1-3): ")

        if opcion_horario == "1":
            print("Menu Desayuno")
            platos_elegidos = opciones_menu(menu, 1, platos_elegidos)

        elif opcion_horario == "2":
            print("Menu Almuerzo")
            platos_elegidos = opciones_menu(menu, 2, platos_elegidos)

        elif opcion_horario == "3":
            print("Menu Almuerzo")
            platos_elegidos = opciones_menu(menu, 3, platos_elegidos)

        else:
            print("Opcion no valida. Por favor, elige una opcion correcta.")
            continue


    mostrar_resumen_cuenta(cantidad_clientes, platos_elegidos)

def opciones_menu(menu, opcion, platos_elegidos):
    contador_platos = 0
    indice_plato = 0
    for plato in menu:
        if plato[2] == str(opcion):
            contador_platos += 1
            print(indice_plato, ". ", plato[0], "- Precio: $", plato[1])
            print("----------------")
        indice_plato += 1
    if contador_platos > 0:
        platos_elegidos = seleccion_plato(menu, platos_elegidos)
    else:
        print("No hay platos disponibles para el desayuno.")
        print("----------------")
        print("----------------")
        print("----------------")

    return platos_elegidos

def seleccion_plato(menu, platos_elegidos):
    plato_seleccionado = int(input("Seleccione el plato que desea consumir: "))
    platos_elegidos.append(menu[plato_seleccionado])

    return platos_elegidos

def mostrar_resumen_cuenta(total_clientes, platos_elegidos):
    print("Resumen de la cuenta:")
    print("Total de clientes:", total_clientes)
    print("Total a pagar: $",calcular_total_cuenta(platos_elegidos))
    print("----------------")
    print("----------------")
    print("----------------")

def calcular_total_cuenta(platos_elegidos):
    total_cuenta = 0
    for plato in platos_elegidos:
        total_cuenta += plato[1]
    return total_cuenta