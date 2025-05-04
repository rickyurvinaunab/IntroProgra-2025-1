def calcular_media(lista):
    # Se inicializa una variable para acumular la suma
    suma = 0
    # Se recorre cada numero de la lista
    for numero in lista:
        suma = suma + numero
    # Se calcula la media dividiendo la suma entre la cantidad de elementos
    media = suma / len(lista)
    # Se retorna la media
    return media


def cuadrados(lista):
    # Se crea una lista vacia para guardar los cuadrados
    lista_cuadrados = []
    # Se recorre cada numero de la lista original
    for numero in lista:
        # Se calcula el cuadrado y se agrega a la nueva lista
        cuadrado = numero ** 2
        lista_cuadrados.append(cuadrado)
    # Se retorna la lista con los cuadrados
    return lista_cuadrados


def estadisticas(lista):
    # Paso 1: Calcular la media
    suma = 0
    for numero in lista:
        suma = suma + numero
    media = suma / len(lista)

    # Paso 2: Calcular diferencias al cuadrado y guardarlas en una nueva lista
    diferencias_cuadradas = []
    for numero in lista:
        diferencia = numero - media
        cuadrado = diferencia ** 2
        diferencias_cuadradas.append(cuadrado)

    # Paso 3: Calcular la varianza sumando los cuadrados y dividiendo por la cantidad
    suma_cuadrados = 0
    for valor in diferencias_cuadradas:
        suma_cuadrados = suma_cuadrados + valor
    varianza = suma_cuadrados / len(lista)

    # Paso 4: Calcular la desviacion tipica como la raiz cuadrada de la varianza
    desviacion = varianza ** 0.5

    # Se retorna un diccionario con los tres valores
    return [ media, varianza, desviacion]
