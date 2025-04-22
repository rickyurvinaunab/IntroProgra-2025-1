# abrir el archivo desde Python
archivo = open('ejemplo2.txt','r')
contenido = archivo.readlines()
archivo.close()

archivo = open('ejemplo2.txt','w')

year = input("Ingresa el anio: ")
lista_anios = []

for linea in contenido:
    datos = linea.strip().split()
    print(datos)
    lista_anios.append(int(datos[0]))

lista_anios.append(int(year))
lista_anios.sort()
print(lista_anios)
lista_resultado = []
for num in lista_anios:
    lista_resultado.append(str(num)+"\n")
archivo.writelines(lista_resultado)
archivo.close()

# 1996 Ricardo Urvina
# 1995 Ingrid Medina
# 2003 Lucas Cauas
# 2005 Benja rosales
# 2007 Joseph Chuyes








# Python es un lenguaje de programación popular.
# Es utilizado para desarrollo web, análisis de datos, y más.
# Este archivo contiene varias líneas para practicar.
# La recursión es un concepto importante en Python.
# Puedes utilizar este archivo para contar las líneas.
# Puedes modificarlo, agregar más contenido, o leerlo con Python.
