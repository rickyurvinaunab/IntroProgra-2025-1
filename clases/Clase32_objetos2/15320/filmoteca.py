from pelicula import Pelicula
# __init__: Constructor que inicializa el atributo peliculas con una lista de instancias de Pelicula.
# __str__: Retorna una cadena que indica el número total de películas en la filmoteca.
# agregar_pelicula: Recibe una instancia de Pelicula y la agrega a la lista de peliculas.


class Filmoteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

    def __str__(self):
        return "La filmoteca es: "+self.nombre+" y tiene "+str(len(self.peliculas))+" peliculas"
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
    
# contar_por_anio: Cuenta cuántas películas hay en la filmoteca por año de lanzamiento y retorna una lista con el conteo.
    def contar_por_anio(self):
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
                    lista_anios[indice_a] =[anio, contador_anios]
            indice_a += 1
        return lista_anios
# mejor_pelicula: Encuentra y retorna la película con el mayor puntaje promedio.
    
    def mejor_pelicula(self):
        lista_promedios = []
        for peli in self.peliculas:
            lista_promedios.append(peli.promedio)
        max_promedio =  max(lista_promedios)
        for peli in self.peliculas:
            if peli.promedio == max_promedio:
                return peli
            
        return         

filmoteca = Filmoteca("Netflix")
pelicula1 = Pelicula("Star Wars 1", 1999, "Ficcion","Una pelicula de ficcion")
pelicula2 = Pelicula("Star Wars 2", 2002,"Ficcion","Otro pelicula de ficcion")
pelicula3 = Pelicula("Star Wars 3", 2005, "Ficcion","Una pelicula de ficcion")
pelicula4 = Pelicula("Star Wars 4", 2002, "Ficcion","Una pelicula de ficcion")
pelicula5 = Pelicula("Star Wars 5", 1999, "Ficcion","Una pelicula de ficcion")
filmoteca.agregar_pelicula(pelicula1)
filmoteca.agregar_pelicula(pelicula2)
filmoteca.agregar_pelicula(pelicula3)
filmoteca.agregar_pelicula(pelicula4)
filmoteca.agregar_pelicula(pelicula5)
print(filmoteca)
pelicula1.agregar_puntuacion(4.5)
pelicula1.agregar_puntuacion(1)
pelicula1.agregar_puntuacion(2)
pelicula3.agregar_puntuacion(5)
pelicula1.agregar_puntuacion(4)
pelicula1.agregar_puntuacion(3)
pelicula3.agregar_puntuacion(5)
pelicula3.agregar_puntuacion(3)
pelicula3.agregar_puntuacion(1)

print(filmoteca.contar_por_anio())