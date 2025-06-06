from pelicula import Pelicula

class Filmoteca:

    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mejor_pelicula(self):
        puntuacion_max = 0
        nombre_max = ""
        for peli in self.peliculas:
            if peli.promedio > puntuacion_max:
                puntuacion_max = peli.promedio
                nombre_max = peli.nombre
        return nombre_max

# contar_por_anio: Cuenta cuántas películas hay en la filmoteca por año de lanzamiento y retorna una lista con el conteo.
    def contar_por_anio(self):
        lista_anios = []
        for peli in self.peliculas:
            if peli.anio not in lista_anios:
                lista_anios.append(peli.anio)

        indice_a = 0
        for anio in lista_anios:
            contador = 0
            for peli in self.peliculas:
                if anio == peli.anio:
                    contador += 1
            lista_anios[indice_a] = [anio, contador]
            indice_a += 1
        return lista_anios
    # mejor_pelicula: Encuentra y retorna la película con el mayor puntaje promedio.
    def mejor_pelicula(self):
        lista_promedios = []
        for peli in self.peliculas:
            lista_promedios.append(peli.promedio)
        max_promedio = max(lista_promedios)
        for peli in self.peliculas:
            if peli.promedio == max_promedio:
                return peli.nombre

netflix = Filmoteca()

pelicula1 = Pelicula("Star Wars I","Ficcion",200, 1999)
pelicula2 = Pelicula("Star Wars II","Ficcion",180, 2002)
pelicula3 = Pelicula("Star Wars III","Ficcion",180, 2002)
pelicula4 = Pelicula("Star Wars III","Ficcion",180, 2002)
pelicula5 = Pelicula("Star Wars III","Ficcion",180, 1900)
pelicula6 = Pelicula("Star Wars III","Ficcion",180, 1900)
pelicula7 = Pelicula("Star Wars III","Ficcion",180, 2005)

netflix.agregar_pelicula(pelicula1)
netflix.agregar_pelicula(pelicula2)
netflix.agregar_pelicula(pelicula3)
netflix.agregar_pelicula(pelicula4)
netflix.agregar_pelicula(pelicula5)
netflix.agregar_pelicula(pelicula6)
netflix.agregar_pelicula(pelicula7)
# print(netflix.contar_por_anio())


pelicula1.agregar_puntuacion(4)
pelicula1.agregar_puntuacion(3)
pelicula1.agregar_puntuacion(2)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(3)
pelicula2.agregar_puntuacion(4)
# print(netflix.peliculas)
print(netflix.mejor_pelicula())
