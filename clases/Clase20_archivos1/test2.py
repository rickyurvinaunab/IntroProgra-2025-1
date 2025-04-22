
archivo = open('ejemplo2.txt','r')
contenido = archivo.readlines()
print(contenido)
archivo.close()

archivo = open('ejemplo2.txt','w')
year = int(input("Ingresa el anio: "))
lista_nueva = []
for linea in contenido:
    dato = int(linea.strip())
    lista_nueva.append(dato)
lista_nueva.append(year)
lista_nueva.sort()
print(lista_nueva)
lista_final = []
for numero in lista_nueva:
    lista_final.append(str(numero)+"\n")
archivo.writelines(lista_final)
archivo.close()



# 1888
# 1996
# 1999
# 1999
# 2003
# 2007
# 2008