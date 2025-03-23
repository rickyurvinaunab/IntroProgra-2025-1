def encontrar_segundo_apellido(nombre):
    apellido = ""
    contador = 0
    for caracter in nombre:
        if caracter == " ":
            contador += 1
            if contador == 2:
                break
        elif contador == 1:
            apellido += caracter
    return apellido

nombre = "GONZALEZ PEREZ JUAN"
apellido = encontrar_segundo_apellido(nombre)
print("El segundo apellido obtenido de la función es:", apellido)