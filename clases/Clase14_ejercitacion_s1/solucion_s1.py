print("Bienvenido al sistema")
opcion  = ""
while opcion != "1" and opcion != "2" and opcion != "3":
    print("0. Salir")
    print("1. Opcion 1 Sistema Arriendos")
    print("2. Opcion 2 Sistema calculo de interes")
    print("3. Opcion 3 Sistema de Pintado")
    opcion = input("Ingrese la opcion deseada (1-3) o 0 para salir: ")
    if opcion == "0":
        print("Vuelva pronto")
        break
    elif opcion == "1":
        print("Bienvenido al Sistema de Arriendos")
        cant_clientes =  int(input("Ingrese la cantidad de clientes: "))
        suma_total = 0
        suma_dias = 0
        total_departamentos = 0
        for cliente in range(cant_clientes):
            suma_cliente = 0
            descuento = 0
            precio = 0
            nombre = input("Ingrese el nombre del cliente "+ str(cliente+1)+": ")
            rut = input("Ingrese el rut del cliente: ")
            cant_departamentos = int(input("Ingrese la cantidad de departamentos: "))
            total_departamentos += cant_departamentos
            for depa in range(cant_departamentos):
                cantidad_hab = int(input("Ingrese la cantidad de habitaciones del departamento"+ str(depa+1)+ ": "))
                cant_dias =  int(input("Ingrese la cantidad de dias: "))
                suma_dias += cant_dias
                if cantidad_hab == 1:
                    precio = 30000
                elif cantidad_hab == 2:
                    precio = 45000
                elif cantidad_hab == 3:
                    precio = 55000
                if cant_dias >7:
                    descuento = 0.085
                precio_dias = precio * cant_dias
                total_dep_cliente = precio_dias - (precio_dias * descuento)
                suma_cliente += total_dep_cliente
                print("El precio del departamento es: ", total_dep_cliente)
                print("El cliente", nombre, "debe pagar: ", total_dep_cliente, "por el departamento de:", cantidad_hab, "habitaciones","por ", cant_dias, "dias")
            print("El cliente", nombre, "debe pagar un total de: ", suma_cliente, "por",cant_departamentos,  " departamentos")
            suma_total += suma_cliente
        print("---------------Resumen---------------")
        print("Cantidad de departamentos arrendados", total_departamentos)
        print("Promedio de dias de arriendo", suma_dias / cant_clientes)
        print("Promedio del monto final, considerando todos los arriendos", suma_total / cant_clientes)
        print("Cantidad de departamentos arrendados por clientes", total_departamentos / cant_clientes)
    elif opcion == "2":
        print("Bienvenido al Sistema de Calculo de Interes")
        capital = float(input("Ingrese el monto a invertir: "))
        tasa = 0.02
        tiempo = int(input("Ingrese el tiempo en meses: "))
        monto_interes = (capital * tasa * tiempo)
        capital_total =  capital + monto_interes
        print("El interes es: ", monto_interes)
        print("El capital total es: ", capital_total)
    elif opcion == "3":
        print("Bienvenido al Sistema de Pintado")
        suma_areas = 0
        for i in range(4):
            print("Pared", i+1)
            largo = float(input("Ingrese el largo de la pared: "))
            alto = float(input("Ingrese el alto de la pared: "))
            area = largo * alto
            suma_areas += area
        print("Dimensiones de laPuerta")
        largo_p = float(input("Ingrese el largo de la puerta: "))
        alto_p = float(input("Ingrese el alto de la puerta: "))
        area_p = largo_p * alto_p
        area_total = suma_areas - area_p
        pintura = area_total /3
        print("El total de pintura necesario es: ", round(pintura, 2),"litros")
    print("-------------------------------------")
    opcion = ""
