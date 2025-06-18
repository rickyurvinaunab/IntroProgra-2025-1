from clase_libreria import Libreria
from clase_libro import Libro
from clase_persona import Persona
from acciones_menu import ingresar_persona, ingresar_libro, pedir_libros, devolver_libro, ver_libros_prestados, personas_con_prestamos
from graficos import mostrar_total_a_pagar


lista_personas = []
lista_libros = []
libreria1 = Libreria("Libreria Alba")

while True:
    print("1. Ingresas Personas")
    print("2. Ingresas Libros")
    print("3. Gestionar Prestamos")
    print("4. Ver Libros Prestados")
    print("5. Ver Personas con Libros Prestado")
    print("6. Ver Grafico de monto a pagar")
    print("7. Salir")
    opcion = input("Ingresa una opcion (1-7)")

    if opcion == "1":
        lista_personas = ingresar_persona(lista_personas)
    elif opcion == "2":
        lista_libros = ingresar_libro(lista_libros, libreria1)
    elif opcion == "3":
        print ("Escoge cual deseas:")
        print("1.- Pedir Libros" )  
        print("2.- Devolver Libros:")
        opcion = input("Ingresa una opcion (1-2)")
        if opcion == "1":
            pedir_libros(lista_personas, lista_libros)
        elif opcion == "2":
            devolver_libro(lista_personas, lista_libros)
    elif opcion == "4":
        lista_libros = ver_libros_prestados(lista_libros)
    elif opcion == "5":
        personas_con_prestamos(lista_personas)
    elif opcion == "6":
        mostrar_total_a_pagar(lista_personas)
    elif opcion == "7":
        print("Saliendo del sistema....")
        break
