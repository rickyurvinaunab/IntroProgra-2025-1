# Crea una función llamada filtrar_nombres(lista_nombres) que reciba una lista de strings y 
# devuelva una nueva lista que contenga solo los nombres con más de 5 letras. 

def filtrar_nombres(lista_nombres):
    lista_nueva = []

    for nombre in lista_nombres:
        if len(nombre)>5:
            lista_nueva.append(nombre)
    return lista_nueva

#Ejemplo 1
lista1 = ['Ricardo','Paul','Ingrid','Aldo','Anabelle','Benja']
lista_nueva =  filtrar_nombres(lista1)
for nombre in lista_nueva:
    print(nombre)

print("-"*8)
#Ejemplo 2
lista2 = ['Rodrigo','Vale','Pedro']
lista_nueva =  filtrar_nombres(lista2)
for nombre in lista_nueva:
    print(nombre)

