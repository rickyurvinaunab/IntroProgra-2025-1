cosas = list()
cosas.append('libro')
cosas.append(99)
print(cosas)
cosas.append('galleta')
print(cosas)
# ['libro', 99, 'galleta']

elemento_eliminado = cosas.pop() # remueve el ultimo
print(cosas)
print(elemento_eliminado)
cosas.remove(99) # remueve por el valor
print(cosas)

cosas.append('libro 2')
cosas.append(99)
print(cosas)
cosas.pop(1) # removiendo por indice
print(cosas)
