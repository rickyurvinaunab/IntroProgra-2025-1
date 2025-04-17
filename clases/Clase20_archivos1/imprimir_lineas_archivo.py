manejador_archivo = open('ejemplo.txt', 'r')
lista = manejador_archivo.readlines()
n_lineas=0
nueva_lista=[]

for linea in lista:
    if n_lineas==1 or n_lineas==5:
        nueva_lista.append(linea.strip())
    n_lineas+=1

for linea in nueva_lista:
    print(linea)
    
# Output:
# Es utilizado para desarrollo web, análisis de datos, y más.

# Puedes modificarlo, agregar más contenido, o leerlo con Python.