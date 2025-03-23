#Este script tiene como finalidad explicar el uso de import en Python
#Importar funciones de otros scripts
#Para importar funciones de otros scripts se utiliza la palabra reservada import seguida del nombre del script

#Ejemplo:
import random

#Para utilizar una función de un script importado se utiliza la sintaxis nombre_script.nombre_funcion()
aleatorio_1_10 = random.randint(1, 10)
#En este caso se importó la función randint() del script random, la cual devuelve un número entero aleatorio entre los dos números especificados.
print("Número aleatorio entre 1 y 10:", aleatorio_1_10)

#También se pueden importar todas las funciones de un script utilizando el asterisco (*)
#Ejemplo:
from random import *

aleatorio=randrange(1,10, 2)
#En este caso se importaron todas las funciones del script random, por lo que no es necesario utilizar la sintaxis nombre_script.nombre_funcion()
print("Número aleatorio entre 1 y 10:", aleatorio)