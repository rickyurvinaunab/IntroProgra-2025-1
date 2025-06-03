from clase32 import Pelicula

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

netflix = Filmoteca()

pelicula1 = Pelicula("Star Wars I","Ficcion",200, 1999)
pelicula2 = Pelicula("Star Wars II","Ficcion",180, 2002)
pelicula3 = Pelicula("Star Wars III","Ficcion",180, 2002)
pelicula1.agregar_puntuacion(4)
pelicula1.agregar_puntuacion(3)
pelicula1.agregar_puntuacion(2)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(5)
pelicula2.agregar_puntuacion(3)
pelicula2.agregar_puntuacion(4)
netflix.agregar_pelicula(pelicula1)
netflix.agregar_pelicula(pelicula2)
netflix.agregar_pelicula(pelicula3)
print(netflix.peliculas)
