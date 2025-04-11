# Lista de listas con las notas de cada estudiante
notas = [
    [600, 600, 600, 600],  # Estudiante 1
    [600, 500, 600, 600],  # Estudiante 2
    [600, 600, 350, 450],  # Estudiante 3
    [600, 200, 450, 600]   # Estudiante 4
]

notas_e2 = notas[1]
print(notas_e2)
# [600, 500, 600, 600]

nota_s3_e4= notas[2][3]
print(nota_s3_e4)
# 450


notas[3][1] = 580
print(notas[3])
# [600, 580, 450, 600]

# recorrer e imprimir todas las notas
for fila in range(len(notas)):
    print("Estudiante", fila+1)
    for col in range(len(notas[fila])):
        print("Set", col + 1, ":", notas[fila][col])
    
# Estudiante 1
# Set 1 : 600
# Set 2 : 600
# Set 3 : 600
# Set 4 : 600
# Estudiante 2
# Set 1 : 600
# Set 2 : 500



#Obtener promedio de estudiante 3
suma = 0
for nota in notas[2]:
    suma += nota
promedio = suma / len(notas[2])
print("Promedio del estudiante 3:", promedio)
# Promedio del estudiante 3: 500.0

# otra forma de resolver
suma = sum(notas[2])
promedio = suma / len(notas[2])
print("Promedio del estudiante 3:", promedio)
# Numero de filas
print(len(notas))

# Numero de columnas
print(len(notas[0]))