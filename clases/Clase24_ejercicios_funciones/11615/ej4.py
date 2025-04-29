# Crea una función llamada filtrar_nombres(lista_nombres) que 
# reciba una lista de strings y devuelva una nueva lista que 
# contenga solo los nombres que la longitud de su nombre sea par.
#  Por ejemplo: Ricardo tiene 7 caracteres, por lo cual no 
# formaría parte de la lista final. 
# Por otro lado, el nombre Aldo, tiene 4 caracteres por 
# lo que si formaría parte de la lista de retorno.

def filtrar_nombres(lista_nombres):
    lista_nueva = []

    for nombre in lista_nombres:
        if len(nombre)%2 == 0:
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

