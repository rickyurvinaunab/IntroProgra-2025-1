class Filmoteca:
    """
    Clase que permite almacenar y gestionar una coleccion de peliculas.
    Permite agregar peliculas, contar peliculas por anio y categoria,
    obtener la mejor pelicula segun promedio, y obtener datos para graficar.
    """

    def __init__(self, nombre):
        """
        Inicializa la filmoteca con un nombre y una lista vacia de peliculas.

        Parametros:
        nombre (str): nombre de la filmoteca.
        """
        self.nombre = nombre
        self.peliculas = []

    def __str__(self):
        """
        Retorna una descripcion de la filmoteca con su nombre y cantidad de peliculas.

        Returns:
        str: descripcion de la filmoteca.
        """
        return "La filmoteca es: " + self.nombre + " y tiene " + str(len(self.peliculas)) + " peliculas"

    def agregar_pelicula(self, pelicula):
        """
        Agrega una pelicula a la filmoteca.

        Parametros:
        pelicula (Pelicula): objeto de la clase Pelicula a agregar.
        """
        self.peliculas.append(pelicula)

    def contar_por_anio(self):
        """
        Cuenta cuantas peliculas hay por anio.

        Returns:
        list: lista de listas con formato [anio (int), cantidad (int)].
        """
        lista_anios = []
        for peli in self.peliculas:
            if peli.anio not in lista_anios:
                lista_anios.append(peli.anio)
        indice_a = 0
        for anio in lista_anios:
            contador_anios = 0
            for peli in self.peliculas:
                if anio == peli.anio:
                    contador_anios += 1
                    lista_anios[indice_a] = [anio, contador_anios]
            indice_a += 1
        return lista_anios

    def contar_por_categoria(self):
        """
        Cuenta cuantas peliculas hay por categoria.

        Returns:
        list: lista de listas con formato [categoria (str), cantidad (int)].
        """
        lista_categorias = []
        for peli in self.peliculas:
            if peli.categoria not in lista_categorias:
                lista_categorias.append(peli.categoria)
        indice_c = 0
        for categoria in lista_categorias:
            contador_categorias = 0
            for peli in self.peliculas:
                if categoria == peli.categoria:
                    contador_categorias += 1
                    lista_categorias[indice_c] = [categoria, contador_categorias]
            indice_c += 1
        return lista_categorias

    def mejor_pelicula(self):
        """
        Retorna la pelicula con el mayor promedio de puntuacion.

        Returns:
        Pelicula or None: objeto Pelicula con el mayor promedio, o None si no hay peliculas.
        """
        lista_promedios = []
        for peli in self.peliculas:
            lista_promedios.append(peli.promedio)
        max_promedio = max(lista_promedios)
        for peli in self.peliculas:
            if peli.promedio == max_promedio:
                return peli
        return

    def obtener_promedios_peliculas(self):
        """
        Obtiene listas de nombres de peliculas y sus promedios de puntuacion.

        Returns:
        list: dos listas, una con nombres (list de str) y una con promedios (list de float).
        """
        nombres = []
        promedios = []
        for peli in self.peliculas:
            nombres.append(peli.nombre)
            promedios.append(peli.promedio)
        return [nombres, promedios]

    def obtener_porcentaje_categorias(self):
        """
        Obtiene listas de categorias y la cantidad de peliculas en cada categoria.

        Returns:
        list: dos listas, una con categorias (list de str) y una con cantidades (list de int).
        """
        lista_categorias = []
        for peli in self.peliculas:
            if peli.categoria not in lista_categorias:
                lista_categorias.append(peli.categoria)
        categorias = []
        cantidades = []
        for categoria in lista_categorias:
            contador = 0
            for peli in self.peliculas:
                if peli.categoria == categoria:
                    contador += 1
            categorias.append(categoria)
            cantidades.append(contador)
        return [categorias, cantidades]