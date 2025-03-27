# Ejercicio 2: Suma de Números
# Escribe un programa que pida al usuario un número y utilice un bucle while para sumar todos los números desde 1 hasta el número ingresado.

# Solicitar al usuario un número
numero = int(input("Ingresa un numero: "))
# Inicializar la variable suma
suma = 0
# Inicializar la variable contador
contador = 1
# Iniciar el bucle while
while contador <= numero:
    # Sumar el contador a la suma
    suma += contador
    # Incrementar el contador
    contador += 1
# Imprimir la suma
print("La suma de los numeros desde 1 hasta ", numero, " es: ", suma)

