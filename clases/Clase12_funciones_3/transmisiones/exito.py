def decodificar_exito(mensaje):
    nombre = ""

    i = 1
    while i < (len(mensaje)):
        nombre += mensaje[i]  # Añadimos la letra al nombre
        i += 2  # Avanzamos con la separación progresiva

    return nombre


# print(decodificar_exito("sSBalmuupeyln"))