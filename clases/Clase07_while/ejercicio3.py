# Ejercicio 3: Promedio de Notas
# Escribe un programa que permita al usuario ingresar un número desconocido de notas, calcular su promedio, y finalizar la entrada cuando el usuario ingrese una nota negativa.

# Solicitar al usuario una nota
nota = float(input("Ingresa una nota (o una nota negativa para terminar): "))
# Inicializar la variable suma
suma = 0
# Inicializar la variable contador
contador = 0
# Iniciar el bucle while
while nota >= 0:
    # Sumar la nota a la suma
    suma += nota
    # Incrementar el contador
    contador += 1
    # Solicitar al usuario una nota
    nota = float(input("Ingresa una nota (o una nota negativa para terminar): "))
# Calcular el promedio
if contador > 0:
    promedio = suma / contador
else:
    promedio = 0
# Imprimir el promedio
print("El promedio de las notas ingresadas es: ", promedio)
# Imprimir la cantidad de notas ingresadas
print("Se ingresaron ", contador, " notas.")
# Imprimir mensaje de fin
print("Fin del programa")