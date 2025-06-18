class Libreria:
    """
    Clase que almacena libros y gestiona la lista de libros prestados.
    Permite agregar libros con su isbn, titulo, especialidad, autor, editorial, edicion, anio, costo.
    obtener la lista de libros prestado y tambien obtener la lista para luego graficarlos.
    """
    def __init__(self, nombre):
        """
        Inicia la libreria con un nombre y una lista vacia de libros.

        Parametros:

        nombre (str) = nombre de la libreria
        """
        self.nombre = nombre
        self.lista_libros = []

    def __str__(self):
        """
        Retorna el nombre de la libreria.

        Returns:
        str: nombre de la libreria.
        """
        return "Bienvenidos a la: " + self.nombre
    
    def agregar_libro(self, libro):
        """
        Agrega un libro a la libreria.

        Parametros:
        libro (Libro): objeto de la clase Libreria a agregar.
        """
        self.lista_libros.append(libro)

