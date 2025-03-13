# Ejercicio 3: Calculadora Simple
# Escribe un programa que actúe como una calculadora simple. Debe pedir al usuario dos números y una operación (+, -, *, /) y luego mostrar el resultado de la operación.

# Solicitar al usuario dos números
numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
# Solicitar al usuario la operación a realizar
operacion = input("Ingresa la operacion a realizar (+, -, *, /): ")
# Realizar
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operacion no valida"
# Imprimir el resultado de la operación
print("El resultado de la operacion es: ", resultado)
# Imprimir los números ingresados
print("Los numeros ingresados son: ", numero1, " y ", numero2)