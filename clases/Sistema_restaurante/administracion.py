# Se importa el módulo os para trabajar con rutas de archivos
import os

# Funcion para mostrar todos los platos del menu actual
def mostrar_menu():
    print("---------------------")
    print("Mostrando el menu....")
    menu = obtener_info_menu()  # Se obtiene la lista de platos desde el archivo menu.txt
    for plato in menu:
        print(plato.strip())  # Se imprime cada plato quitando saltos de línea
    print("------------------")

# Funcion que busca si un plato ya existe en el menu
def buscar_plato_menu(nombre_plato):
    menu = obtener_info_menu()
    for plato in menu:
        if nombre_plato in plato:  # Si el nombre está en alguna línea del menu
            return True
    return False  # Si no se encuentra, retorna falso

# Funcion que guarda el menu completo en el archivo menu.txt
def guardar_menu_en_archivo(menu):
    archivo = open('menu.txt','w')  # Se abre el archivo en modo escritura (sobrescribe todo)
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
        tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena ")
        # Se construye el string del nuevo plato con su formato
        plato = "# " + str(len(menu)+1) + " Nombre: "+nombre_plato+" Precio: "+precio+" Tipo de menu: "+ tipo_menu+"\n"
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
        if numero_plato < len(menu) and numero_plato >= 0:
            plato = menu[numero_plato-1].strip()
            plato_lista = plato.split()  # Se divide en palabras para acceder por indices
            print("El plato a modificar es:", plato_lista[3], "el precio es:", plato_lista[5])
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nuevo_precio = input("Ingresa el nuevo precio: ")
            nuevo_tipo = input("Ingresa el nuevo tipo (1) Desayuno, (2) Almuerzo, (3) Cena: ")
            # Se reconstruye la línea del plato con los nuevos datos
            plato = "# " + str(numero_plato) + " Nombre: "+nuevo_nombre+" Precio: "+nuevo_precio+" Tipo de menu: "+ nuevo_tipo+"\n"
            menu[numero_plato-1] = plato  # Se reemplaza en la posición correspondiente
            guardar_menu_en_archivo(menu)
            print("El plato:", nuevo_nombre,"se modifico exitosamente...")
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
        if numero_plato < len(menu) and numero_plato >= 0:
            plato_eliminado = menu.pop(numero_plato-1)  # Se elimina de la lista
            guardar_menu_en_archivo(menu)  # Se guarda el nuevo menu sin ese plato
            print("El plato eliminado es:", plato_eliminado[0])
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
        archivo = open('menu.txt','w')  # Se crea vacio
        archivo.close()
        print("El archivo menu.txt fue creado exitosamente.!")
        return menu
    archivo = open('menu.txt','r')  # Se abre para lectura
    contenido = archivo.readlines()
    archivo.close()
    return contenido

# Funcion que calcula el total de todos los precios del menu
def mostrar_total():
    menu = obtener_info_menu()
    suma = 0
    for plato in menu:
        suma += int(plato.strip().split()[5])  # Se obtiene el precio (índice 5) y se suma

    print("El total de los:", len(menu), "platos es:", suma)

    archivo = open('total_platos.txt','w')  # Se guarda el total en un archivo
    archivo.write(str(suma))
    archivo.close()

# Funcion que actualiza los indices de los platos despues de agregar, modificar o eliminar
def actualizar_indices():
    menu = obtener_info_menu()
    menu_nuevo = []
    indice = 1
    for plato in menu:
        datos = plato.split()
        # Se reconstruye cada linea con su nuevo indice
        plato_str = "# " + str(indice) + " Nombre: "+datos[3]+" Precio: "+datos[5]+" Tipo de menu: "+ datos[9]+"\n"
        indice += 1
        menu_nuevo.append(plato_str)
    guardar_menu_en_archivo(menu_nuevo)

# Funcion que calcula el total de dinero gastado en todas las ordenes registradas
def mostrar_total_ordenes(ordenes):
    total = 0
    for orden in ordenes:
        if "Orden" not in orden:  # Se omiten las lineas que indican "Orden #:"
            datos = orden.split()
            costo = datos[5]  # Se extrae el precio (índice 5)
            total += float(costo)
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
            actualizar_indices()
        elif opcion_adm == "2":
            modificar_plato()
            actualizar_indices()
        elif opcion_adm == "3":
            eliminar_plato()
            actualizar_indices()
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