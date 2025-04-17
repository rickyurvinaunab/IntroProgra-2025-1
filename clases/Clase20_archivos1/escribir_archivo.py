# Usando el método write() para escribir en un archivo
archivo = open('ejemplo.txt', 'w')
archivo.write('Hola Mundo!')
lineas = [
    'Primera línea', 
    '\nSegunda línea', 
    '\nTercera línea'
]
archivo.writelines(lineas)
print('\nHola, Ricardo!', file=archivo)
archivo.close()

# # Usando writelines() para escribir en un archivo
# archivo = open('ejemplo.txt', 'w')
# lineas = [
#     'Primera línea', 
#     '\nSegunda línea', 
#     '\nTercera línea'
# ]
# archivo.writelines(lineas)
# archivo.close()

# # # Usando print() para escribir en un archivo
# manejador_archivo = open('ejemplo.txt', 'a')
# print('\nHola, mundo!', file=manejador_archivo)
# manejador_archivo.close()