import os  # Importa el módulo os para manejar rutas de archivos

def mostrar_menu():
    print("---------------------")
    print("Mostrando el menu....")
    menu = obtener_info_menu()  # Carga el contenido del archivo menu.txt
    for plato in menu:
        print(plato.strip())  # Imprime cada plato sin espacios extras
    print("------------------")

def buscar_plato_menu(nombre_plato):
    menu = obtener_info_menu()  # Obtiene el menú actual
    for plato in menu:
        if nombre_plato in plato:  # Busca si el nombre del plato ya existe
            return True
    return False

def guardar_menu_en_archivo(menu):
    archivo = open('menu.txt','w')  # Abre el archivo en modo escritura
    archivo.writelines(menu)  # Escribe la lista completa del menú en el archivo
    print("Menu guardado exitosamente...")
    archivo.close()  # Cierra el archivo

def agregar_plato():
    menu = obtener_info_menu()  # Carga el menú actual
    nombre_plato = input("Ingresa el nombre del plato: ")
    encontrado = buscar_plato_menu(nombre_plato)  # Verifica si ya existe

    if encontrado:
        print("El plato", nombre_plato,"ya existe en el menu.")
    else:
        precio = input("Ingresa el precio del plato: ")
        tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena ")
        # Crea una cadena con los datos del nuevo plato
        plato = "# " + str(len(menu)+1) + " Nombre: "+nombre_plato+" "+"Precio: "+precio+" Tipo de menu: "+ tipo_menu+"\n"
        menu.append(plato)  # Agrega el nuevo plato a la lista
        guardar_menu_en_archivo(menu)  # Guarda los cambios
        print("Se agrego exitosamente al menu el plato", nombre_plato)

def modificar_plato():
    print("Modificando un plato...")
    menu = obtener_info_menu()  # Carga el menú

    if len(menu)>0:
        mostrar_menu()  # Muestra el menú actual
        numero_plato = int(input("Ingresa el numero de plato a editar: "))  # Pide el número del plato

        if numero_plato < len(menu) and numero_plato >= 0:
            plato = menu[numero_plato-1].strip()  # Selecciona el plato indicado
            plato_lista = plato.split()  # Separa los datos del plato
            print("El plato a modificar es: ", plato_lista[3], "el precio es:", plato_lista[5])
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nuevo_precio = input("Ingresa el nuevo precio: ")
            nuevo_tipo = input("Ingresa el nuevo tipo (1) Desayuno, (2) Almuerzo, (3) Cena: ")
            # Crea el nuevo registro con los datos actualizados
            plato = "# " + str(numero_plato) + " Nombre: "+nuevo_nombre+" "+"Precio: "+nuevo_precio+" Tipo de menu: "+ nuevo_tipo+"\n"
            menu[numero_plato-1] = plato  # Reemplaza el plato en la lista
            guardar_menu_en_archivo(menu)  # Guarda los cambios en el archivo
            print("El plato:", nuevo_nombre,"se modifico exitosamente...")
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")

def eliminar_plato():
    print("Eliminando un plato...")
    menu = obtener_info_menu()  # Carga el menú actual

    if len(menu)>0:
        mostrar_menu()  # Muestra el menú
        numero_plato = int(input("Ingresa el numero de plato a eliminar: "))
        if numero_plato < len(menu) and numero_plato >= 0:
            plato_eliminado = menu.pop(numero_plato-1)  # Elimina el plato indicado
            guardar_menu_en_archivo(menu)  # Guarda el menú actualizado
            print("El plato eliminado es:" , plato_eliminado[0])
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")

def obtener_info_menu():
    menu = []  # Lista vacía para almacenar los platos
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'menu.txt')  # Ruta del archivo menu.txt

    if not os.path.isfile(ruta_archivo):  # Verifica si el archivo no existe
        print("El archivo menu.txt no existe.")
        archivo =  open('menu.txt','w')  # Crea el archivo vacío, si el archivo no existe
        archivo.close()
        print("El archivo menu.txt fue creado exitosamente.!")
        return menu  # Retorna lista vacía

    archivo = open('menu.txt','r')  # Abre el archivo en modo lectura
    contenido = archivo.readlines()  # Lee todas las líneas del archivo
    return contenido  # Devuelve las líneas como lista

def mostrar_total():
    menu = obtener_info_menu()  # Carga el menú
    suma = 0

    for plato in menu:
        suma += int(plato.strip().split()[5])  # Extrae el precio (posición 5) y suma

    print("El total de los: ", len(menu),"platos es: ", suma)

    archivo = open('total_platos.txt','w')  # Crea un archivo para guardar el total
    archivo.write(str(suma))  # Escribe el total
    archivo.close()

def sistema_administracion(menu):
    while True:
        # Menú principal del sistema de administración
        print("1. Agregar platos...")
        print("2. Modificar un plato...")
        print("3. Eliminar un plato...")
        print("4. Ver el menu...")
        print("5. Ver total del menu...")
        print("6. Salir...")
        opcion_adm = input("Ingrese la opcion (1-5): ")

        # Llama a la función correspondiente según la opción elegida
        if opcion_adm == "1":
            agregar_plato()
        elif opcion_adm =="2":
            modificar_plato()
        elif opcion_adm == "3":
            eliminar_plato()
        elif opcion_adm == "4":
            mostrar_menu()
        elif opcion_adm == "5":
            mostrar_total()
        elif opcion_adm == "6":
            print("Saliendo del sistema de adminsitracion")
            break  # Sale del bucle