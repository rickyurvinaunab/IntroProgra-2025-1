# »	Ejercicio 1: Comparación de Números
# Escribe un programa que pida al usuario un número y 
# determine si es positivo, negativo o cero.

# num = int(input("Ingrese el numero: "))

# if num > 0:
#     print("Es positivo")
# elif num < 0:
#     print("Es negativo")
# else:
#     print("Es cero")










# »	Ejercicio 2: Clasificación de Edad
# Escribe un programa que pida al usuario su edad y 
# clasifique en una de las siguientes categorías: niño (0-12), 
# adolescente (13-19), adulto (20- 64) o adulto mayor (65+).
# edad = int(input("Ingrese la edad: "))

# if edad <0:
#     print("La edad no es valida")
# else:
#     if edad >= 0  and edad <=12:
#         print("Es un ninio")
#     elif edad >= 13 and edad <= 19:
#         print("Es un adolescente")
#     elif edad >= 20 and edad <= 64:
#         print("Es un adulto")
#     else:
#         print("Es un adulto mayor")









# »	Ejercicio 3: Calculadora Simple
# Escribe un programa que actúe como una calculadora simple. 
# Debe pedir al usuario dos números y una operación (+, -, *, /) y 
# luego mostrar el resultado de la operación.

num1 = int(input("ingrese el num 1: "))
num2 = int(input("ingrese el num 2: "))
operacion = input("Ingrese la operacion: ")

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/" and num2 > 0:
    print(num1 / num2)