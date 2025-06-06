class Pelicula:

    def __init__(self, nombre, genero, duracion, anio):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.anio = anio
        self.puntos = []
        self.promedio = 0

    def __str__(self):
        texto = "El nombre de la peli es: "+ self.nombre
        return texto
    
    def agregar_puntuacion(self, puntuacion):
        self.puntos.append(puntuacion)
        self.calcular_promedio()
    
    def calcular_promedio(self):
        self.promedio = sum(self.puntos)/len(self.puntos)
