# Ejercicio 2: Suma de Números
# Escribe un programa que pida al usuario un número mayor de 1 y utilice un bucle for para sumar todos los números desde 1 hasta el número ingresado.

# Solicitar al usuario un número
numero = int(input("Ingresa un numero: "))
# Inicializar la variable suma
suma = 0
# Iniciar el bucle for
for contador in range(1, numero + 1):
    # Sumar el contador a la suma
    suma += contador
# Imprimir la suma
print("La suma de los numeros desde 1 hasta ", numero, " es: ", suma)
# Imprimir mensaje de fin
print("Fin del programa")