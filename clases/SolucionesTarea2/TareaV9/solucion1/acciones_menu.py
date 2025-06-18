from clase_persona import Persona
from clase_libro import Libro

def ingresar_persona(lista_personas):
    """
    Solicita datos de persona al usuario, crea un objeto Persona 
    y lo agrega a la lista de personas.

    Argumentos:
        lista_personas (list): Lista que contiene objetos de tipo Persona.

    Return:
        list: Lista actualizada con la nueva persona incluida
    """
    nombre = input("ingresa tu nombre:")
    apellido = input("ingresa tu apellido:")
    rut = int(input("ingresa tu rut:"))
    persona = Persona(nombre, apellido, rut)
    lista_personas.append(persona)
    print("Persona agregada con exito")
    return lista_personas


def ingresar_libro(lista_libros, libreria1):
    """
    Solicita al usuario los datos de un nuevo libro, lo crea como objeto
    y lo agrega a la lista de libros y a la librería.

    Argumentos:
        lista_libros (list): Lista que contiene objetos de tipo Libro.
        libreria1 (Libreria): Objeto de la clase Libreria donde se agregará el libro.

    Return:
        list: Lista actualizada con el nuevo libro incluido.

    """
    nombre = input("Ingresar nombre del libro: ")
    isbn = int(input("ingresa isbn del libro:"))
    titulo = input("ingresa el titulo del libro:")
    especialidad = input("ingresa la especialidad del libro:")
    autor = input("ingresa el autor del libro:")
    editorial = input("ingresa la editorial del libro:")
    edicion = input("ingresa la edicion del libro:")
    anio = int(input("ingresa el año de estreno del libro:"))
    costo = float(input("ingresa el costo del libro:"))
    libro = Libro(isbn, titulo, especialidad, autor, edicion, editorial, anio, costo)
    lista_libros.append(libro)
    libreria1.agregar_libro(libro)
    print("Libro ingresado con exito")
    return lista_libros


def pedir_libros(lista_personas, lista_libros):
    """
    Permite a una persona que se identifique por su rut para solicitar un libro ingresando la isbn de este. 
    Si se encuentra la persona y el libro, se registra el préstamo.

    Argumentos:
        lista_personas (list): Lista de objetos de tipo Persona registrados en el sistema.
        lista_libros (list): Lista de objetos de tipo Libro disponibles en la biblioteca.

    """
    rut_buscado = int(input("Ingrese su rut: "))
    persona_encontrada = None
    for persona in lista_personas:
        if persona.rut == rut_buscado:
            persona_encontrada = persona
            break
    if persona_encontrada:
        print("Libros disponibles:")
        for libro in lista_libros:
            print(f"isbn:{libro.isbn} - titulo: {libro.titulo} - especialidad: {libro.especialidad} - autor: {libro.autor} - edicion: {libro.edicion} - editorial: {libro.editorial} - anio: {libro.anio} - costo: {libro.costo}")
    else:
        persona_encontrada = None
        print("El rut ingresado no se ha encontrado en el sistema.")
        
    isbn_solicitado = int(input("Ingrese el isbn del libro que desea: "))
    libro_encontrado = None
    for libro in lista_libros:
        if libro.isbn == isbn_solicitado:
            libro_encontrado = libro
            break
    if libro_encontrado:
        libro_encontrado.prestar_libro (persona_encontrada)
        print("Libro pedido con exito")
    else:
        print("No se encontró un libro con el isbn ingresado o el Rut ingresado no se ha encontrado en el sistema.")

    return lista_personas, lista_libros

def devolver_libro(lista_personas, lista_libros):
    """
    Permite a una persona devolver un libro que haya sido prestado anteriormente.
    
    Argumentos:
        lista_personas (list): Lista de objetos Persona.
        lista_libros (list): Lista de objetos Libro.
    """
    rut = int(input("Ingrese su rut: "))
    persona = None
    for persona in lista_personas:
        if persona.rut == rut:
            break
    if persona and persona.libros:
        print("Libros que puede devolver:")
        for libro in persona.libros:
            print(f"isbn:{libro.isbn} - titulo: {libro.titulo} - especialidad: {libro.especialidad} - autor: {libro.autor} - edicion: {libro.edicion} - editorial: {libro.editorial} - anio: {libro.anio} - costo: {libro.costo}")
        isbn = int(input("Ingrese el ISBN del libro a devolver: "))
        for libro in persona.libros:
            if libro.isbn == isbn:
                libro.devolver_libro(persona)
                print(f"Libro '{libro.titulo}' devuelto correctamente.")
                return lista_libros
        print("No se encontró el libro con ese ISBN.")
    else:
        print("No se encontró la persona o no tiene libros prestados.")

def ver_libros_prestados(lista_libros):
    """
    Muestra los libros que están actualmente prestados.
    
    Argumentos:
        lista_libros (list): Lista de objetos Libro.
    """
    print("Libros prestados:")
    for libro in lista_libros:
        if libro.prestado:
            print(f"isbn:{libro.isbn} - titulo: {libro.titulo} - especialidad: {libro.especialidad} - autor: {libro.autor} - edicion: {libro.edicion} - editorial: {libro.editorial} - anio: {libro.anio} - costo: {libro.costo}")

def personas_con_prestamos(lista_personas):
    """
    Muestra las personas que han solicitado libros prestados.
    
    Argumentos:
        lista_personas (list): Lista de objetos Persona.
    """
    print("Personas con libros prestados:")
    for persona in lista_personas:
        if persona.libros:
            print(f"{persona.nombre} {persona.apellido} (rut: {persona.rut})")
            for libro in persona.libros:
                print(f"isbn:{libro.isbn} - titulo: {libro.titulo} - especialidad: {libro.especialidad} - autor: {libro.autor} - edicion: {libro.edicion} - editorial: {libro.editorial} - anio: {libro.anio} - costo: {libro.costo}")
    
