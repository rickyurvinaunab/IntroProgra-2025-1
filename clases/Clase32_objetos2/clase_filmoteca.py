from clase_pelicula import Pelicula

class Filmoteca:
    def __init__(self, peliculas):
        self.peliculas = peliculas

    def __str__(self):
        return "Filmoteca con " + str(len(self.peliculas)) + " películas."

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def contar_por_anio(self):
        conteo = []
        for pelicula in self.peliculas:
            encontrado = False
            for item in conteo:
                if item[0] == pelicula.anio:
                    item[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                conteo.append([pelicula.anio, 1])
        return conteo

    def mejor_pelicula(self):
        if not self.peliculas:
            return None
        mejor = self.peliculas[0]
        for pelicula in self.peliculas:
            if pelicula.promedio > mejor.promedio:
                mejor = pelicula
        return mejor



pelicula1 = Pelicula("Una nueva esperanza", 1997, "Ciencia ficción", "Un joven granjero intercepta una llamada de socorro")
pelicula2 = Pelicula("La amenaza fantasma", 1999, "Ciencia ficción", "Los Jedi descubren a Anakin Skylwalker")
pelicula3 = Pelicula("Dunkirk", 2017, "Guerra", "Dramatica evacuacion de Dunkirk durante la Segunda Guerra Mundial")

pelicula1.agregar_puntuacion(8)
pelicula1.agregar_puntuacion(9)
pelicula2.agregar_puntuacion(9)
pelicula2.agregar_puntuacion(10)
pelicula3.agregar_puntuacion(7)
pelicula3.agregar_puntuacion(8)

filmoteca = Filmoteca([pelicula1, pelicula2, pelicula3])

print(filmoteca)
print("Conteo por año:", filmoteca.contar_por_anio())
print("Mejor pelicula:", filmoteca.mejor_pelicula())

print("¿Es 'Una nueva esperanza' mejor que 'La amenaza fantasma'?:", pelicula2.es_mejor_que(pelicula1))
print("¿Es 'Dunkirk' mejor que 'La amenaza fantasma'?:", pelicula3.es_mejor_que(pelicula2))
