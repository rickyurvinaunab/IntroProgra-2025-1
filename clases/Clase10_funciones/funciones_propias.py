def encontrar_apellido(nombre):
    apellido=""
    for caracter in nombre: 
        if caracter==" ":
            break 
        apellido+=caracter 
    return apellido

nombre="GONZALEZ PEREZ JUAN PABLO"
apellido= encontrar_apellido(nombre)

print("El apellido obtenido de la función es:", apellido)