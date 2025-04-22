import os

def mostrar_menu():
    
    print("---------------------")
    print("Mostrando el menu....")
    menu = obtener_info_menu()
    for plato in menu:
        print(plato.strip())
    print("------------------")

def buscar_plato_menu(nombre_plato):
    menu = obtener_info_menu()
    for plato in menu:
        if nombre_plato in plato:
            return True
    return False
    
def guardar_menu_en_archivo(menu):
    archivo = open('menu.txt','w')
    archivo.writelines(menu)
    print("Menu guardado exitosamente...")
    archivo.close()

def agregar_plato():
        menu = obtener_info_menu()
        nombre_plato = input("Ingresa el nombre del plato: ")
        encontrado = buscar_plato_menu(nombre_plato)
        if encontrado:
            print("El plato", nombre_plato,"ya existe en el menu.")
        else:
            precio = input("Ingresa el precio del plato: ")
            tipo_menu = input("Ingresa el tipo de menu (1) Desayuno, (2) Almuerzo, (3) Cena ")
            plato = "# " + str(len(menu)+1) + " Nombre: "+nombre_plato+" "+"Precio: "+precio+" Tipo de menu: "+ tipo_menu+"\n"
            menu.append(plato)
            guardar_menu_en_archivo(menu)
            print("Se agrego exitosamente al menu el plato", nombre_plato)

def modificar_plato():
        print("Modificando un plato...")
        menu = obtener_info_menu()
        if len(menu)>0:
            mostrar_menu()
            numero_plato = int(input("Ingresa el numero de plato a editar: "))
            if numero_plato < len(menu) and numero_plato >= 0:
                plato = menu[numero_plato-1].strip()
                plato_lista = plato.split()
                print("El plato a modificar es: ", plato_lista[3], "el precio es:", plato_lista[5])
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                nuevo_precio = input("Ingresa el nuevo precio: ")
                nuevo_tipo = input("Ingresa el nuevo tipo (1) Desayuno, (2) Almuerzo, (3) Cena: ")
                plato = "# " + str(numero_plato) + " Nombre: "+nuevo_nombre+" "+"Precio: "+nuevo_precio+" Tipo de menu: "+ nuevo_tipo+"\n"
                menu[numero_plato-1] = plato
                guardar_menu_en_archivo(menu)
                print("El plato:", nuevo_nombre,"se modifico exitosamente...")
            else:
                print("El plato", numero_plato,"no existe en el menu")
        else:
            print("El menu esta vacio.")
        

def eliminar_plato():
    print("Eliminando un plato...")
    menu = obtener_info_menu()
    if len(menu)>0:
        mostrar_menu()
        numero_plato = int(input("Ingresa el numero de plato a eliminar: "))
        if numero_plato < len(menu) and numero_plato >= 0:
            plato_eliminado = menu.pop(numero_plato-1)
            guardar_menu_en_archivo(menu)
            print("El plato eliminado es:" , plato_eliminado[0])
        else:
            print("El plato", numero_plato,"no existe en el menu")
    else:
        print("El menu esta vacio.")
    
def obtener_info_menu():
    menu = []
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'menu.txt')

    if not os.path.isfile(ruta_archivo):
        print("El archivo menu.txt no existe.")
        archivo =  open('menu.txt','w')
        archivo.close()
        print("El archivo menu.txt fue creado exitosamente.!")
        return menu
    archivo = open('menu.txt','r')
    contenido = archivo.readlines()

    return contenido

def mostrar_total():
    menu = obtener_info_menu()
    suma = 0
    for plato in menu:
        suma += int(plato.strip().split()[5])
    
    print("El total de los: ", len(menu),"platos es: ", suma)
    
    archivo = open('total_platos.txt','w')
    archivo.write(str(suma))
    archivo.close()

def sistema_administracion(menu):

    while True:
        print("1. Agregar platos...")
        print("2. Modificar un plato...")
        print("3. Eliminar un plato...")
        print("4. Ver el menu...")
        print("5. Ver total del menu...")
        print("6. Salir...")
        opcion_adm = input("Ingrese la opcion (1-5): ")

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
            break
    
    return menu
