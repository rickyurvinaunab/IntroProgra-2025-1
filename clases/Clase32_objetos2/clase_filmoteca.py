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

    def peliculas_por_categoria(self, categoria):
        resultado = []
        for pelicula in self.peliculas:
            if categoria in pelicula.categoria:
                resultado.append(pelicula)
        return resultado

    def obtener_promedios(self):
        for pelicula in self.peliculas:
            print(pelicula.nombre + " :", str(pelicula.promedio))

    def peliculas_por_rango_anio(self, anio_inicio, anio_fin):
        resultado = []
        for pelicula in self.peliculas:
            if anio_inicio <= pelicula.anio <= anio_fin:
                resultado.append(pelicula)
        return resultado

    def contar_por_categoria(self):
        conteo = []
        for pelicula in self.peliculas:
            encontrado = False
            for item in conteo:
                if item[0] == pelicula.categoria:
                    item[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                conteo.append([pelicula.categoria, 1])
        return conteo


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
print("Peliculas de Ciencia ficcion:")
for pelicula in filmoteca.peliculas_por_categoria("Ciencia ficcion"):
    print(pelicula)

print("Peliculas entre 2010 y 2015:")
for pelicula in filmoteca.peliculas_por_rango_anio(2010, 2015):
    print(pelicula)

print("Conteo por categoria:", filmoteca.contar_por_categoria())

filmoteca.obtener_promedios()

print("¿Es 'Una nueva esperanza' mejor que 'La amenaza fantasma'?:", pelicula2.es_mejor_que(pelicula1))
print("¿Es 'Dunkirk' mejor que 'La amenaza fantasma'?:", pelicula3.es_mejor_que(pelicula2))
