# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! 
# cada vez que se la invoque.

#Factorial

def calcular_area_circulo(radio):

    area = 3.14 * radio**2
    return area

def calcular_volumen_cilindro(radio, altura):

    area = calcular_area_circulo(radio)
    volumen =  area * altura
    return volumen

resultado =  calcular_volumen_cilindro(3, 5)
print("El volumen es: ", resultado)