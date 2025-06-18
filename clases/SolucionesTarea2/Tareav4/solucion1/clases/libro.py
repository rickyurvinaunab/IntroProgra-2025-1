class Libro:
    """
    CLASE DE LIBRO.

    Representa un libro con sus caracteristicas principales para
    la gestion en un sistema de biblioteca o inventario.
    """
    def __init__(self, isbn, titulo, especialidad, autor, editorial, edicion, anio, costo, cantidad):
        """
        Inicializa una nueva instancia de la clase Libro.

        Args:
            isbn (str): El numero ISBN unico del libro.
            titulo (str): El titulo del libro.
            especialidad (str): La especialidad o categoria a la que pertenece el libro.
            autor (str): El autor o autores del libro.
            editorial (str): La editorial que publico el libro.
            edicion (str): La edicion del libro.
            anio (str): El año de publicacion del libro.
            costo (float): El costo unitario del libro.
            cantidad (int): La cantidad de ejemplares disponibles en stock.
        """
        self.isbn = isbn
        self.titulo = titulo
        self.especialidad = especialidad
        self.autor = autor
        self.editorial = editorial
        self.edicion = edicion
        self.anio = anio
        self.costo = costo
        self.cantidad = cantidad

    def mostrar_info(self):
        """
        Muestra en la consola toda la informacion detallada del libro.
        """
        print("ISBN: " + self.isbn)
        print("Titulo: " + self.titulo)
        print("Especialidad: " + self.especialidad)
        print("Autor: " + self.autor)
        print("Editorial: " + self.editorial)
        print("Edicion: " + self.edicion)
        print("Año: " + self.anio)
        print("Costo: $" + str(self.costo))
        print("Cantidad disponible: " + str(self.cantidad))

    def a_linea_txt(self):
        """
        Convierte los atributos del libro en una cadena de texto.

        Esta cadena esta formateada para ser guardada en un archivo,
        usando el punto y coma (;) como separador entre cada atributo.

        Returns:
            str: Una cadena de texto con la informacion del libro.
        """
        return self.isbn + ";" + self.titulo + ";" + self.especialidad + ";" + self.autor + ";" + self.editorial + ";" + self.edicion + ";" + self.anio + ";" + str(self.costo) + ";" + str(self.cantidad)

    def disminuir_stock(self):
        """
        Disminuye la cantidad de ejemplares del libro en uno.

        Esta operacion se realiza solo si la cantidad actual de libros
        en stock es mayor que cero, evitando que el stock se vuelva negativo.
        """
        if self.cantidad > 0:
            self.cantidad -= 1