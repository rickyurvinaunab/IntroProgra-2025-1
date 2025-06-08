from pelicula import Pelicula
from filmoteca import Filmoteca
from graficos import graficar_promedios_peliculas, graficar_porcentaje_categorias

disney = Filmoteca("disney")

p1 = Pelicula("Star Wars Episodio IV", 1977, "Ficcion", "La primera pelicula de Star Wars.")
p2 = Pelicula("Star Wars Episodio V", 1980, "Ficcion", "La segunda pelicula de Star Wars.")
p3 = Pelicula("Star Wars Episodio VI", 1983, "Ficcion", "La tercera pelicula de Star Wars.")

p4 = Pelicula("El Rey Leon", 1994, "Animacion", "Clasico de Disney sobre el ciclo de la vida.")
p5 = Pelicula("La Bella y la Bestia", 1991, "Animacion", "Clasico cuento de Disney.")

p6 = Pelicula("Iron Man", 2008, "Accion", "El inicio del universo cinematografico de Marvel.")
p7 = Pelicula("Avengers: Endgame", 2019, "Accion", "El cierre de la saga del infinito de Marvel.")

p8 = Pelicula("Titanic", 1997, "Romance", "Historia romantica a bordo del Titanic.")
p9 = Pelicula("Inception", 2010, "Ciencia Ficcion", "Un thriller sobre los sueños y la mente.")
p10 = Pelicula("Jurassic Park", 1993, "Aventura", "Parque tematico con dinosaurios.")


p1.agregar_puntuacion(5)
p1.agregar_puntuacion(4)
p1.agregar_puntuacion(5)
p1.agregar_puntuacion(4)

p2.agregar_puntuacion(5)
p2.agregar_puntuacion(5)
p2.agregar_puntuacion(4)

p3.agregar_puntuacion(4)
p3.agregar_puntuacion(3)
p3.agregar_puntuacion(4)
p3.agregar_puntuacion(5)

p4.agregar_puntuacion(5)
p4.agregar_puntuacion(5)
p4.agregar_puntuacion(4)
p4.agregar_puntuacion(5)

p5.agregar_puntuacion(4)
p5.agregar_puntuacion(4)
p5.agregar_puntuacion(5)

p6.agregar_puntuacion(4)
p6.agregar_puntuacion(5)
p6.agregar_puntuacion(4)

p7.agregar_puntuacion(5)
p7.agregar_puntuacion(5)
p7.agregar_puntuacion(5)
p7.agregar_puntuacion(5)

p8.agregar_puntuacion(4)
p8.agregar_puntuacion(5)
p8.agregar_puntuacion(5)
p8.agregar_puntuacion(4)

p9.agregar_puntuacion(5)
p9.agregar_puntuacion(4)
p9.agregar_puntuacion(5)

p10.agregar_puntuacion(5)
p10.agregar_puntuacion(4)
p10.agregar_puntuacion(4)
p10.agregar_puntuacion(5)

disney.agregar_pelicula(p1)
disney.agregar_pelicula(p2)
disney.agregar_pelicula(p3)
disney.agregar_pelicula(p4)
disney.agregar_pelicula(p5)
disney.agregar_pelicula(p6)
disney.agregar_pelicula(p7)
disney.agregar_pelicula(p8)
disney.agregar_pelicula(p9)
disney.agregar_pelicula(p10)

print(disney)

print("Peliculas por anio:")
print(disney.contar_por_anio())

print("Peliculas por categoria:")
print(disney.contar_por_categoria())

mejor = disney.mejor_pelicula()
print("La mejor pelicula es:", mejor)

graficar_promedios_peliculas(disney)
graficar_porcentaje_categorias(disney)