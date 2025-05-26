from filmoteca import Director

class Pelicula:
    def __init__(self, nombre, anio, categoria, descripcion, director):
        self.nombre = nombre
        self.anio = anio
        self.categoria = categoria
        self.descripcion = descripcion
        self.director = director
        self.puntos = []
        self.promedio = 0

    def __str__(self):
        return "La película: " + self.nombre + " del año: " + str(self.anio) + " tiene un puntaje promedio de: " + str(self.promedio)

    def agregar_puntuacion(self, puntaje):
        self.puntos.append(puntaje)
        self.calcular_promedio()

    def calcular_promedio(self):
        if self.puntos:
            suma = sum(self.puntos)
            self.promedio = round(suma / len(self.puntos), 1)
        else:
            self.promedio = 0

    def es_mejor_que(self, otra_pelicula):
        return self.promedio > otra_pelicula.promedio
