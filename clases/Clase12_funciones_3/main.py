# Escribir una función que calcule el máximo común divisor de dos números y
#  otra que calcule el mínimo común múltiplo.

def mcd(num1, num2):
    maximo = 1
    for divisor in range(1,  num1+1):
        if num1 % divisor == 0 and num2 % divisor== 0:
            maximo = divisor
    return maximo

print(mcd(8,20))