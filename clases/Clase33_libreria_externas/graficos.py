import matplotlib.pyplot as plt

def graficar_promedios_peliculas(filmoteca):
    """
    Grafica un grafico de barras con el promedio de puntuaciones de las peliculas de la filmoteca.

    Parametros:
    filmoteca (Filmoteca): objeto de la clase Filmoteca.
    """
    resultado = filmoteca.obtener_promedios_peliculas()
    nombres = resultado[0]
    promedios = resultado[1]

    plt.figure(figsize=(10,6))
    plt.bar(nombres, promedios, color='skyblue')
    plt.title("Promedio de puntuaciones por pelicula")
    plt.xlabel("Peliculas")
    plt.ylabel("Promedio de puntuacion")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graficar_porcentaje_categorias(filmoteca):
    """
    Grafica un grafico de torta con el porcentaje de peliculas por categoria en la filmoteca.

    Parametros:
    filmoteca (Filmoteca): objeto de la clase Filmoteca.
    """
    resultado_cat = filmoteca.obtener_porcentaje_categorias()
    categorias = resultado_cat[0]
    cantidades = resultado_cat[1]

    plt.figure(figsize=(6,6))
    plt.pie(cantidades, labels=categorias, autopct='%d%%', startangle=140)
    plt.title("Distribucion de peliculas por categoria")
    plt.show()