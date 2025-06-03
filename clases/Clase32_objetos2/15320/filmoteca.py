from pelicula import Pelicula

class Filmoteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

    def __str__(self):
        return "La filmoteca es: "+self.nombre+" y tiene "+str(len(self.peliculas))+" peliculas"
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
    
    def contar_despues_2000(self):
        contador = 0
        for peli in self.peliculas:
            if peli.anio >= 2000:
                contador += 1
        
        return contador


filmoteca = Filmoteca("Netflix")
pelicula1 = Pelicula("Star Wars 1", 1999, "Ficcion","Una pelicula de ficcion")
pelicula2 = Pelicula("Star Wars 2", 2002,"Ficcion","Otro pelicula de ficcion")
pelicula3 = Pelicula("Star Wars 3", 2005, "Ficcion","Una pelicula de ficcion")
pelicula4 = Pelicula("Star Wars 4", 2007, "Ficcion","Una pelicula de ficcion")
pelicula5 = Pelicula("Star Wars 5", 2009, "Ficcion","Una pelicula de ficcion")
filmoteca.agregar_pelicula(pelicula1)
filmoteca.agregar_pelicula(pelicula2)
filmoteca.agregar_pelicula(pelicula3)
filmoteca.agregar_pelicula(pelicula4)
filmoteca.agregar_pelicula(pelicula5)
print(filmoteca)
pelis_2000 = filmoteca.contar_despues_2000()
print("La cantidad de peliculas desde el 2000 son:", pelis_2000)

pelicula1.agregar_puntuacion(4.5)
pelicula1.agregar_puntuacion(1)
pelicula1.agregar_puntuacion(2)
pelicula3.agregar_puntuacion(5)
pelicula1.agregar_puntuacion(4)
pelicula1.agregar_puntuacion(3)
pelicula3.agregar_puntuacion(5)
pelicula3.agregar_puntuacion(3)
pelicula3.agregar_puntuacion(1)

