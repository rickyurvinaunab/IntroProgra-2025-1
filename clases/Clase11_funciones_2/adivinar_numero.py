# Supongamos que necesitamos construir una función donde el usuario intente adivinar
# un número entre el 1 y el 100. La cantidad de veces que puede el usuario intentar son 7. 
# Sin embargo el usuario puede solicitar más intentos al inicio del programa. 
# La función debe recibir la cantidad de intentos y si no se especifica debe tener 7 intentos. 
# Además, recibe el número a adivinar.
# El programa debe decirle al usuario si es mayor o menos el número ingresado. 
# Si adivina debe mostrar un mensaje que le diga que adivino el número y debe terminar el programa
import random

def adivinar_numero(numero_aleatorio,intentos=7):
    for i in range(intentos):
        print("Intento", i + 1)
        adivinanza = int(input("Ingrese un número entre 1 y 100: "))
        if adivinanza == numero_aleatorio:
            print("¡Adivinaste el número!")
            break
        elif adivinanza < numero_aleatorio:
            print("El número es mayor")
        else:
            print("El número es menor")
    print("El número era:", numero_aleatorio)
    print("Fin del juego")

print("Bienvenido al juego de adivinar el número")
print("Tienes 7 intentos para adivinar el número")

pregunta_intentos = input("Desea cambiar la cantidad de intentos? (s/n): ")
numero_aleatorio= random.randint(1,100)
if pregunta_intentos == "s":
    intentos = int(input("Ingrese la cantidad de intentos: "))
    adivinar_numero(numero_aleatorio,intentos)
else:
    adivinar_numero(numero_aleatorio)