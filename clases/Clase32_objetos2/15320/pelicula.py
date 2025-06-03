class Pelicula:
    def __init__(self, nombre, anio, categoria, descripccion):
        self.nombre = nombre
        self.anio = anio
        self.categoria = categoria
        self.descripccion = descripccion
        self.puntos = []
        self.promedio = 0
    def __str__(self):
        return "La pelicula es: " + self.nombre + " Su promedio es: "+str(self.promedio)
    
    def agregar_puntuacion(self, puntuacion):
        self.puntos.append(puntuacion)
        self.promedio = sum(self.puntos) / len(self.puntos)
   