class Pelicula:
    """
    Clase que representa una pelicula con su informacion basica
    y permite registrar puntuaciones y calcular su promedio.

    Atributos:
    nombre (str): nombre de la pelicula.
    anio (int): anio de estreno de la pelicula.
    categoria (str): categoria o genero de la pelicula.
    descripccion (str): descripcion de la pelicula.
    puntos (list): lista de puntuaciones recibidas.
    promedio (float): promedio de las puntuaciones recibidas.
    """

    def __init__(self, nombre, anio, categoria, descripccion):
        """
        Inicializa una pelicula con sus atributos basicos.

        Parametros:
        nombre (str): nombre de la pelicula.
        anio (int): anio de estreno de la pelicula.
        categoria (str): categoria o genero de la pelicula.
        descripccion (str): descripcion de la pelicula.
        """
        self.nombre = nombre
        self.anio = anio
        self.categoria = categoria
        self.descripccion = descripccion
        self.puntos = []
        self.promedio = 0

    def __str__(self):
        """
        Retorna una descripcion de la pelicula con su nombre y promedio.

        Returns:
        str: descripcion de la pelicula.
        """
        return "La pelicula es: " + self.nombre + " Su promedio es: " + str(self.promedio)

    def agregar_puntuacion(self, puntuacion):
        """
        Agrega una nueva puntuacion a la pelicula y actualiza su promedio.

        Parametros:
        puntuacion (float): puntuacion a agregar (por ejemplo de 1 a 5).
        """
        self.puntos.append(puntuacion)
        self.promedio = sum(self.puntos) / len(self.puntos)

    def es_mejor_que(self, pelicula):
        """
        Compara esta pelicula con otra segun el promedio de puntuaciones.

        Parametros:
        pelicula (Pelicula): otra pelicula a comparar.

        Returns:
        bool: True si esta pelicula tiene un promedio mayor, False en caso contrario.
        """
        return self.promedio > pelicula.promedio