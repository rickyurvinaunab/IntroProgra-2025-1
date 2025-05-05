# Se importa el módulo os para trabajar con rutas de archivos
import os


# Funcion para mostrar todos los platos del menu actual
def mostrar_menu():
    print("---------------------")
    print("Mostrando el menu....")
    menu = obtener_info_menu()  # Se obtiene la lista de platos desde el archivo menu.txt
    indice = 1
    for plato in menu:
        datos = plato.strip().split(";")
        if len(datos) == 3:
            nombre, precio, tipo = datos
            print(f"{indice}. {nombre} - Precio: {precio} - Tipo: {tipo}")
            indice += 1
    print("------------------")

# Funcion que busca si un plato ya existe en el menu
def buscar_plato_menu(nombre_plato):
    menu = obtener_info_menu()
    for plato in menu:
        datos = plato.strip().split(";")
        if len(datos) >= 1 and nombre_plato == datos[0]:  # Comparar nombre exacto
            return True
    return False  # Si no se encuentra, retorna falso

# Funcion que guarda el menu completo en el archivo menu.txt
def guardar_menu_en_archivo(menu):
    archivo = open('menu.txt','w')  # Se abre el archivo en modo agregar
    archivo.writelines(menu)  # Se escriben todas las líneas del menu
    print("Menu guardado exitosamente...")
    archivo.close()

# Funcion para agregar un nuevo plato al menu
def agregar_plato():
    menu = obtener_info_menu()
    nombre_plato = input("Ingresa el nombre del plato: ")
    encontrado = buscar_plato_menu(nombre_plato)
    if encontrado:
        print("El plato", nombre_plato,"ya existe en el menu.")
    else:
        precio = input("Ingresa el precio del plato: ")
        tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena: ")
        tipos = ["Desayuno", "Almuerzo", "Cena"]
        if tipo_menu in ["1", "2", "3"]:
            tipo_texto = tipos[int(tipo_menu) - 1]
        else:
            tipo_texto = "Desconocido"
        plato = f"{nombre_plato};{precio};{tipo_texto}\n"
        menu.append(plato)  # Se añade a la lista del menu
        guardar_menu_en_archivo(menu)  # Se guarda el nuevo menu
        print("Se agrego exitosamente al menu el plato", nombre_plato)

# Funcion para modificar un plato existente
def modificar_plato():
    print("Modificando un plato...")
    menu = obtener_info_menu()
    if len(menu) > 0:  # Si el menu no esta vacio
        mostrar_menu()
        numero_plato = int(input("Ingresa el numero de plato a editar: "))
        if 1 <= numero_plato <= len(menu):
            plato = menu[numero_plato-1].strip()
            datos = plato.split(";")
            if len(datos) == 3:
                nombre_actual, precio_actual, tipo_actual = datos
                print(f"El plato a modificar es: {nombre_actual} - Precio: {precio_actual} - Tipo: {tipo_actual}")
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                nuevo_precio = input("Ingresa el nuevo precio: ")
                nuevo_tipo = input("Ingresa el nuevo tipo (1) Desayuno, (2) Almuerzo, (3) Cena: ")
                tipos = ["Desayuno", "Almuerzo", "Cena"]
                if nuevo_tipo in ["1", "2", "3"]:
                    nuevo_tipo_texto = tipos[int(nuevo_tipo) - 1]
                else:
                    nuevo_tipo_texto = tipo_actual
                plato_modificado = f"{nuevo_nombre};{nuevo_precio};{nuevo_tipo_texto}\n"
                menu[numero_plato-1] = plato_modificado
                guardar_menu_en_archivo(menu)
                print("El plato:", nuevo_nombre,"se modifico exitosamente...")
            else:
                print("Formato incorrecto del plato seleccionado.")
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")

# Funcion para eliminar un plato del menu
def eliminar_plato():
    print("Eliminando un plato...")
    menu = obtener_info_menu()
    if len(menu) > 0:
        mostrar_menu()
        numero_plato = int(input("Ingresa el numero de plato a eliminar: "))
        if 1 <= numero_plato <= len(menu):
            plato_eliminado = menu.pop(numero_plato-1)  # Se elimina de la lista
            guardar_menu_en_archivo(menu)  # Se guarda el nuevo menu sin ese plato
            datos = plato_eliminado.strip().split(";")
            nombre_eliminado = datos[0] if len(datos) > 0 else ""
            print("El plato eliminado es:", nombre_eliminado)
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")

# Funcion para leer el contenido del archivo menu.txt
def obtener_info_menu():
    menu = []
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'menu.txt')  # Ruta relativa

    if not os.path.isfile(ruta_archivo):  # Si el archivo no existe
        print("El archivo menu.txt no existe.")
        archivo = open(ruta_archivo,'w')  # Se crea el archivo
        print("El archivo menu.txt fue creado exitosamente.!")
        archivo.close()
        return menu
    archivo = open('menu.txt','r')  # Se abre el archivo en modo agregar
    contenido = archivo.readlines()
    return contenido

# Funcion que calcula el total de todos los precios del menu
def mostrar_total():
    menu = obtener_info_menu()
    suma = 0
    for plato in menu:
        datos = plato.strip().split(";")
        if len(datos) >= 2:
            suma += int(datos[1])  # Se obtiene el precio (índice 1) y se suma

    print("El total de los:", len(menu), "platos es:", suma)

    archivo = open('total_platos.txt','w')
    archivo.write(str(suma))

# Funcion que calcula el total de dinero gastado en todas las ordenes registradas
def mostrar_total_ordenes(ordenes):
    total = 0
    for orden in ordenes:
        datos = orden.strip().split(";")
        precio = float(datos[2])  # Se intenta convertir directamente a float
        total += precio
    return total

# Funcion principal del sistema de administracion
def sistema_administracion(ordenes):
    print("Sistema de administracion...")
    while True:
        # Menu de opciones administrativas
        print("1. Agregar platos...")
        print("2. Modificar un plato...")
        print("3. Eliminar un plato...")
        print("4. Ver el menu...")
        print("5. Ver total del menu...")
        print("6. Ver total de ordenes...")
        print("7. Salir...")
        opcion_adm = input("Ingrese la opcion (1-7): ")

        if opcion_adm == "1":
            agregar_plato()
        elif opcion_adm == "2":
            modificar_plato()
        elif opcion_adm == "3":
            eliminar_plato()
        elif opcion_adm == "4":
            mostrar_menu()
        elif opcion_adm == "5":
            mostrar_total()
        elif opcion_adm == "6":
            total = mostrar_total_ordenes(ordenes)
            print("El total de todas las ordenes es:", total)
        elif opcion_adm == "7":
            print("Saliendo del sistema de administracion")
            break