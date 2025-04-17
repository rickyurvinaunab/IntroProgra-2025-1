# Escribamos un programa que verifique que las notas finales son las correctas, en el caso de que no sean las correctas actualizarlas
from leer_notas import leer_notas
from escribir_notas import escribir_notas_actualizadas

def convertir_notas(notas):
    for nota in notas:
        for i in range(1, len(nota)):
            nota[i] = int(nota[i])
    return notas

def verificar_nota(notas):
    notas_int = convertir_notas(notas)
    for nota in notas_int:
        suma = sum(nota[2:])
        nota_sobre_7 = int(suma*7/(len(nota[2:])*600))
        if nota_sobre_7 != nota[1]:
            nota[1] = nota_sobre_7
    escribir_notas_actualizadas('notas.csv', notas)
    
notas = leer_notas('notas.csv')
verificar_nota(notas)
 