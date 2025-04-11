from suma import calcular_suma
from resta import calcular_resta
from division import calcular_division
from multi import calcular_multiplicacion

num1 =  float(input("Ingrese el # 1: "))
num2 =  float(input("Ingrese el # 2: "))
operacion = input("Ingrese la operacion: ")

if operacion == "+":
    resultado = calcular_suma(num1, num2)
elif operacion == "-":
    resultado = calcular_resta(num1, num2)
elif operacion == "/":
    resultado = calcular_division(num1, num2)
elif operacion == "*":
    resultado = calcular_multiplicacion(num1, num2)

print("El resultado de: ", operacion, "es:", resultado)