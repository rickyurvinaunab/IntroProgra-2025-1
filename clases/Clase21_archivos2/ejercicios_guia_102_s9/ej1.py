
# 1. Escribir un programa que pregunte al usuario los números 
# ganadores de la 
# lotería primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.

lista_ganadores = []
while True:
    print("Ingresa el numero ganador o ingresa -1 para salir.")
    numero = int(input("Ingresa el numero ganador: "))
    if numero == -1:
        break
    lista_ganadores.append(numero)
lista_ganadores.sort()
print("Numeros ganadores en Orden ascendente")
for ganador in lista_ganadores:
    print("El numero ganador es:", ganador)


# lista = list(range(1,11))

# resultado = ""
# for i in range(len(lista), 0, -1):
#     resultado += str(i)+","

# print(resultado)
# import copy

# abecedario ="abcdefghijklmnoprstuvwxyz"
# lista = []
# for letra in abecedario:
#     lista.append(letra)
# print(lista)
# copia = copy.deepcopy(lista)
# for i in range(1,len(copia)+1):
#     if i % 3 == 0:
#         elemento_a_eliminar = copia[i-1]
#         print("elemento a eliminar: ", elemento_a_eliminar)
#         lista.remove(elemento_a_eliminar)

# print(lista)

# numeros = [ 50, 75, 46, 22, 80, 65, 8]
# print("min", min(numeros))
# print("max", max(numeros))



















# 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física,
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura
# y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
# asignaturas que el usuario tiene que repetir.

# 5. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que
# contiene cada vocal