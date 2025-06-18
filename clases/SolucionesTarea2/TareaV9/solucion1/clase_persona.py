class Persona:

    def __init__(self, nombre, apellido, rut):
        """
        Inicializa una instancia de la clase Persona.

        Argumentos:
            nombre (str): nombre de la persona.
            apellido (str): apellido de la persona.
            rut (int): rut de la persona.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.libros = []

    def __str__(self):
        return ""

    def agregar_libro(self, libro):
        """
    Agrega un libro a la lista de préstamos de la persona si el libro no está prestado.

    Argumentos:
        libro (Libro): Objeto de tipo Libro que se desea agregar.
    """
        if libro.prestado == False: 
            self.libros.append(libro)
        else:
            print("El libro:"+libro.nombre+"no esta disponible...")


        