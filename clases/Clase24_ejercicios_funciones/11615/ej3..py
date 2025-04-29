# Crea una función llamada suma_multiples_tres(n) que 
# sume todos los números múltiplos del 3 desde 1 hasta n 
# inclusive 

def suma_multiples_tres(n):
    suma = 0
    for numero in range(1, n+1):
        if numero%3 == 0:
            suma += numero
    return suma

#Ejemplo 1
print(suma_multiples_tres(10)) #1,2,3,4,5,6,7,8,9,10
#Ejemplo 2
numero = 1500
resultado = suma_multiples_tres(numero)
print(resultado)

