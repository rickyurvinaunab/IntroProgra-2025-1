# Ejercicio 1: Comparación de Números
# Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.


# Solicitar al usuario un número
numero = int(input("Ingresa un numero: "))

if numero >= 0 and numero <= 0:
    print("Es un numero...")
# Verificar si el número es positivo
if numero > 0:
    print("El numero ", numero, " es positivo.")
# Verificar si el número es negativo
elif numero < 0:
    print("El numero ", numero, " es negativo.")
# Verificar si el número es cero
else:
    print("El numero ", numero, " es cero.")
# Imprimir el número ingresado
print("El numero ingresado es: ", numero)