
# 3. Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo, Matemáticas, Física,
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota 
# que ha sacado en cada asignatura
# y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
# por pantalla las
# asignaturas que el usuario tiene que repetir.
lista_asiganturas = []
while True:
    ramo = input("Ingresa el nombre del ramo, o ingresa hecho para terminar")
    if ramo == "hecho":
        break
    lista_asiganturas.append(ramo)

print(lista_asiganturas)
nombre = input("ingresa tu nombre: ")
lista_notas = []
for ramo in lista_asiganturas:
    nota = input("Ingresa tu nota del ramo "+ramo+": ")
    lista_notas.append([ramo, nota])
print(lista_notas)
for item in lista_notas:
    # item = lista_notas[2]
    if float(item[1]) > 4:
        lista_notas.remove(item)
print("las materias a repetir son: ")
for item in lista_notas:
    print(item)


















# lista_asignaturas = []
# import copy
# while True:
#     asignatura = input("Ingrese la asignatura o ingrese hecho para acabar.")
#     if asignatura == "hecho":
#         break
#     lista_asignaturas.append(asignatura)

# lista_notas = []

# nombre = input("Ingresa tu nombre: ")

# for ramo in lista_asignaturas:
#     nota = input("Ingresa tu nota en la asignatura: "+ramo)
#     lista_notas.append([ramo, nota])
# print("Notas totales")
# for nota in lista_notas:
#     print(nota)

# indice = 0
# copia_notas = copy.deepcopy(lista_notas)
# for nota in copia_notas:
#     if float(nota[1]) >= 4:
#         lista_notas.remove(nota)

# print("Asignaturas a repetir..")
# for nota in lista_notas:
#     print(nota)


