linea = 'Muchos         espacios'
etc = linea.split()
print(etc)
# ['Muchos', 'Espacios']
linea = 'primero;segundo;tercero'
cosa = linea.split()
print(cosa)
# ['primero;segundo;tercero']
print(len(cosa))
# 1
cosa = linea.split(';')
print(cosa)
# ['primero', 'segundo', 'tercero']
print(len(cosa))
# 3
abc = 'Con tres palabras'
cosas = abc.split()
print(cosas)
['Con', 'tres', 'palabras']
print(len(cosas))
# 3
print(cosas[0])
# Con

