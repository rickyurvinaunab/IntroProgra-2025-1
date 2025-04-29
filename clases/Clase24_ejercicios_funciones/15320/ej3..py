# Crea una función llamada suma_pares(n) que sume todos los números pares desde 2 hasta n inclusive 

def sum_pares(n):
    suma = 0
    for numero in range(2, n+1):
        if numero%2 == 0:
            suma += numero
    return suma

#Ejemplo 1
print(sum_pares(10)) #0,1,2,3,4,5,6,7,8,9,10
#Ejemplo 2
numero = 1500
resultado = sum_pares(numero)
print(resultado)

