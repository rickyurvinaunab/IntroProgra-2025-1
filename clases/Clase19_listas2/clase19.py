# # This code snippet is creating a list of lists called `original` with two inner lists. It then
# creates a shallow copy of the `original` list called `copia` using the `copy()` method.
# original = [
#     [34,55],
#     [88,66]
# ]

# copia = original.copy()
# print("original", original)
# print("copia", copia)
# print("-----------")
# copia[1][0] = 100
# print("original", original)
# print("copia", copia)

notas = [
    [600, 100, 50, 600],  # Estudiante 1
    [600, 500, 600, 600],  # Estudiante 2
    [600, 600, 350, 450],  # Estudiante 3
    [600, 200, 450, 600]   # Estudiante 4
]

max_promedio = 0
indice_max_promedio = 0
indice = 0
for estudiante in notas:
    promedio = sum(estudiante)/ len(estudiante)
    if promedio > max_promedio:
        max_promedio = promedio
        indice_max_promedio = indice

    indice += 1

print("El estudiante con mejor promedio es el estudiante: ", indice_max_promedio+1)



# for fila in range(len(notas)):
#     print("Estudiante", fila+1)
#     for col in range(len(notas[0])):
#         nota = notas[fila][col]
#         print("Set",col+1,":",nota)

# numero_estudiante = 1
# for notas_estudiante in notas:
#     # print("Notas estudiante", notas_estudiante)
#     print("Estudiante", numero_estudiante)
#     numero_set = 1
#     for nota in notas_estudiante:
#         print("Set",numero_set, ":", nota)
#         numero_set += 1
#     numero_estudiante += 1






# # Estudiante 1
# # Set 1 : 600
# # Set 2 : 600
# # Set 3 : 600
# # Set 4 : 600
# # Estudiante 2
# # Set 1 : 600
# # Set 2 : 500