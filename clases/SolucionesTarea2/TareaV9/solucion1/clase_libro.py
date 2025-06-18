class Libro:
    """
    Clase que permite representar un libro con su informacion basica 
    y permite ver si esta prestado a alguien o aun no.

    Atributos:

    isbn (int) = isbn del libro
    titulo (str) = titulo del libro
    especialidad (str) = especialidad del libro
    autor (str) = autor del libro
    editorial (str) = editorial del libro
    edicion (str) = edicion a la que pertenece libro
    anio (int) = anio de estreno del libro
    costo (int) = precio del libro
    prestado (bool) = el libro esta prestado o no
    """

    def __init__(self, isbn, titulo, especialidad, autor, edicion, editorial, anio, costo):
        """
        Inicializa un libro con sus atributos basicos.

        Parametros:
        isbn (int) = isbn del libro
        titulo (str) = titulo del libro
        especialidad (str) = especialidad del libro
        autor (str) = autor del libro
        edicion (str) = edicion a la que pertenece libro
        editorial (str) = editorial del libro
        anio (int) = anio de estreno del libro
        costo (int) = precio del libro
        prestado (bool) = el libro esta prestado o no


        """
        self.isbn = isbn
        self.titulo = titulo 
        self.especialidad = especialidad 
        self.autor = autor 
        self.edicion = edicion
        self.editorial = editorial 
        self.anio = anio 
        self.costo = costo
        self.prestado = False

    def prestar_libro(self,persona):
        self.prestado = True
        persona.libros.append(self)

    def devolver_libro(self, persona):
        self.prestado = False

        for libro in persona.libros:
            if self.titulo == libro.titulo:
                persona.libros.remove(libro)
        