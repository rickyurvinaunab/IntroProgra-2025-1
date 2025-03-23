# Ejercicio 5: Tabla de Multiplicar
# Escribe un programa que pida al usuario un número y utilice un bucle for para 
# imprimir la tabla de multiplicar de ese número del 1 al 10.

numero = int(input())

for i in range(1, 11):
    multiplicacion = numero * i
    print("Numero", numero ,"*", i, "=", multiplicacion)