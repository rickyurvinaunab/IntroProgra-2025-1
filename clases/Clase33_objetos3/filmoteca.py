from pelicula import Pelicula


# crear clase Director, nombre, nacionalidad

class Director:
    
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Filmoteca:
    def __init__(self):
        self.peliculas = []

    def __str__(self):
        return "Filmoteca con " + str(len(self.peliculas)) + " películas."

    # crear funcion agregar_pelicula
    
    def agregar_pelicula(self, nombre, anio, categoria, descripccion, nombre_director, nacionalidad):
        
        director = Director(nombre_director, nacionalidad)
        pelicula = Pelicula(nombre, anio, categoria, descripccion, director)
        self.peliculas.append(pelicula)
        
    def director_mas_frecuente(self):
        directores = []
        for pelicula in self.peliculas:
            directores.append(pelicula.director.nombre)
        directores_unicos = []
        for director in directores:
            if director not in directores_unicos:
                directores_unicos.append(director)
        contador = []
        for director in directores_unicos:
            contador.append(directores.count(director))
        maximo = max(contador)
        indice = contador.index(maximo)
        return [directores_unicos[indice], maximo]
      
        
        
        

filmoteca = Filmoteca()
filmoteca.agregar_pelicula("Inception", 2010, "Ciencia ficcion", "Un ladron roba secretos a traves de los suenos.", "Christopher Nolan", "Britanico")
filmoteca.agregar_pelicula("Interstellar", 2014, "Ciencia ficcion", "Viaje a traves de un agujero de gusano.", "Christopher Nolan", "Britanico")
filmoteca.agregar_pelicula("Dunkirk", 2017, "Guerra", "Evacuacion durante la Segunda Guerra Mundial.", "Christopher Nolan", "Britanico")
filmoteca.agregar_pelicula("Jurassic Park", 1993, "Aventura", "Cientificos recrean dinosaurios en una isla remota.", "Steven Spielberg", "Estadounidense")

print(filmoteca)
print(filmoteca.director_mas_frecuente())
#  return esperado ['Christopher Nolan',3]