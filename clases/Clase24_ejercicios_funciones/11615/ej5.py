# Crea una función contar_mayores_edad(nombre_archivo) que abra un archivo de texto, 
# lea todas sus líneas, y cree un archivo nuevo con las personas que son mayores de edad.
# El archivo tendrá el siguiente formato

def contar_mayores_edad(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    contenido =  archivo.readlines()
    archivo.close()
    lista_nueva = []
    for item in contenido:
        datos =  item.split()
        edad =  2025 - int(datos[2])
        if edad >= 18:
            lista_nueva.append(item)

    archivo = open('mayores.txt','w')
    archivo.writelines(lista_nueva)
    archivo.close()

#Ejemplo
nombre =  'datos.txt'
contar_mayores_edad(nombre)
