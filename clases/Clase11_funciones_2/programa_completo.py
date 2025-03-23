import random


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

def encontrar_aleatorio_entre_1_y_10():
    aleatorio = random.randint(1, 10)
    return aleatorio

nombre = "GONZALEZ PEREZ JUAN"
apellido = encontrar_segundo_apellido(nombre)
print("El segundo apellido obtenido de la función es:", apellido)


aleatorio_1_10 = encontrar_aleatorio_entre_1_y_10()
print("Número aleatorio entre 1 y 10:", aleatorio_1_10)
