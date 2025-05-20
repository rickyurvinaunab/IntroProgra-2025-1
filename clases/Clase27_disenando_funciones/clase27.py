# Escriba una funcion que reciba una lista de numeros y retorne una lista con sus cuadrados

def cuadrados(lista_numeros):

    indice_l = 0
    for numero in lista_numeros:
        cuadrado =  numero**2
        lista_numeros[indice_l] = cuadrado
        indice_l += 1
    return lista_numeros

lista_numeros = [2,4,5]
resultado = cuadrados(lista_numeros)
print(resultado)