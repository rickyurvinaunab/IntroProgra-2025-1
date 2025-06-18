class Libreria:
    """
    Clase que almacena libros y gestiona la lista de libros prestados.
    Permite agregar libros con su isbn, titulo, especialidad, autor, editorial, edicion, anio, costo.
    obtener la lista de libros prestado, lista con las personas que se les presto algun libro.


    """
    def __init__(self, nombre):
        """
        Inicia la libreria con un nombre y una lista vacia de libros
        
        Parametros:
        nombre (str): nombre de la libreria.
        """
        self.nombre = nombre
        self.libros = []
        