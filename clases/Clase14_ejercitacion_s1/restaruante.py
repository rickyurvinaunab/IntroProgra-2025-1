print("Bienvenido al Restaurante Quiteño libre")

total_cuenta = 0
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

    nombre_plato = ""
    precio = 0
    horario = ""

    if opcion_horario == "1":
        horario = "Desayuno"
        opcion_plato = ""
        while opcion_plato not in ["1", "2", "3"]:
            print("--- Menu de Desayuno ---")
            print("1. Cafe + Croissant ($3000)")
            print("2. Jugo + Sandwich ($4500)")
            print("3. Panqueques con miel ($5000)")
            opcion_plato = input("Selecciona tu plato (1-3): ")

        if opcion_plato == "1":
            nombre_plato = "Cafe + Croissant"
            precio = 3000
        elif opcion_plato == "2":
            nombre_plato = "Jugo + Sandwich"
            precio = 4500
        elif opcion_plato == "3":
            nombre_plato = "Panqueques con miel"
            precio = 5000

    elif opcion_horario == "2":
        horario = "Almuerzo"
        opcion_plato = ""
        while opcion_plato not in ["1", "2", "3", "4"]:
            print("--- Menu de Almuerzo ---")
            print("1. Ensalada + Pollo ($6000)")
            print("2. Pasta bolonesa ($7500)")
            print("3. Filete con papas ($9000)")
            print("4. Hamburguesa con bebida ($6500)")
            opcion_plato = input("Selecciona tu plato (1-4): ")

        if opcion_plato == "1":
            nombre_plato = "Ensalada + Pollo"
            precio = 6000
        elif opcion_plato == "2":
            nombre_plato = "Pasta bolonesa"
            precio = 7500
        elif opcion_plato == "3":
            nombre_plato = "Filete con papas"
            precio = 9000
        elif opcion_plato == "4":
            nombre_plato = "Hamburguesa con bebida"
            precio = 6500

    elif opcion_horario == "3":
        horario = "Cena"
        opcion_plato = ""
        while opcion_plato not in ["1", "2", "3"]:
            print("--- Menu de Cena ---")
            print("1. Sopa + Plato fuerte ($8000)")
            print("2. Sushi ($10000)")
            print("3. Pizza + Bebida ($7500)")
            opcion_plato = input("Selecciona tu plato (1-3): ")

        if opcion_plato == "1":
            nombre_plato = "Sopa + Plato fuerte"
            precio = 8000
        elif opcion_plato == "2":
            nombre_plato = "Sushi"
            precio = 10000
        elif opcion_plato == "3":
            nombre_plato = "Pizza + Bebida"
            precio = 7500

    cumple = ""
    while cumple != "si" and cumple != "no":
        cumple = input("Es tu cumpleanos hoy? (si/no): ")

    if cumple == "si":
        descuento = precio * 0.35
        precio_final = precio - descuento
        aplica_descuento = "Si"
    else:
        precio_final = precio
        aplica_descuento = "No"

    total_cuenta += precio_final

    print("--- Resumen del pedido del cliente", cliente, "---")
    print("Horario seleccionado:", horario)
    print("Plato elegido:", nombre_plato)
    print("Precio original: $", precio)
    print("Descuento aplicado?:", aplica_descuento)
    print("Precio final a pagar: $", round(precio_final, 2))

print("--- Total de la cuenta para todos los clientes ---")
print("Total a pagar: $", round(total_cuenta, 2))