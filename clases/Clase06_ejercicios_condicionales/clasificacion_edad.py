# Ejercicio 2: Clasificación de Edad
# Escribe un programa que pida al usuario su edad y clasifique en una de las siguientes categorías: niño (0-12), adolescente (13-19), adulto (20-64) o adulto mayor (65+).

# Solicitar al usuario su edad
edad = int(input("Ingresa tu edad: "))
# Verificar si la edad es de un niño
if edad >= 0 and edad <= 12:
    print("Eres un niño.")
# Verificar si la edad es de un adolescente
elif edad >= 13 and edad <= 19:
    print("Eres un adolescente.")
# Verificar si la edad es de un adulto
elif edad >= 20 and edad <= 64:
    print("Eres un adulto.")
# Verificar si la edad es de un adulto mayor
else:
    print("Eres un adulto mayor.")
# Imprimir la edad ingresada
print("Tu edad es: ", edad)