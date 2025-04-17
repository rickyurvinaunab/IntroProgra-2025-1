import csv

def leer_notas(nombre_archivo):
    archivo = open(nombre_archivo, 'r') 
    # enconding='utf-8-sig' es para evitar el BOM
    notas = []
    reader = csv.reader(archivo) 
    # reader es un objeto iterable
    cabecera = next(reader) 
    print(cabecera)
    # next() devuelve la siguiente línea del archivo
    print(cabecera)
    for linea in reader:
        notas.append(linea)
    
    archivo.close()
    return notas

nombre_archivo = 'notas.csv'
notas = leer_notas(nombre_archivo)
print(notas)