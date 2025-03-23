# Función para eliminar la palabra "fallo" del mensaje
def eliminar_fallo(mensaje):
    mensaje_limpio = ""
    i = 0
    while i < len(mensaje):
        if mensaje[i:i+len("fallo")] == "fallo":
            i += 5  # Saltamos la palabra "fallo"
        else:
            mensaje_limpio += mensaje[i]  # Añadimos el carácter al mensaje limpio
            i += 1  # Continuamos con el siguiente carácter
    return mensaje_limpio

# Función para buscar el nombre cada 2 caracteres
def buscar_nombre(mensaje):
    mensaje=eliminar_fallo(mensaje)
    nombre = ""
    i = 0
     # Recorremos el mensaje hasta encontrar una letra mayúscula
    while i < len(mensaje):
        if mensaje[i].isupper():
            # Comenzamos a formar el nombre una vez que encontramos la mayúscula
            while i < len(mensaje):
                nombre += mensaje[i]  # Añadimos la letra al nombre
                i += 2  # Tomamos una letra cada 2 caracteres
            return nombre # Return hace como break, rompe el ciclo y termina la función
        i += 1  # Seguimos buscando la mayúscula

# print(buscar_nombre("ehfoIfnfalloggrriidd"))